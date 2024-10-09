from models.usuario import Usuario

class Farmaceutico(Usuario):
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str):
        super().__init__(ID, Nombre, Documento, Rol, Usuario, Contraseña, TarjetaProfesional)

    def registrar_medicamento(self):
        pass

    def modificar_medicamento(self):
        pass

    def dispensar_medicamento(self):
        pass

    def consultar_guia_clinica(self):
        pass
