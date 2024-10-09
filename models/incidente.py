from models.medicamento import Medicamento
from models.usuario import Usuario
from datetime import datetime

class Incidente:
    def __init__(self, ID: int, FechaHora: str, Descripcion: str, Medicamento: Medicamento, PersonalInvolucrado: Usuario, AccionesCorrectivas: str):
        self.ID = ID
        self.FechaHora = FechaHora or datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Se establece la fecha y hora actual si no se proporciona
        self.Descripcion = Descripcion
        self.Medicamento = Medicamento
        self.PersonalInvolucrado = PersonalInvolucrado
        self.AccionesCorrectivas = AccionesCorrectivas

    def registrar_incidente(self):
        # Lógica para registrar el incidente
        print(f"Registrando incidente ID: {self.ID}")
        print(f"Fecha y Hora: {self.FechaHora}")
        print(f"Descripción: {self.Descripcion}")
        print(f"Medicamento: {self.Medicamento.Nombre} (Código: {self.Medicamento.Codigo})")
        print(f"Personal Involucrado: {self.PersonalInvolucrado.Nombre} ({self.PersonalInvolucrado.Rol})")
        print(f"Acciones Correctivas: {self.AccionesCorrectivas}")
        # Aquí podrías agregar lógica para guardar el incidente en una base de datos
