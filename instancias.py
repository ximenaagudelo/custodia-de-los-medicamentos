from models.medico import Medico
from models.farmaceutico import Farmaceutico
from models.enfermera import Enfermera
from models.paciente import Paciente

# Crear instancias
medico = Medico(1, "Dr. Juan", "123456", "Medico", "juandoc", "password", "12345678")
farmaceutico = Farmaceutico(2, "Carlos López", "789012", "Farmaceutico", "carlosf", "pass123", "87654321")
enfermera = Enfermera(3, "Maria Perez", "345678", "Enfermera", "mariap", "pass456", "23456789")
paciente = Paciente(4, "Ana Gómez", "456789", "Paciente", "anagomez", "pass123", "", "Historia médica", "Hipertensión", "Losartán")

# Llamar métodos
medico.crear_paciente()
paciente.consultar_historial()


print(medico)
print(paciente)