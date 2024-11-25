-- Base de datos
CREATE DATABASE IF NOT EXISTS megadeals;
USE megadeals;

-- Tabla: Products
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL, -- Precio en CLP
    stock INT NOT NULL,
    photo_url VARCHAR(255) -- Ruta de la foto del producto
);

INSERT INTO products (name, description, price, stock, photo_url) VALUES
('Laptop', 'Laptop de alto rendimiento para trabajo y gaming.', 1200000.00, 10, '/static/images/products/laptop.webp'),
('Smartphone', 'Smartphone de última generación con cámara de alta resolución.', 800000.00, 20, '/static/images/products/smartphone.webp'),
('Headphones', 'Audífonos inalámbricos con cancelación de ruido activa.', 150000.00, 50, '/static/images/products/headphone.webp');

-- Tabla: Employee Users
CREATE TABLE employee_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    business_role VARCHAR(50) NOT NULL, -- Rol empresarial
    application_role VARCHAR(50) NOT NULL, -- Rol en la aplicación
    profile_photo_url VARCHAR(255) -- Ruta de la foto de perfil
);

INSERT INTO employee_users (email, password, name, business_role, application_role, profile_photo_url) VALUES
('sofia.martinez@megadeals.com', 'password123', 'Sofia Martinez', 'Gerente General', 'Admin', '/static/images/profiles/sofia_martinez.webp'),
('carlos.gomez@megadeals.com', 'password123', 'Carlos Gómez', 'Encargado de Logística', 'Employee', '/static/images/profiles/carlos_gomez.webp'),
('ana.lopez@megadeals.com', 'password123', 'Ana Lopez', 'Especialista en Atención al Cliente', 'Employee', '/static/images/profiles/ana_lopez.webp');

-- Tabla: Customer Users
CREATE TABLE customer_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20)
);

INSERT INTO customer_users (email, password, name, address, phone) VALUES
('customer1@example.com', 'password123', 'Alice Brown', 'Calle Elm 123', '555-1234'),
('customer2@example.com', 'password123', 'Bob Green', 'Avenida Oak 456', '555-5678');
