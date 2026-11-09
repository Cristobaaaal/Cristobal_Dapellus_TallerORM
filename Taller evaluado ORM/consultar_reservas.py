from sqlalchemy import select
from conexion import Session
from modelos import Reserva


def consultar_reservas():
    with Session() as session:
        reservas = session.scalars(select(Reserva)).all()

        if not reservas:
            return print("No hay reservas registradas.")

        for reserva in reservas:
            print(
                f"ID: {reserva.id} | Estudiante: {reserva.estudiante} | "
                f"Sala: {reserva.sala.nombre} | Fecha: {reserva.fecha}"
            )