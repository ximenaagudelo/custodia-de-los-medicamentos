from flask import Flask, render_template, redirect, request, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'custodiadelosmedicamentos'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Página principal
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/login')
def iniciosesion():
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# FUNCION DE LOGIN
@app.route('/acceso-login', methods=["GET", "POST"])
def login():
    if request.method == "POST" and "txtUsuario" in request.form and "txtContrasena" in request.form:
        _usuario = request.form["txtUsuario"]
        _contrasena = request.form["txtContrasena"]

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE Username = %s AND Contrasena = %s', (_usuario, _contrasena))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['Id_Usuario'] = account["Id_Usuario"]
            session['Rol'] = account["Id_Rol"]

            if account['Id_Rol'] == 2:  # Médico
                return redirect('/medico')
            elif account['Id_Rol'] == 3:  # Farmacéutico
                return redirect('/farmaceutico')
            else:
                return render_template("admin.html")
        else:
            return render_template('login.html')

# Ruta para médicos
@app.route('/medico')
def medico():
    if 'logueado' in session and session['Rol'] == 2:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM paciente')
        pacientes = cur.fetchall()
        cur.close()
        return render_template('medico.html', pacientes=pacientes)
    else:
        return redirect('/login')

# Ruta para crear un nuevo paciente
@app.route('/crear-paciente', methods=["GET", "POST"])
def crear_paciente():
    if 'logueado' in session and session['Rol'] == 2:
        if request.method == "POST":
            nombre = request.form["nombre"]
            documento = request.form["documento"]
            fecha_nacimiento = request.form["fechaNacimiento"]
            historia_medica = request.form.get("historiaMedica", "")
            enfermedades = request.form.get("enfermedades", "")
            medicamentos_actuales = request.form.get("medicamentosActuales", "")

            cur = mysql.connection.cursor()
            cur.execute('''INSERT INTO paciente (Nombre, Documento, Fecha_Nacimiento, Historia_Medica, Enfermedades, Medicamentos_Actuales) VALUES (%s, %s, %s, %s, %s, %s)''',
                        (nombre, documento, fecha_nacimiento, historia_medica, enfermedades, medicamentos_actuales))
            mysql.connection.commit()
            cur.close()

            return redirect('/medico')
        return render_template('crear_paciente.html')
    else:
        return redirect('/login')

# Ruta para editar un paciente
@app.route('/editar-paciente/<int:id>', methods=["GET", "POST"])
def editar_paciente(id):
    if 'logueado' in session and session['Rol'] == 2:
        cur = mysql.connection.cursor()
        if request.method == "POST":
            nombre = request.form["nombre"]
            documento = request.form["documento"]
            fecha_nacimiento = request.form["fechaNacimiento"]
            historia_medica = request.form["historiaMedica"]
            enfermedades = request.form["enfermedades"]
            medicamentos_actuales = request.form["medicamentosActuales"]

            cur.execute('''
                UPDATE paciente
                SET Nombre = %s, Documento = %s, Fecha_Nacimiento = %s, Historia_Medica = %s, Enfermedades = %s, Medicamentos_Actuales = %s
                WHERE Id_Paciente = %s
            ''', (nombre, documento, fecha_nacimiento, historia_medica, enfermedades, medicamentos_actuales, id))
            mysql.connection.commit()
            cur.close()
            return redirect('/medico')
        else:
            cur.execute('SELECT * FROM paciente WHERE Id_Paciente = %s', (id,))
            paciente = cur.fetchone()
            cur.close()
            return render_template('editar_paciente.html', paciente=paciente)
    else:
        return redirect('/login')

# Ruta para ver detalles de un paciente
@app.route('/ver-paciente/<int:id>')
def ver_paciente(id):
    if 'logueado' in session and session['Rol'] == 2:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM paciente WHERE Id_Paciente = %s', (id,))
        paciente = cur.fetchone()
        cur.close()
        if paciente:
            return render_template('ver_paciente.html', paciente=paciente)
        else:
            return "Paciente no encontrado", 404
    else:
        return redirect('/login')

# Ruta para eliminar un paciente
@app.route('/eliminar-paciente/<int:id>', methods=["POST"])  
def eliminar_paciente(id):
    if 'logueado' in session and session['Rol'] == 2:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM paciente WHERE Id_Paciente = %s', (id,))
        mysql.connection.commit()
        cur.close()
        return redirect('/medico')
    else:
        return redirect('/login')

# Rutas para farmacéuticos
@app.route('/farmaceutico')
def farmaceutico():
    if 'logueado' in session and session['Rol'] == 3:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM medicamento')
        medicamentos = cur.fetchall()
        cur.close()
        return render_template('farmaceutico.html', medicamentos=medicamentos)
    else:
        return redirect('/login')

# Ruta para crear un nuevo medicamento
@app.route('/crear-medicamento', methods=["GET", "POST"])
def crear_medicamento():
    if 'logueado' in session and session['Rol'] == 3:
        if request.method == "POST":
            nombre = request.form["nombre"]
            laboratorio = request.form["laboratorio"]
            fecha_vencimiento = request.form["fecha_vencimiento"]
            tipo = request.form["tipo"]

            cur = mysql.connection.cursor()
            cur.execute('''
                INSERT INTO medicamento (Nombre, Laboratorio, Fecha_vencimiento, Tipo)
                VALUES (%s, %s, %s, %s)
            ''', (nombre, laboratorio, fecha_vencimiento, tipo))
            mysql.connection.commit()
            cur.close()

            return redirect('/farmaceutico')
        return render_template('crear_medicamento.html')
    else:
        return redirect('/login')

# Ruta para ver detalles de un medicamento
@app.route('/ver-medicamento/<int:codigo>')
def ver_medicamento(codigo):
    if 'logueado' in session and session['Rol'] == 3:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM medicamento WHERE Codigo = %s', (codigo,))
        medicamento = cur.fetchone()
        cur.close()
        if medicamento:
            return render_template('ver_medicamento.html', medicamento=medicamento)
        else:
            return "Medicamento no encontrado", 404
    else:
        return redirect('/login')

# Ruta para editar un medicamento
@app.route('/editar-medicamento/<int:codigo>', methods=["GET", "POST"])
def editar_medicamento(codigo):
    if 'logueado' in session and session['Rol'] == 3:
        cur = mysql.connection.cursor()
        if request.method == "POST":
            nombre = request.form["nombre"]
            laboratorio = request.form["laboratorio"]
            fecha_vencimiento = request.form["fecha_vencimiento"]
            tipo = request.form["tipo"]

            cur.execute('''
                UPDATE medicamento
                SET Nombre = %s, Laboratorio = %s, Fecha_vencimiento = %s, Tipo = %s
                WHERE Codigo = %s
            ''', (nombre, laboratorio, fecha_vencimiento, tipo, codigo))
            mysql.connection.commit()
            cur.close()
            return redirect('/farmaceutico')
        else:
            cur.execute('SELECT * FROM medicamento WHERE Codigo = %s', (codigo,))
            medicamento = cur.fetchone()
            cur.close()
            return render_template('editar_medicamento.html', medicamento=medicamento)
    else:
        return redirect('/login')

# Ruta para eliminar un medicamento
@app.route('/eliminar-medicamento/<int:codigo>', methods=["POST"])
def eliminar_medicamento(codigo):
    if 'logueado' in session and session['Rol'] == 3:
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM medicamento WHERE Codigo = %s', (codigo,))
        mysql.connection.commit()
        cur.close()
        return redirect('/farmaceutico')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.secret_key = "custodia"
    app.run(debug=True)
