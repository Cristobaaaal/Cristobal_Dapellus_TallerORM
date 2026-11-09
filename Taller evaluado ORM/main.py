from conexion import engine, Session
import modelos 
import crear_tablas
from registrar_sala import registrar_sala
from consultar_salas import consultar_salas
from registrar_reserva import pedir_reserva
from consultar_reservas import consultar_reservas
from cancelar_reserva import pedir_cancelacion

def conexion():
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
    conexion = engine.connect()
    return conexion

def mostrar_menu():
    print("======== Menú ========")
    print("1. Registrar sala")
    print("2. Consultar salas")
    print("3. Registrar reserva")
    print("4. Consultar reservas")
    print("5. Cancelar reserva")
    print("6. Salir")
    print("======================")

def main():
    conexion()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_sala()
        elif opcion == "2":
            consultar_salas()
        elif opcion == "3":
            pedir_reserva()
        elif opcion == "4":
            consultar_reservas()
        elif opcion == "5":
            pedir_cancelacion()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
