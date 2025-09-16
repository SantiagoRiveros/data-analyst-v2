-- Esto es para crear la base de datos
CREATE DATABASE ambox;
-- Esta linea de arriba, se ejecuta una sola vez, cuando creas la DB

-- Con esta linea, "Seleccionamos" la base de datos a usar
USE ambox;

-- Vamos a crear nuestra primera tabla
CREATE TABLE productos (
	id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL,
    categoria TEXT
);

-- Ahora vamos a insertar datos en nuestra tabla
INSERT INTO productos (id, nombre, precio, categoria) 
VALUES
	(1, 'Camiseta', 25.99, 'Ropa'),
    (2, 'Zapatillas', 59.99, 'Calzado'),
    (3, 'Pantalon', 35.00, 'Ropa'),
    (4, 'Gorra', 15.50, 'Accesorios');
    
    
-- Con esto hacemos un GET de la tabla
SELECT * FROM productos;
    
    
-- Seleccionar columnas especificas
SELECT nombre, precio FROM productos;

-- WHERE
SELECT * FROM productos WHERE categoria = 'Ropa';

SELECT * FROM productos WHERE precio > 30;

-- ESTE EJEMPLO USA REGEX, NO SE PREOCUPEN EN ENTENDER REGEX AHORA.
SELECT * FROM productos WHERE nombre LIKE 'Z%';

-- Ejercicio 1: Crear una tabla de clientes
CREATE TABLE clientes (
	id INTEGER PRIMARY KEY,
    nombre TEXT,
    email TEXT
    );
    
-- Ejercicio 2: Insertar clientes
INSERT INTO clientes(id, nombre, email)
VALUES
	(1, 'Ana', 'ana@hotmail.com'),
    (2, "Jose", 'jose@yahoo.com'),
    (3, 'Carla', 'carla@gmail.com');
    
SELECT * FROM clientes;

-- Ejercicio 3: Realizar una cnsulta
SELECT * FROM clientes WHERE nombre = 'Jose';


-- Creamos una tabla nueva ventas, con 2 FK, uno de clientes, otro de producto
CREATE TABLE ventas (
	id INTEGER PRIMARY KEY,
    producto_id INTEGER,
    cliente_id INTEGER,
    cantidad INTEGER,
    total DECIMAL (10, 2),
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Insertar al menos 3 registros.

-- Hacer un SELECT que muestre todas las ventas con total mayor a 50.

-- Mostrar solo los nombres de productos cuyo precio sea menor a 40.
