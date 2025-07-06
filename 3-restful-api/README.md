# IMEXHS Medical Image API

RESTful API desarrollada en **FastAPI** y **PostgreSQL** para almacenar, procesar y consultar resultados de procesamiento de imágenes médicas.

## 📅 Descripción

Esta API permite cargar archivos JSON estructurados con datos de dispositivos de imagen, validar y normalizar los datos, calcular promedios antes y después de la normalización, y realizar operaciones CRUD completas sobre los resultados.

## 🚀 Características

- Crear entradas a partir de datos JSON (con validación y procesamiento).
- Consultar todos los elementos o filtrarlos por fecha, promedio, y tamaño.
- Consultar un solo elemento por ID.
- Actualizar el nombre del dispositivo o ID.
- Eliminar entradas por ID.
- Relación entre elementos y dispositivos mediante Foreign Key.

---

## 📁 Estructura del proyecto

```
app/
├── crud.py              # Lógica de negocio y operaciones con la DB
├── database.py          # Configuración de PostgreSQL y sesión de DB
├── models.py            # Modelos SQLAlchemy (Device y ImageElement)
├── routers/
│   └── elements.py      # Endpoints CRUD de la API
├── schemas.py           # Pydantic schemas para validación
main.py                  # Inicialización de la app FastAPI
```

---

## 📝 Requisitos

- Python 3.10+
- PostgreSQL 13+

### Instalación

```bash
git clone https://github.com/Alejolora25/medical-image-api.git
cd medical-image-api
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configura tus variables de entorno (opcional)

```bash
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=root
export POSTGRES_DB=imexhs_db
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

---

## 🚩 Uso de la API

Levanta el servidor:

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

### ✉ Endpoints disponibles

#### Crear elementos (POST)

- **POST** `/api/elements/`
- Payload JSON:

```json
{
  "1": {
    "id": "aabbcc1",
    "data": [
      "78 83 21 68 96 46 40 11 1 88",
      "58 75 71 69 33 14 15 93 18 54"
    ],
    "deviceName": "CT SCAN"
  }
}
```

#### Consultar todos (GET)

- **GET** `/api/elements/`
- Soporta filtros opcionales por:
  - `created_from`, `created_to`
  - `avg_before_gt`, `avg_after_lt`
  - `data_size_gt`, etc.

#### Consultar uno (GET)

- **GET** `/api/elements/{id}`

#### Actualizar (PUT)

- **PUT** `/api/elements/{id}`
- Body JSON:

```json
{
  "device_name": "MRI SCANNER",
  "new_id": "nuevo_id"
}
```

#### Eliminar (DELETE)

- **DELETE** `/api/elements/{id}`

---

## 📂 Base de datos

Se crean dos tablas:

- **devices**: lista de dispositivos
- **image\_elements**: cada entrada con promedios, data size, timestamps y FK a `devices`

---

## ❌ Manejo de errores

- Código 422 para errores de validación
- Código 404 si no se encuentra un recurso
- Código 409 para IDs duplicados

---

## 💡 Extras

- Los datos numéricos se validan y normalizan automáticamente.
- Se calcula promedio antes y después de la normalización.

---

## 👤 Autor

Jesús Alejandro Lora Tovar\
📧 [alejandroloratovar@outlook.com](mailto\:alejandroloratovar@outlook.com)\
🔗 [https://github.com/Alejolora25](https://github.com/Alejolora25)

