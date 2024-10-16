from models.usuario import Usuario
from flask_mysqldb import MySQL

class Medico(Usuario):
    def __init__(self, ID: int, Nombre: str, Documento: str, Rol: str, Usuario: str, Contraseña: str, TarjetaProfesional: str, db: MySQL):
        super().__init__(ID, Nombre, Documento, Rol, Usuario, Contraseña, TarjetaProfesional)
        self.db = db  # Aquí pasamos la conexión a la base de datos

    def crear_paciente(self, nombre: str, documento: str, historia_medica: str, enfermedades: str, medicamentos_actuales: str):
        """
        Este método inserta un nuevo paciente en la base de datos.
        :param nombre: Nombre del paciente
        :param documento: Documento del paciente
        :param historia_medica: Historia médica del paciente
        :param enfermedades: Enfermedades del paciente
        :param medicamentos_actuales: Medicamentos actuales del paciente
        """
        try:
            cur = self.db.connection.cursor()
            cur.execute('''
                INSERT INTO paciente (Nombre, Documento, Historia_Medica, Enfermedades, Medicamentos_Actuales)
                VALUES (%s, %s, %s, %s, %s)
            ''', (nombre, documento, historia_medica, enfermedades, medicamentos_actuales))
            self.db.connection.commit()
            cur.close()
            print("Paciente creado exitosamente")
        except Exception as e:
            print(f"Error al crear el paciente: {e}")

    def asignar_prescripcion(self):
        # Método para asignar prescripción a un paciente (implementarlo según tus necesidades)
        pass

    def asignar_diagnostico(self) -> str:
        # Método para asignar diagnóstico a un paciente (implementarlo según tus necesidades)
        return ""
