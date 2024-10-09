from models.usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str):
        super().__init__(ID, Nombre, Documento, Rol, Usuario, Contraseña, TarjetaProfesional)

    def administrar_dosis(self):
        pass

    def consultar_guia_clinica(self):
        pass

    def consultar_inventario(self):
        pass
