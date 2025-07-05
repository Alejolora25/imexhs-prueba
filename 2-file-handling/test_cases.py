from file_processor import FileProcessor

processor = FileProcessor(base_path=".", log_file="logfile.log")

# Prueba: listar el contenido de esta misma carpeta
processor.list_folder_contents(folder_name=".", details=True)

# Testeo de archivo CSV
processor.read_csv(filename="sample-02-csv.csv", summary=True, report_path="./reports")

# ==== PRUEBA DICOM 1 ====
print("\n===== PRUEBA DICOM 1 =====")
processor.read_dicom(
    filename="sample-02-dicom.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],  # PatientName, Modality
    extract_image=True
)

# ==== PRUEBA DICOM 2 ====
print("\n===== PRUEBA DICOM 2 =====")
processor.read_dicom(
    filename="sample-02-dicom-2.dcm",
    tags=[(0x0010, 0x0020), (0x0008, 0x0020)],  # PatientID, StudyDate
    extract_image=True
)

