from fastapi import APIRouter
from config.db import conn
from models.alumno import alumnos
from schemas.alumno import Alumno
router=APIRouter()

@router.get('/getAll')
def ObtenerAlumnos():
    result=conn.execute(alumnos.select()).fetchall()
    response=[]
    for tuple in result:
        alumno={
            "matricula":tuple[0],
            "nombre":tuple[1],
            "apellidos":tuple[2],
            "cuatrimestre":tuple[3],
            "promedio":tuple[4],
        }
        response.append(alumno)
    return response
@router.post('/insert')
def InsertarAlumno(alumno:Alumno):
    conn.execute(alumnos.insert().values(dict(alumno)))
    conn.commit()
    res={
        "status":"Alumno insertado con exito"
    }
    return res

@router.delete('/delete/{matricula}')
def EliminarAlumno(matricula: int):
    conn.execute(alumnos.delete().where(alumnos.c.matricula == matricula))
    conn.commit()
    res = {
        "status": f"Alumno con matrícula {matricula} eliminado con éxito"
    }
    return res
