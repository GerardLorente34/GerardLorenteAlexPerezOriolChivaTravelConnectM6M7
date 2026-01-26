from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

# Importar todos los routers
from .routers.auth import router as auth_router
from .routers.usuario import router as users_router
from .routers.creador import router as creador_router
from .routers.viajero import router as viajero_router
from .routers.trips import router as trips_router
from .routers.chat import router as chat_router
from .routers.admin import router as admin_router
from .routers.promocion import router as promocion_router

app = FastAPI(title="Bienvenido a nuestra agencia de viajes")

# CORS - Debe configurarse antes de los routers
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5500",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API agencia de viajes"}

# Incluir routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(creador_router)
app.include_router(viajero_router)
app.include_router(trips_router)
app.include_router(chat_router)
app.include_router(admin_router)
app.include_router(promocion_router)


