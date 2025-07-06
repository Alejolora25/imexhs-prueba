from fastapi import FastAPI
from app.routers import elements
from app import models
from app.database import engine
from app.database import init_db  


# Inicializar la app
app = FastAPI(
    title="IMEXHS Medical Image API",
    description="RESTful API para almacenar y consultar resultados de procesamiento de imágenes médicas.",
    version="1.0.0"
)

# Crea las tablas al iniciar
init_db()

# Incluir las rutas
app.include_router(elements.router)
