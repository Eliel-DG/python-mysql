from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Float
from config.db import meta,engine
alumnos=Table("alumnos", meta,
              Column("matricula",Integer, primary_key=True),
              Column("nombre", String(100)),
              Column("apellidos", String(100)),
              Column("cuatrimestre", Integer),
              Column("promedio",Float))
meta.create_all(engine)