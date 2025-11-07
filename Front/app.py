from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        confirmar_contrasena = request.form.get('confirmar_contrasena')
        presupuesto = request.form.get('presupuesto')
        periodo = request.form.get('periodo')
        tipo_cuenta = request.form.get('tipo_cuenta')

        # Validación simple
        if not nombre or not email or not contrasena:
            flash("Todos los campos obligatorios deben completarse", "error")
            return redirect(url_for('login'))

        if contrasena != confirmar_contrasena:
            flash("Las contraseñas no coinciden", "error")
            return redirect(url_for('register'))

        # En el futuro: guardar datos en la base de datos
        # guardar_usuario(nombre, email, contrasena, presupuesto, periodo, tipo_cuenta)

        flash("Cuenta creada con éxito. Ahora podés ingresar.", "success")
        return redirect(url_for('login'))

    # Si es GET, solo mostramos el formulario
    return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Capturar los datos del formulario
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        flash(f"Inicio de sesión simulado: {email}", "success")
        return redirect(url_for('dashboard'))  
    
    # Si es GET, mostrar el formulario
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/')
def main():
    return render_template('index.html')


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
