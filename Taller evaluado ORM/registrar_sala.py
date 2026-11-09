from conexion import Session
from modelos import Sala


def insertar_sala(nombre: str, capacidad: int):
    nombre = nombre.strip()

    if not nombre:
        raise ValueError("El nombre de la sala es obligatorio.")
    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")

    with Session.begin() as session:
        sala = Sala(nombre=nombre, capacidad=capacidad)
        session.add(sala)


def registrar_sala() -> None:
    nombre = input("Nombre de la sala: ")

    try:
        capacidad = int(input("Capacidad: "))
    except ValueError:
        return print("La capacidad debe ser un número entero.") 
    try:
        insertar_sala(nombre, capacidad)
    except ValueError as error:
        return print(error)

    print("Sala registrada correctamente.")