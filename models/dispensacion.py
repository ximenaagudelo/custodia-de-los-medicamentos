from models.prescripcion import Prescripcion

class Dispensacion:
    def __init__(self, ID: int, FechaDispensacion: str, Prescripcion: Prescripcion):
        self.ID = ID
        self.FechaDispensacion = FechaDispensacion
        self.Prescripcion = Prescripcion

    def dispensar_medicamento(self):
        # Lógica para dispensar el medicamento basado en la prescripción.
        print(f"Dispensando medicamento(s) para la prescripción ID: {self.Prescripcion.ID} en la fecha: {self.FechaDispensacion}")
        # Aquí podrías agregar más lógica para actualizar inventarios, etc.

    def validar_inventario(self):
        # Lógica para validar que hay suficiente medicamento disponible en el inventario.
        pass
