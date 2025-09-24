-- JOINS

-- INNER JOIN -> Devuelve solo coincidencias entre ambas tablas
-- LEFT JOIN -> Devuelve todas las filas de la tabla izquierda, y las coincidencias de la derecha
-- RIGHT JOIN -> Devuelve todas las filas de la tabla derecha, y las coincidencias de la izquierda
-- FULL OUTER JOIN -> Devuelve todas las filas, tenga o no coincidencia

-- Sintaxis Basica:
-- SELECT tabla1.columna, tabla2.columna
-- FROM tabla1
-- JOIN tabla2 ON tabla1.columna_clave = tabla2.columna_clave

CREATE DATABASE ambox_join;

USE ambox_join;

CREATE TABLE productos (
  producto_id INT PRIMARY KEY,
  nombre VARCHAR(50),
  precio DECIMAL(10,2)
);

CREATE TABLE ventas (
  venta_id INT PRIMARY KEY,
  producto_id INT,
  cantidad INT,
  fecha DATE,
  FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

INSERT INTO productos VALUES
(1, 'Notebook', 1000.00),
(2, 'Monitor', 300.00),
(3, 'Mouse', 20.00),
(4, 'Teclado', 50.00);

INSERT INTO ventas VALUES
(1, 1, 2, '2023-05-01'),
(2, 2, 1, '2023-05-03'),
(3, 4, 5, '2023-05-05');


-- Mostrar nombre del producto, precio y cantidad vendida.
SELECT p.nombre, p.precio, v.cantidad
FROM productos p
JOIN ventas v ON p.producto_id = v.producto_id;

-- Mostrar todos los productos, aunque no se hayan vendido.
SELECT p.nombre, v.cantidad
FROM productos p
LEFT JOIN ventas v ON p.producto_id = v.producto_id;

-- Mostrar solo productos que no tienen ventas.
SELECT p.nombre
FROM productos p
LEFT JOIN ventas v ON p.producto_id = v.producto_id
WHERE v.venta_id IS NULL;

-- Calcular el total facturado por cada producto.
SELECT p.nombre, SUM(p.precio * v.cantidad) AS total
FROM productos p
JOIN ventas v ON p.producto_id = v.producto_id
GROUP BY p.nombre;

-- Subconsultas

SELECT nombre, precio
FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);

-- Mostrar ventas del producto más vendido.
SELECT v.producto_id, p.nombre, v.cantidad, SUM(p.precio * v.cantidad) AS total
FROM ventas v
JOIN productos p ON p.producto_id = v.producto_id
WHERE v.producto_id = (
	SELECT producto_id
    FROM ventas
    GROUP BY producto_id
    ORDER BY SUM(cantidad) ASC LIMIT 1
);

-- Mostrar productos que se vendieron
SELECT nombre
FROM productos
WHERE producto_id IN (SELECT producto_id FROM ventas);

-- Mostrar productos QUE NO se vendieron
SELECT nombre
FROM productos
WHERE producto_id NOT IN (SELECT producto_id FROM ventas);


-- Dado un dataset con clientes, ventas, y productos, que hagan:

-- JOIN entre ventas y clientes para ver qué clientes compraron qué.

-- Calcular cuál es el cliente con más compras (en cantidad total).

-- Subconsulta para encontrar productos más caros que el promedio.

-- JOIN + agregación para ver cuánto gastó cada cliente.

