from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers.viajero import router as viatger_router
from .routers.creator import router as creador_router
from .routers.admin import router as admin_router

app = FastAPI(title="Bienvenido a nuestra agencia de viajes")

print("APP ARRANCADA CORRECTAMENTE")


# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API agencia de viajes"}

# Incluir rutas
app.include_router(viatger_router)
app.include_router(creador_router)
app.include_router(admin_router)


# Lista de orígenes permitidos
origins = [
    "http://localhost:5500",  # si tu frontend corre aquí
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],  # permite cualquier origen (no recomendable en producción)
    allow_origins=origins,  # permite solo esos orígenes
    allow_credentials=True,
    allow_methods=["*"],    # permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],    # permite todas las cabeceras
)


