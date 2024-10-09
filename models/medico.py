from models.usuario import Usuario

class Medico(Usuario):
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str):
        super().__init__(ID, Nombre, Documento, Rol, Usuario, Contraseña, TarjetaProfesional)

    def crear_paciente(self):
        pass

    def asignar_prescripcion(self):
        pass

    def asignar_diagnostico(self) -> str:
        return ""
