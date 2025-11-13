# 🧺 AlacenApp (Flask + MySQL)
Aplicación web para gestionar tu alacena personal o compartida, escanear productos, controlar presupuesto mensual y generar recetas con los alimentos disponibles.
Desarrollada con con backend en Flask, base de datos MySQL y frontend en HTML, CSS y JavaScript.

## 🧱 Requerimientos funcionales

### 🔹 Backend (Flask)

#### ⚙️ Configurar el entorno del proyecto

- Crear entorno virtual (python -m venv .venv).
- Instalar dependencias
- Configurar conexión a la base de datos en config.py.
- Crear script init.sh con instalación de dependencias (pip install -r requirements.txt).

#### 🗃️ Diseñar el modelo de base de datos

- Base de datos: alacenapp_db
- Tablas mínimas requeridas:
  ##### users
   - id (INT, PK, autoincremental)
   - name (VARCHAR)
   - email (VARCHAR, único)
   - password_hash (VARCHAR)
   - tipo_cuenta (ENUM: "solo", "compartida")
   - presupuesto_mensual (FLOAT)
  ##### products
   - id (INT, PK)
   - name (VARCHAR)
   - barcode (VARCHAR)
   - category (VARCHAR)
   - precio_referencia (FLOAT)
  ##### pantry_items
   - id (INT, PK)
   - user_id (FK users.id)
   - product_id (FK products.id)
   - quantity (INT)
   - expiry_date (DATE)
   - (Opcional): shared_groups, shared_group_users para cuentas compartidas.
 ##### FAMILY_GROUP
   - ID_FAMILY
   - ID USER

#### 🌐 Implementar rutas API REST

- Formato de intercambio: JSON
  
   ##### Autenticación y usuarios
  - POST /api/auth/register → registrar usuario (solo/compartida)
  - POST /api/auth/login → iniciar sesión
  - GET /api/user/me → obtener datos del usuario autenticado

   ##### Productos / Alacena
  - GET /api/products → obtener todos los productos
  - POST /api/products → agregar nuevo producto
  - PUT /api/products/<id> → editar producto
  - DELETE /api/products/<id> → eliminar producto
  - GET /api/pantry → listar productos del usuario
  - POST /api/pantry → agregar producto a la alacena
  - POST /api/scan → buscar producto por código de barras (API OpenFoodFacts)

   ##### Estadísticas
  - GET /api/stats/budget → resumen de gasto mensual
  - GET /api/stats/pantry → composición de la alacena por categoría

#### ✅ Validaciones y manejo de errores

- Validar campos obligatorios antes de insertar/actualizar.
- Manejar errores HTTP 404 (Not Found), 500 (Internal Server Error).
- Responder mensajes JSON claros ({"error": "Producto no encontrado"}).

#### 🧪 Pruebas básicas del backend
- Testear endpoints principales con Postman o pytest/unittest.
- Verificar creación, lectura, modificación y eliminación de registros.
- Validar conexión con la base de datos.

### 🔹 Frontend (Flask + HTML, CSS, JavaScript)

#### 🎨 Diseño de interfaz

- Usar templates Jinja2 (index.html, login.html, register.html, pantry.html, etc.).
- Pantalla inicial con botones: Ingresar y Registrarte --> “Solo para mí” o “Para varias personas”
- Página principal: “Hola, {nombre}. En tu alacena hay X productos.” Botón destacado: Mi Alacena.

#### 🧩 Funcionalidades principales
- Listado de productos: muestra todos los ítems almacenados.
- Filtros: por categoría.
- Lista del supermercado: productos con stock en cero.
- Gráficos estadísticos: Barra ( gasto mensual) y Torta (proporción de categorías)
- Recetas sugeridas: conexión con API TheMealDB.
- Escanear productos: integración con OpenFoodFacts API (nombre + código de barras). Si no existe → formulario manual para agregarlo localmente.

#### 🖥️ Integración con Backend Flask

- Uso de `@app.route` para definir las rutas del sitio.
- Envío y recepción de datos entre frontend y backend mediante formularios HTML o llamadas AJAX (fetch).
- Respuestas del backend en formato JSON para los datos dinámicos.
- Actualización del contenido en la página sin recargar (fetch + DOM).

#### 💅 Estilo y usabilidad

- Diseño moderno y responsivo (Bootstrap o Tailwind).
- Notificaciones de éxito o error (por ejemplo, al agregar producto o escanear).
- Experiencia fluida en escritorio y móvil.

#### 📁 Gestión de archivos estáticos

- Organizar los recursos en carpetas /static/css, /static/js, /static/img.
- Configurar Flask para servir estos archivos correctamente.

### 🔹 Base de datos (MySQL)

#### 🧩 Configuración de esquema
- Crear base de datos alacenapp_db.
- Ejecutar script para definir las tablas.
- Definir usuario, contraseña y privilegios.

#### 🔄 Persistencia y migraciones

- Usar Flask-SQLAlchemy o Flask-Migrate para mantener el esquema actualizado.

### 🔹 Extras / Mejoras opcionales

- 🔐 Autenticación con cuenta de Google (OAuth 2.0).
- 📱 Interfaz mobile usando Kivy UI (versión local).
- 🧾 Documentación de API (Swagger o Postman).
- 🐳 Docker para levantar el entorno completo (Flask + MySQL).
- 📊 Dashboard visual con gráficos más detallados (Chart.js / Recharts).

### 🔹 Despliegue
 - Hosting del proyecto en PythonAnywhere


## ✅ Objetivo final

Tener una aplicación funcional donde el usuario pueda:

- 👤 Registrarse o iniciar sesión (individual o compartido).
- 📦 Ver y gestionar los productos de su alacena.
- 🧾 Visualizar estadísticas de consumo y presupuesto.
- 🛒 Generar automáticamente su lista del supermercado.
- 📷 Escanear productos mediante código de barras.
- 🍳 Obtener recetas con los alimentos disponibles.
- 💾 Guardar y recuperar todos los datos desde una base MySQL.
- 🌐 Acceder a través de una interfaz web moderna y responsiva.

### Integrantes de Equipo 007:

- María Florencia Guardo 114421
- Lourdes Camasta 114423
- Luz Acuña  110210
- Alan Cristobo 109915
- Lautaro Superno 114524


