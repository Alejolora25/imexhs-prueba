# Prueba Técnica IMEXHS - Fullstack Developer

Este repositorio contiene la solución completa a la prueba técnica para el cargo de desarrollador en **IMEXHS (Imaging Experts and Healthcare Services)**. Cada reto está ubicado en una carpeta independiente y cuenta con su propio archivo `README.md` con las instrucciones detalladas de ejecución, dependencias y estructura del proyecto.

---

## Estructura del repositorio

```
/
├── 1-recursion-colors/      # Reto 1: Recursividad con reglas de colores
├── 2-file-handling/         # Reto 2: Manejo de archivos CSV y DICOM
├── 3-restful-api/           # Reto 3: API RESTful con FastAPI y PostgreSQL
├── 4-angular-app/           # Reto 4: Aplicación Angular para estimar área de mancha
└── README.md                # Este archivo general con descripción de todos los retos
```

Cada carpeta contiene:

- Código fuente del reto correspondiente
- Archivo `README.md` con instrucciones específicas
- Requisitos para ejecución y configuración del entorno

---

## Descripción de cada reto

### 1. 📊 Recursion and Colors

Simulación de la Torre de Hanoi con una restricción adicional: discos del mismo color no pueden estar directamente uno sobre otro. Se usó **Python** y recursividad para resolver el problema, retornando la secuencia de movimientos o `-1` si es imposible.

### 2. 🗂️ File Handling and Array Operations

Clase `FileProcessor` en Python que permite:

- Listar archivos de una carpeta con detalles
- Analizar archivos `.csv` (estadísticas numéricas y resumen de columnas categóricas)
- Leer archivos DICOM usando `pydicom`, imprimir tags y exportar imagen como `.png`

Incluye manejo de errores, uso de `logging` y generación de reportes.

### 3. 🚀 RESTful API

API desarrollada en **FastAPI** con base de datos **PostgreSQL** para almacenar resultados de procesamiento de imágenes médicas. Características:

- CRUD completo con validaciones, normalización de datos y filtros
- Modelos relacionales para `Device` y `ImageData`
- Endpoints para creación, consulta filtrada, actualización y eliminación de datos
- Logging de peticiones y errores

### 4. 🎨 Angular App

Aplicación desarrollada en **Angular 17** con **Angular Material** y **Bootstrap** para calcular el área de una mancha en una imagen binaria usando un algoritmo probabilístico.

Características:

- Subida de imagen con vista previa
- Selector deslizante para cantidad de puntos aleatorios
- Cálculo del área estimada y almacenamiento de resultados en tabla
- Componente tipo stepper que explica la metodología paso a paso

División clara en componentes standalone, uso de Signals para manejo de estado, estilos modernos y responsive.

---

## ⬆️ Instrucciones generales

1. Clona este repositorio:

```bash
git clone https://github.com/Alejolora25/imexhs-prueba.git
cd imexhs-prueba
```

2. Revisa el `README.md` dentro de cada carpeta para instrucciones específicas de instalación y ejecución.

3. Asegúrate de tener:

- Python 3.10+
- Node.js y Angular CLI para el reto 4
- PostgreSQL para el reto 3

---

## 👤 Autor

**Jesús Alejandro Lora Tovar**\
📧 [alejandroloratovar@outlook.com](mailto\:alejandroloratovar@outlook.com)\
🔗 [https://github.com/Alejolora25](https://github.com/Alejolora25)

---

