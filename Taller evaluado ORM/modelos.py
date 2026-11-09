from sqlalchemy import ForeignKey, Integer, String, Boolean, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):
    __tablename__= "salas"
    __table_args__=(
        CheckConstraint("capacidad > 0", name="ck_capacidad"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(Integer, nullable=False)
    disponible: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")

class Reserva(Base):
    __tablename__= "reservas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("salas.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)
    sala: Mapped["Sala"] = relationship(back_populates="reservas")




