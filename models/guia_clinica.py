class GuiaClinica:
    def __init__(self, ID: int, Documento: str, Recomendaciones: str, FechaActualizacion: str):
        self.ID = ID
        self.Documento = Documento
        self.Recomendaciones = Recomendaciones
        self.FechaActualizacion = FechaActualizacion

    def consultar_guia(self):
        # Lógica para consultar la guía clínica
        print(f"Consultando guía clínica ID: {self.ID}")
        print(f"Documento: {self.Documento}")
        print(f"Recomendaciones: {self.Recomendaciones}")
        print(f"Fecha de actualización: {self.FechaActualizacion}")

    def actualizar_guia(self, nuevo_documento: str, nuevas_recomendaciones: str):
        # Lógica para actualizar la guía clínica
        self.Documento = nuevo_documento
        self.Recomendaciones = nuevas_recomendaciones
        # Actualiza la fecha de actualización a la fecha actual (simplificado)
        from datetime import datetime
        self.FechaActualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Guía clínica ID: {self.ID} actualizada.")
