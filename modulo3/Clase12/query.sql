-- Breve repaso
SELECT nombre, precio
FROM productos
WHERE categoria = 'Ropa' AND precio > 30;

-- Me da el error:
-- Error Code: 1046. No database selected Select the default DB to be used by double-clicking its name in the SCHEMAS list in the sidebar.
-- Este error es porque no estamos usando la base de datos, como lo arreglamos:
USE ambox;

-- Funciones de agregacion:
-- SUM() Suma total de una columna numerica
-- AVG() Promedio
-- MAX() Valor Maximo.
-- MIN() Valor Minimo.
-- COUNT() Cuenta de Filas.

-- Suma Total de todos los precios
SELECT SUM(precio) AS total_ventas FROM productos;

-- Precio Promedio
SELECT AVG(precio) AS promedio FROM productos;

-- Producto Mas caro
SELECT MAX(precio) AS maximo FROM productos;

-- Total de productos
SELECT COUNT(*) FROM productos;

-- Agrupaciones con GROUP BY
SELECT categoria, AVG(precio)
FROM productos
GROUP BY categoria;
-- Esto agrupa los productos por categoria y devuelve el precio promedio de cada una.

-- Cantidad de productos por categoria
SELECT categoria, COUNT(*) FROM productos
GROUP BY categoria;

-- Ejemplo Brian
SELECT categoria, AVG(precio), MAX(precio) FROM productos GROUP BY categoria;

-- Total de ventas por categoria
SELECT categoria, SUM(precio) FROM productos GROUP BY categoria;


-- HAVING
-- Que categoria tiene mas de 2 productos
SELECT categoria, COUNT(*) AS total
FROM productos
GROUP BY categoria
HAVING COUNT(*) >= 2;

SELECT categoria, AVG(precio) AS promedio
FROM productos
GROUP BY categoria
HAVING AVG(precio) > 40;

SELECT * FROM productos;

INSERT INTO productos (id, nombre, precio, categoria) VALUES
(5, 'Remera', 20.0, 'Ropa'),
(6, 'Camisa', 30.0, 'Ropa'),
(7, 'Ojotas', 15.0, 'Calzado');

-- Mostrar el precio total de todos los productos.
SELECT SUM(precio) FROM productos;

-- Mostrar el promedio de precio de cada categoría.
SELECT categoria, AVG(precio) FROM productos GROUP BY categoria;

-- Mostrar cuántos productos hay por categoría.
SELECT categoria, COUNT(*) FROM productos GROUP BY categoria;

-- Mostrar las categorías que tienen más de 1 producto.
SELECT categoria FROM productos GROUP BY categoria HAVING COUNT(*) > 1;

-- Mostrar categorías cuyo promedio de precio supere los 25.
SELECT categoria FROM productos HAVING AVG(precio) > 25;

SELECT * FROM productos;


-- EJERCICIOS EXTRAS

-- 1 Mostrar el producto más caro y el más barato.
SELECT MAX(precio) AS maximo_precio, MIN(precio) AS minimo_precio
FROM productos;

-- Si queremos hacerlo que muestre le producto en si:
SELECT nombre, precio
FROM productos
ORDER BY precio DESC
LIMIT 1;

SELECT nombre, precio
FROM productos
ORDER BY precio ASC
LIMIT 1;

-- 2 Mostrar el nombre y precio del producto más caro dentro de cada categoría.

SELECT p.categoria, p.nombre, p.precio
FROM productos p
WHERE p.precio = (
  SELECT MAX(precio)
  FROM productos
  WHERE categoria = p.categoria
);


-- 3 Mostrar todas las categorías ordenadas por su precio promedio de mayor a menor.
SELECT categoria, AVG(precio) AS promedio
FROM productos
GROUP BY categoria
ORDER BY promedio DESC;

SELECT * FROM productos LIMIT 1 OFFSET 1;
SELECT * FROM productos LIMIT 2000 OFFSET 5;
-- LIMIT es para que me traiga X cantidad MAXIMA de entradas
-- OFFSET es la cantidad de entradas que "ignora" si le pongo un numero X, lo que me traiga, va a ser luego de ignorar X elementos.

-- Sistema de paginado:
-- Pagina 1:
SELECT * FROM productos LIMIT 20 OFFSET 0;
-- Pagina 2:
SELECT * FROM productos LIMIT 20 OFFSET 20;
-- Pagina 3:
SELECT * FROM productos LIMIT 20 OFFSET 40;

-- 4 Listar los productos cuyo precio sea mayor al promedio general.
SELECT nombre, precio
FROM productos
WHERE precio > (SELECT AVG(precio) FROM productos);


-- 5 Mostrar el total gastado si compro un producto de cada categoría.
SELECT SUM(max_precio) AS total_gastado
FROM (
	SELECT MAX(precio) AS max_precio
    FROM productos
    GROUP BY categoria
) AS sub;


-- 6 Listar los productos de la categoría 'Ropa' que cuesten más que cualquier producto de 'Accesorios'.
SELECT nombre, precio
FROM productos
WHERE categoria = 'Ropa'
AND precio > ALL (
  SELECT precio
  FROM productos
  WHERE categoria = "Accesorios"
);

-- 7 Mostrar las 2 categorías con mayor cantidad de productos.

SELECT categoria, COUNT(*) AS cantidad
FROM productos
GROUP BY categoria
ORDER BY cantidad DESC LIMIT 2;


-- 8 Calcular cuánto representa cada categoría en porcentaje del total de productos.
SELECT categoria,
	ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM productos), 2) AS porcentaje
FROM productos
GROUP BY categoria;

-- 10 Mostrar el nombre de los productos que tienen el mismo precio que otro producto.
SELECT p1.nombre, p1.precio
FROM productos p1
JOIN productos p2
  ON p1.precio = p2.precio
 AND p1.id <> p2.id;
 
 SELECT * FROM productos;
