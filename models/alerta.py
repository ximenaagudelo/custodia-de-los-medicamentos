from datetime import datetime

class Alerta:
    def __init__(self, ID: int, TipoAlerta: str, Descripcion: str):
        self.ID = ID
        self.TipoAlerta = TipoAlerta
        self.Descripcion = Descripcion
        self.FechaHora = datetime.now()  # Se establece la fecha y hora actual al crear la alerta

    def enviar_alerta(self):
        # Lógica para enviar la alerta
        print(f"Alerta ID: {self.ID}")
        print(f"Tipo de Alerta: {self.TipoAlerta}")
        print(f"Descripción: {self.Descripcion}")
        print(f"Fecha y Hora: {self.FechaHora.strftime('%Y-%m-%d %H:%M:%S')}")
        # Aquí podrías agregar lógica para enviar la alerta a un sistema externo o a los usuarios relevantes
