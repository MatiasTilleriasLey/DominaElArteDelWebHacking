from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from db import authenticate_user, get_products_from_db, update_product_in_db
from functools import wraps

app = Flask(__name__)
app.secret_key="DominaElArteDelWebHacking"
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "application_role" not in session or session["application_role"] != "Admin":
            return redirect(url_for("index"))  # Redirige al índice si no está autenticado o no es admin
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    
    email = request.form.get("email")
    password = request.form.get("password")
    auth = authenticate_user(email, password)
    session["application_role"] = auth["application_role"]
    session["email"] = auth["email"]
    session["id"] = auth["id"]
    session["name"] = auth["name"]
    session["business_role"] = auth["business_role"]
    session["profile_photo_url"] = auth["profile_photo_url"]
    if auth == False:
        return redirect(url_for("index"))
    if session["application_role"] == "Admin":
        return redirect(url_for("adminPortal"))
    if session["application_role"] == "Employee":
        return redirect(url_for("employeePortal"))
    
@app.route('/admin', methods=['GET'])
@admin_required
def adminPortal():
    return render_template("admin.html", 
                        profile_url = session["profile_photo_url"],
                        business_role = session["business_role"],
                        name = session["name"]
                        )

@app.route('/admin/products', methods=['GET'])
def admin_products():
    return render_template("admin_products.html", 
                        products=get_products_from_db(),
                        profile_url = session["profile_photo_url"],
                        business_role = session["business_role"],
                        name = session["name"])

@app.route('/update-product/<int:product_id>', methods=['POST'])
@admin_required
def update_product(product_id):
    # Obtener los datos enviados desde el cliente
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')

    # Llamar a la función de actualización en db.py
    success = update_product_in_db(product_id, name, description, price, stock)

    if success:
        return jsonify({"message": "Producto actualizado exitosamente"}), 200
    else:
        return jsonify({"message": "Error al actualizar el producto"}), 500
@app.route('/test')
def test():
    # Datos de prueba
    product_id = 1
    name = "Laptop Actualizada"
    description = "Laptop con mejores especificaciones para gaming."
    price = 1250000.00
    stock = 8

    return update_product_in_db(product_id, name, description, price, stock)

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("index"))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
