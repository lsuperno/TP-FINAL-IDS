from flask import Blueprint, jsonify, request
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

#cambiar acorde al uso
def get_conection(): 
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="6002682",
        database='AlacenApp'
    )

usuarios_bp = Blueprint("usuarios", __name__)

"""

"""
@usuarios_bp.route('/registrar', methods=['POST'])
def crear_usuario():
    #Obtengo info de usuario
    info = request.json
    nombre = info.get("nombre")
    email = info.get("email")
    contrasena = info.get("contrasena")
    confirmar_contrasena = info.get("confirmar_contrasena")
    presupuesto = info.get("presupuesto")

    #Verificaciones basicas del form
    if not nombre or not email or not contrasena:
        return jsonify({"message": "Complete los campos obligatorios"}), 400
    if contrasena != confirmar_contrasena:
        return jsonify({"message": "Las contrasenas no coinciden"}), 400
    
    #Conecto a base
    conn = get_conection()
    cursor = conn.cursor(dictionary=True)

    #Verifico si ya existe una cuenta con ese mail
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    existe_usario = cursor.fetchone()
    if existe_usario:
        cursor.close()
        conn.close()
        return jsonify({"message": f"Ya existe un usario asociado al email: {email}"}), 409
    
    #Guardo el usuario
    contrasena = generate_password_hash(contrasena)
    cursor.execute("""
                    INSERT INTO usuarios (nombre, email, contrasena, presupuesto)
                    VALUES (%s, %s, %s, %s)
                    """, (nombre, email, contrasena, presupuesto))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": f'Cuenta registrada correctamente {nombre}'}), 201


"""

"""
@usuarios_bp.route('/iniciar', methods=['POST'])
def obtener_usuario():
    #obtengo informacion del usuario
    info = request.json
    email = info.get("email")
    contrasena = info.get("contrasena")
    if not email or not contrasena:
        return jsonify({"message": "Complete los campos obligatorios"}), 400
    
    #Conecto a base
    conn = get_conection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, contrasena FROM usuarios WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    #Verificaciones
    if not user:
        return jsonify({"message": f"No existe un usario asociado al email: {email}"}), 404
    if not check_password_hash(user['contrasena'], contrasena):
        return jsonify({"message": f"Contrasena incorrecta"}), 401
    
    #Si pasa las verificaciones devuelve el id de usuario
    else:
        return jsonify({"user_id": user["id"]}), 200

