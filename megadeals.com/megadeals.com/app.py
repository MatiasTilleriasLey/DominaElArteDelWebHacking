from flask import Flask, render_template, flash, redirect, request
import mysql.connector
app = Flask(__name__)
app.secret_key="DominaElArteDelWebHacking"

@app.route('/')
def index():
    db_config = {
    'host': 'megadeals_database',       # Cambia esto si estás usando Docker o un servidor remoto
    'port': 3306,              # Puerto por defecto de MySQL
    'user': 'root',            # Usuario de MySQL
    'password': 'root',        # Contraseña del usuario
    'database': 'megadeals'    # Nombre de la base de datos
}
    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # Consulta para obtener los productos
    cursor.execute(""" 
        SELECT name, price, photo_url 
        FROM products 
        ORDER BY id DESC 
        LIMIT 3
    """)
    products = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Pasar los productos al template
    return render_template('index.html', products=products, is_index=True)

@app.route('/register')
def registerSite():
    return render_template("register.html", is_index=False)

@app.route('/register', methods=['POST'])
def register():
    db_config = {
    'host': 'megadeals_database',       # Cambia esto si estás usando Docker o un servidor remoto
    'port': 3306,              # Puerto por defecto de MySQL
    'user': 'root',            # Usuario de MySQL
    'password': 'root',        # Contraseña del usuario
    'database': 'megadeals'    # Nombre de la base de datos
}
        # Obtener datos del formulario
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')  # Deberías encriptarla para mayor seguridad
    address = request.form.get('address')
    phone = request.form.get('phone')

    # Validación básica
    if not name or not email or not password or not address or not phone:
        flash('Por favor, completa todos los campos.', 'error')
        return redirect('/register')

    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Comprobar si el usuario ya está registrado
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                flash('El correo electrónico ya está registrado. Por favor, inicia sesión.', 'error')
                return redirect('/register')

            # Insertar datos en la base de datos
            query = """
            INSERT INTO users (name, email, password, address, phone) 
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, email, password, address, phone))
            connection.commit()

            flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
            return redirect('/login')
    except:
        flash('Hubo un problema al procesar tu solicitud. Inténtalo de nuevo más tarde.', 'error')
        return redirect('/register')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)