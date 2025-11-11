from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = 'IDS'
app.permanent_session_lifetime = timedelta(days=30)


API_BASE = "http://localhost:5000"


def register_user(nombre, email, contrasena, confirmar_contrasena, presupuesto):
    if not presupuesto:
        presupuesto = 0
    response = requests.post(
        f"{API_BASE}/usuarios/registrar",
        json={"nombre": nombre,
              "email": email,
              "contrasena": contrasena,
              "confirmar_contrasena": confirmar_contrasena,
              "presupuesto": presupuesto},
    )
    return response.json(), response.status_code


def log_user(email, contrasena):
    response = requests.post(
        f"{API_BASE}/usuarios/iniciar",
        json={"email":email,
              "contrasena":contrasena},
    )
    return response.json(), response.status_code


# <---RUTAS FLASK--->


@app.route('/')
def main():
    if "user_id" in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if "user_id" in session:
        return redirect(url_for('dashboard'))
    else:
        if request.method == 'POST':
            
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            contrasena = request.form.get('contrasena')
            confirmar_contrasena = request.form.get('confirmar_contrasena')
            presupuesto = request.form.get('presupuesto')
            periodo = request.form.get('periodo')
            tipo_cuenta = request.form.get('tipo_cuenta')

            respuesta, codigo = register_user(nombre, email, contrasena, confirmar_contrasena, presupuesto)
            flash(respuesta["message"], codigo)

        # Si es GET, solo mostramos el formulario
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "user_id" in session:
        return redirect(url_for('dashboard'))
    else:
        if request.method == 'POST':
            # Capturar los datos del formulario
            email = request.form.get('email')
            contrasena = request.form.get('contrasena')

            respuesta, codigo = log_user(email, contrasena)
            if codigo == 200:
                session["user_id"] = respuesta["user_id"]
                return redirect(url_for('dashboard'))  
            else:
                flash(respuesta["message"])
        # Si es GET, mostrar el formulario
        return render_template('login.html')


@app.route('/logout', methods=["POST"])
def logout():
    session.clear() 
    return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    if "user_id" in session:
        return render_template('dashboard.html')
    return redirect(url_for('register'))


@app.route('/cambiar_contraseña')
def cambiar_contraseña():
    return render_template('reset-password.html')

@app.route('/precios')
def precios():
    return render_template('pricing.html')

@app.route('/mail')
def mail():
    return render_template('mail-success.html')

@app.route('/contacto')
def contacto():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog-single.html')

@app.route('/blog_grilla')
def blog_grilla():
    return render_template('blog-grid.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
