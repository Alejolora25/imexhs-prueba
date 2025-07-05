import os
import csv
import logging
from typing import List, Tuple, Optional
import pandas as pd
import pydicom
from PIL import Image
import numpy as np

class FileProcessor:
    def __init__(self, base_path: str, log_file: str = "logfile.log"):
        self.base_path = base_path
        self.logger = logging.getLogger("FileProcessor")
        self.logger.setLevel(logging.ERROR)
        handler = logging.FileHandler(os.path.join(base_path, log_file))
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        folder_path = os.path.join(self.base_path, folder_name)

        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            self.logger.error(f"Folder not found: {folder_path}")
            print(f"❌ Carpeta no encontrada: {folder_path}")
            return

        elements = os.listdir(folder_path)
        print(f"📁 Carpeta: {folder_path}")
        print(f"📦 Número de elementos: {len(elements)}")

        files = []
        folders = []

        for item in elements:
            full_path = os.path.join(folder_path, item)
            if os.path.isfile(full_path):
                files.append(full_path)
            elif os.path.isdir(full_path):
                folders.append(full_path)

        if files:
            print("📄 Archivos:")
            for file in files:
                name = os.path.basename(file)
                if details:
                    size_mb = os.path.getsize(file) / (1024 * 1024)
                    modified = os.path.getmtime(file)
                    from datetime import datetime
                    mod_str = datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M:%S')
                    print(f" - {name} ({size_mb:.2f} MB, Modificado: {mod_str})")
                else:
                    print(f" - {name}")

        if folders:
            print("📂 Carpetas:")
            for folder in folders:
                name = os.path.basename(folder)
                if details:
                    modified = os.path.getmtime(folder)
                    from datetime import datetime
                    mod_str = datetime.fromtimestamp(modified).strftime('%Y-%m-%d %H:%M:%S')
                    print(f" - {name} (Modificado: {mod_str})")
                else:
                    print(f" - {name}")


    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        try:
            file_path = os.path.join(self.base_path, filename)
            df = pd.read_csv(file_path)

            print(f"📄 Analizando archivo CSV: {filename}")
            print(f"🧾 Columnas: {list(df.columns)}")
            print(f"📊 Número de filas: {len(df)}")

            numeric_cols = df.select_dtypes(include='number')
            non_numeric_cols = df.select_dtypes(exclude='number')

            print("📐 Análisis de columnas numéricas:")
            stats_lines = []
            for col in numeric_cols.columns:
                avg = numeric_cols[col].mean()
                std = numeric_cols[col].std()
                print(f" - {col}: Promedio = {avg:.2f}, Desviación estándar = {std:.2f}")
                stats_lines.append(f"{col}: Promedio = {avg:.2f}, Desviación estándar = {std:.2f}")

            if summary and not non_numeric_cols.empty:
                print("🧵 Resumen de columnas no numéricas:")
                for col in non_numeric_cols.columns:
                    unique_vals = non_numeric_cols[col].value_counts()
                    print(f" - {col}:")
                    for val, freq in unique_vals.items():
                        print(f"    • {val}: {freq} veces")

            if report_path:
                os.makedirs(report_path, exist_ok=True)
                report_file = os.path.join(report_path, f"{filename}_report.txt")
                with open(report_file, "w", encoding="utf-8") as f:
                    f.write("Resumen estadístico de columnas numéricas:\n")
                    f.write("\n".join(stats_lines))
                print(f"📄 Resumen guardado en: {report_file}")

        except FileNotFoundError:
            self.logger.error(f"Archivo no encontrado: {filename}")
            print(f"❌ Error: Archivo no encontrado: {filename}")
        except pd.errors.EmptyDataError:
            self.logger.error(f"Archivo vacío o inválido: {filename}")
            print(f"❌ Error: Archivo vacío o inválido: {filename}")
        except Exception as e:
            self.logger.error(f"Error leyendo CSV {filename}: {e}")
            print(f"❌ Error inesperado: {e}")


    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        dicom_path = os.path.join(self.base_path, filename)
        print(f"📦 Analizando archivo DICOM: {filename}")

        try:
            dataset = pydicom.dcmread(dicom_path)

            # Datos básicos
            patient_name = getattr(dataset, "PatientName", "Desconocido")
            study_date = getattr(dataset, "StudyDate", "Sin fecha")
            modality = getattr(dataset, "Modality", "Desconocida")

            print(f"👤 Paciente: {patient_name}")
            print(f"🗓️  Fecha de estudio: {study_date}")
            print(f"📷 Modalidad: {modality}")

            # Leer tags personalizados
            if tags:
                print("🏷️  Tags personalizados:")
                for group, element in tags:
                    tag = (group, element)
                    value = dataset.get(tag, "No encontrado")
                    print(f" - Tag {hex(group)}, {hex(element)}: {value}")

            # Extraer imagen (soporte para multiframe)
            if extract_image:
                if 'PixelData' in dataset:
                    arr = dataset.pixel_array

                    # Si multiframe (3D), tomar el primer frame
                    if arr.ndim == 3:
                        print(f"🌀 Imagen multiframe detectada: {arr.shape[0]} frames")
                        arr = arr[0]  # primer frame

                    img = Image.fromarray(arr)

                    # Convertimos si no es formato de imagen
                    if img.mode != "L":
                        img = img.convert("L")

                    output_path = os.path.join(self.base_path, filename.replace(".dcm", ".png"))
                    img.save(output_path)
                    print(f"🖼️  Imagen extraída en: {output_path}")
                else:
                    raise ValueError("El archivo DICOM no contiene datos de imagen (PixelData)")

        except FileNotFoundError:
            print("❌ Archivo DICOM no encontrado.")
            self.logger.error(f"Archivo no encontrado: {dicom_path}")
        except Exception as e:
            print("❌ Error al procesar el archivo DICOM.")
            self.logger.error(f"Error procesando {filename}: {str(e)}")


