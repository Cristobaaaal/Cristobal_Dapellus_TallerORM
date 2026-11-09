from sqlalchemy import select
from conexion import Session
from modelos import Sala


def consultar_salas():
    with Session() as session:
        salas = session.scalars(select(Sala)).all()

        if not salas:
            return print("No hay salas registradas.")
            

        for sala in salas:
            if sala.disponible is True:
                estado="Disponible"
            else:
                estado="No disponible"
            print(f"ID: {sala.id} | {sala.nombre} | {sala.capacidad} cupos | {estado}")