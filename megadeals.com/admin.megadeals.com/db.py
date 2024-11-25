import mysql.connector

# Configuración de la conexión
db_config = {
    'host': 'megadeals_database',       # Cambia esto si estás usando Docker o un servidor remoto
    'port': 3306,              # Puerto por defecto de MySQL
    'user': 'root',            # Usuario de MySQL
    'password': 'root',        # Contraseña del usuario
    'database': 'megadeals',
    'charset': 'utf8mb4'    # Nombre de la base de datos
}

def authenticate_user(email, password):
    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    try:

        # Consulta SELECT con condición WHERE
        query = f"""
        SELECT id, name, email, business_role, application_role, profile_photo_url
        FROM employee_users
        WHERE email = '{email}' AND password = '{password}';
        """
        print(f"Consulta ejecutada: {query}")  # Para fines de depuración
        cursor.execute(query)

        # Recuperar resultado
        user = cursor.fetchone()
        if user:
            return user
        else:
            return False
    except mysql.connector.Error as err:
        pass
    finally:
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_products_from_db():
    # Lista donde se almacenarán los productos
    products = []

    try:
        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL para obtener los productos
        query = """
        SELECT id, name, description, price, stock, photo_url
        FROM products
        ORDER BY id ASC;
        """
        cursor.execute(query)

        # Recuperar todos los resultados
        products = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")

    finally:
        # Cierra el cursor y la conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return products
def update_product_in_db(product_id, name, description, price, stock):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Consulta para actualizar el producto
        query = """
        UPDATE products
        SET name = %s, description = %s, price = %s, stock = %s
        WHERE id = %s;
        """
        cursor.execute(query, (name, description, price, stock, product_id))
        conn.commit()
        return True  # Indica que la actualización fue exitosa

    except mysql.connector.Error as err:
        print(f"Error al actualizar el producto: {err}")
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

