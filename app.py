from flask import Flask, render_template, redirect, request, Response, session
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='custodiadelosmedicamentos'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

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

#FUNCION DE LOGIN
@app.route('/acceso-login', methods=["GET", "POST"])
def login():
    if request.method == "POST" and "txtUsuario" in request.form and "txtContrasena":
        _usuario = request.form["txtUsuario"]
        _contrasena = request.form["txtContrasena"]

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE Username = %s AND Contrasena =%s', (_usuario,_contrasena))
        account=cur.fetchone()

        if account:
            session['logueado'] = True
            session['Id_Usuario'] = account["Id_Usuario"]

            return render_template("admin.html")
        
        else:
            return render_template('login.html')

if __name__ == '__main__':
    app.secret_key="custodia"
    app.run(debug=True)