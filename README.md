# Cristobal_Dapellus_TallerORM
Taller evaluado de Programación II (ICINF1109).
Cristóbal Dapellus

Aplicación de consola que permite registrar y consultar salas de estudio, crear reservas y cancelarlas. Cada sala admite una sola reserva activa a la vez. Al cancelar una reserva, la sala vuelve a quedar disponible.

## Requisitos

- Python 3.10 o superior.
- SQLAlchemy 2.x.
- SQLite, incluido con Python.

## Instalación y ejecución en Windows

Abre PowerShell en la carpeta que contiene `main.py`. Crea el entorno virtual e instala SQLAlchemy:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "SQLAlchemy>=2.0,<3.0"
python -c "import sqlalchemy; print(sqlalchemy.__version__)"
```

Verifica que la conexión en `conexion.py` use la URL `sqlite:///reservas.db`. Luego inicia el programa:

```powershell
python main.py
```

Al iniciar, el programa crea las tablas si aún no existen. La base `reservas.db` se guarda en la carpeta desde donde ejecutas el programa.

## Menú
1. Registrar una sala con nombre y capacidad.
2. Consultar las salas y su disponibilidad. 
3. Reservar una sala con el nombre del estudiante, el ID de la sala y una fecha en formato `AAAA-MM-DD`.
4. Consultar las reservas y sus IDs. 
5. Cancelar una reserva usando su ID. 
6. Salir.

## Casos de prueba
1. CP-01 Crea Sala A con 6 cupos y Sala B con 4. Consulta las salas y anota el ID de Sala A. Ambas disponibles.
2. CP-02 Reserva Sala A para Ana con una fecha válida. Se registra la reserva y Sala A queda ocupada.
3. CP-03 Intenta reservar Sala A para Pedro. El programa rechaza la solicitud.
4. CP-04 Consulta las reservas y anota el ID de la reserva de Ana. Aparece la reserva de Ana con el nombre de Sala A y la fecha.
5. CP-05 Cancela la reserva de Ana y consulta las salas. La reserva se elimina y Sala A vuelve a estar disponible.
6. CP-06 Reserva Sala A para Pedro. La reserva se registra y Sala A queda ocupada.

Para comprobar la persistencia, sal con la opción `0`, abre el programa de nuevo y consulta las reservas. La reserva de Pedro debe seguir apareciendo.
