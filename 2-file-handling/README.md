
# 📁 Reto Técnico 2 – File Handling & DICOM Processing

Este proyecto en Python implementa una clase `FileProcessor` encargada de realizar operaciones sobre archivos y carpetas, incluyendo análisis de archivos CSV y lectura de archivos médicos DICOM, con extracción de imágenes incluidas.

---

## 🚀 Funcionalidades

### ✅ 1. Listado de contenido en carpetas
- Lista los archivos y subcarpetas dentro de un directorio.
- Muestra el tamaño, fecha de modificación y tipo.
- Maneja errores si la carpeta no existe.

### ✅ 2. Lectura y análisis de archivos CSV
- Imprime el número de columnas, nombres y cantidad de filas.
- Calcula promedio y desviación estándar para columnas numéricas.
- Si `summary=True`, resume valores únicos y su frecuencia en columnas no numéricas.
- Si se indica `report_path`, guarda el análisis en un `.txt`.

### ✅ 3. Lectura de archivos DICOM
- Imprime datos del paciente, modalidad y fecha del estudio.
- Permite extraer tags personalizados.
- Extrae imágenes del archivo `.dcm` como `.png` (soporta multiframe).

---

## 📂 Estructura de Archivos

```bash
.
├── file_processor.py      # Clase con toda la lógica
├── test_cases.py          # Casos de prueba
├── sample-02-csv.csv      # Archivo CSV de ejemplo
├── sample-02-dicom.dcm    # Archivo DICOM multiframe
├── sample-02-dicom-2.dcm  # Archivo DICOM simple
├── reports/               # Reportes generados del análisis CSV
├── logfile.log            # Registro de errores
└── README.md              # Este archivo
```

---

## 📦 Requisitos

- Python 3.8+
- Librerías:
  ```bash
  pip install pandas pydicom pillow
  ```

---

## 🧪 Cómo ejecutar el proyecto

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/TU_USUARIO/imexhs-prueba.git
   cd imexhs-prueba/2-file-handling
   ```

2. **Activa el entorno virtual (opcional):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Instala las dependencias:**
   ```bash
   pip install pandas pydicom pillow
   ```

4. **Ejecuta el script de prueba:**
   ```bash
   python test_cases.py
   ```

---

## 📌 Ejemplos de Salida

### 🗂️ Listar carpeta

```
📁 Carpeta: ./.
📦 Número de elementos: 8
📄 Archivos:
 - file_processor.py (0.00 MB, Modificado: ...)
📂 Carpetas:
 - reports (Modificado: ...)
```

### 📊 Análisis CSV

```
📄 Analizando archivo CSV: sample-02-csv.csv
🧾 Columnas: ['PatientID', 'Age', ...]
📊 Número de filas: 52
📐 Análisis de columnas numéricas:
 - Age: Promedio = 31.08, Desviación estándar = 7.41
🧵 Resumen de columnas no numéricas:
 - PatientID:
   • ab1: 1 veces
   ...
📄 Resumen guardado en: ./reports/sample-02-csv.csv_report.txt
```

### 🩻 Lectura de DICOM

```
===== PRUEBA DICOM 1 =====
📦 Analizando archivo DICOM: sample-02-dicom.dcm
👤 Paciente: Rubo DEMO
🗓️  Fecha de estudio: 19941013
📷 Modalidad: XA
🏷️  Tags personalizados:
 - Tag 0x10, 0x10: 'Rubo DEMO'
🌀 Imagen multiframe detectada: 96 frames
🖼️  Imagen extraída en: ./sample-02-dicom.png
```

---

## ⚠️ Notas

- El código incluye manejo de errores detallado y logging en `logfile.log`.
- Los archivos DICOM multiframe son soportados extrayendo solo el primer frame como imagen PNG.

---

## 📬 Contacto

**Jesús Alejandro Lora Tovar**  
📧 alejandroloratovar@outlook.com  
🔗 [https://github.com/Alejolora25](https://github.com/Alejolora25)

---
