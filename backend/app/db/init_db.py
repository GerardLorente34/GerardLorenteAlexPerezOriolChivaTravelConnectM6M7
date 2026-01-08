from .database import Base, engine
from ..models.alumno import Alumno
from ..models.curso import Curso
from ..models.alumno_curso import AlumnoCurso
from ..models.user import User  


Base.metadata.create_all(bind=engine)
