from datetime import date
from conexion import Session
from modelos import Reserva, Sala


def registrar_reserva(estudiante: str, sala_id: int, fecha: str):
    estudiante = estudiante.strip()
    fecha = fecha.strip()

    if not estudiante:
        raise ValueError("El nombre del estudiante es obligatorio.")

    mensaje_fecha = "Ingresa una fecha válida en formato AAAA-MM-DD."
    try:
        fecha_validada = date.fromisoformat(fecha)
    except ValueError:
        raise ValueError(mensaje_fecha) from None

    if fecha_validada.isoformat() != fecha:
        raise ValueError(mensaje_fecha)

    with Session.begin() as session:
        sala = session.get(Sala, sala_id)

        if sala is None:
            raise ValueError("No existe una sala con ese ID.")
        if not sala.disponible:
            raise ValueError("La sala ya tiene una reserva activa.")

        reserva = Reserva(estudiante=estudiante, sala=sala, fecha=fecha)
        session.add(reserva)
        sala.disponible = False


def pedir_reserva():
    estudiante = input("Nombre del estudiante: ")

    try:
        sala_id = int(input("ID de la sala: "))
    except ValueError:
        print("El ID de la sala debe ser un número entero.")
        return

    fecha = input("Fecha (AAAA-MM-DD): ")

    try:
        registrar_reserva(estudiante, sala_id, fecha)
    except ValueError as error:
        print(error)
        return

    print("Reserva registrada correctamente.")