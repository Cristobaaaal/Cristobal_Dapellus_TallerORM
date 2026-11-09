from conexion import Session
from modelos import Reserva


def cancelar_reserva(id_reserva: int):
    with Session.begin() as session:
        reserva = session.get(Reserva, id_reserva)

        if reserva is None:
            raise ValueError("No existe una reserva con ese ID.")

        reserva.sala.disponible = True
        session.delete(reserva)


def pedir_cancelacion() -> None:
    try:
        id_reserva = int(input("ID de la reserva: "))
    except ValueError:
        print("El ID de la reserva debe ser un número entero.")
        return

    try:
        cancelar_reserva(id_reserva)
    except ValueError as error:
        print(error)
        return

    print("Reserva cancelada. La sala vuelve a estar disponible.")