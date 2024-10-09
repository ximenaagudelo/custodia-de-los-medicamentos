from models.usuario import Usuario

class Paciente(Usuario):
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str, HistoriaMedica: str, Enfermedades: str, MedicamentosActuales: str):
        super().__init__(ID, Nombre, Documento, Rol, Usuario, Contraseña, TarjetaProfesional)
        self.HistoriaMedica = HistoriaMedica
        self.Enfermedades = Enfermedades
        self.MedicamentosActuales = MedicamentosActuales

    def registrar_paciente(self):
        pass

    def consultar_historial(self):
        pass
