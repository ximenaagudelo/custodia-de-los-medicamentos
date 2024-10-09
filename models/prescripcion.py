from models.medicamento import Medicamento
from models.usuario import Usuario

class Prescripcion:
    def __init__(self, ID: int, FechaPrescripcion: str, Medicamentos: list[Medicamento], Dosis: str, Doctor: Usuario):
        self.ID = ID
        self.FechaPrescripcion = FechaPrescripcion
        self.Medicamentos = Medicamentos
        self.Dosis = Dosis
        self.Doctor = Doctor

    def asignar_prescripcion(self):
        # Lógica para asignar la prescripción al paciente.
        pass

    def validar_interacciones(self):
        # Validar si los medicamentos en la prescripción tienen interacciones peligrosas.
        interacciones_detectadas = []
        for medicamento in self.Medicamentos:
            for interaccion in medicamento.Interacciones:
                interacciones_detectadas.append(interaccion)
        if interacciones_detectadas:
            # Aquí podrías generar una alerta o realizar alguna acción correctiva.
            print(f"Interacciones detectadas: {interacciones_detectadas}")
        else:
            print("No se detectaron interacciones.")
