from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers.alumno import router as alumno_router
from .routers.curso import router as curso_router
from .routers.user import router as user_router
from .routers.auth import router as auth_router

app = FastAPI(title="CRUD N:N en FastAPI con MySQL")

# Ruta raíz
@app.get("/")
def read_root():
    return {"message": "API de Alumnos y Cursos"}

# Incluir rutas
app.include_router(alumno_router)
app.include_router(curso_router)
app.include_router(user_router)
app.include_router(auth_router)

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

#user: Jorge
#password: Jorge123
