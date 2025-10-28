from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('signin.html')

@app.route('/registrar_cuenta')
def registrar_cuenta():
    return render_template('signup.html')

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

@app.route('/ingresar')
def ingresar():
    return render_template('ingresar.html')

@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('crear_cuenta.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run('localhost', port=8080, debug = True)