class Usuario:
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str):
        self.ID = ID
        self.Nombre = Nombre
        self.Documento = Documento
        self.Rol = Rol
        self.Usuario = Usuario
        self.Contraseña = Contraseña
        self.TarjetaProfesional = TarjetaProfesional

    def loguear(self):
        pass
