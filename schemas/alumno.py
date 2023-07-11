from pydantic import BaseModel
class Alumno(BaseModel):
    matricula:int
    nombre:str
    apellidos:str
    cuatrimestre:int
    promedio:float
 