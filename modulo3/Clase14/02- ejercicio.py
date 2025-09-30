from sqlalchemy import create_engine
import pandas as pd


# # engine = create_engine("mysql+mysqlconnector://usuario:contraseña@host/nombre_db")

""" 
mysql+mysqlconnector: indica que usamos MySQL y ese driver.

root:passwrod: usuario y contraseña (acá el usuario es "root").

localhost: dirección del servidor (usualmente local).

tienda: nombre de la base de datos.

"""

engine = create_engine("mysql+mysqlconnector://root:@localhost/ambox")

productos = pd.read_sql("SELECT * FROM productos", engine)

print(productos)

# Venta con detalles

ventas = pd.read_sql("SELECT v.venta_id, c.nombre AS cliente, p.nombre AS producto, v.cantidad, v.fecha FROM ventas v JOIN clientes c ON v.cliente_id = c.cliente_id JOIN productos p ON v.producto_id = p.producto_id", engine)

print(ventas)

# ¿Quien compro mas productos?

mayor = ventas.groupby("cliente")["cantidad"].sum().sort_values(ascending=False)

print(mayor)

# ¿Qué producto se vendió más veces?

populares = ventas.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
print(populares)

# ¿Cuanto gasto cada cliente?

ventas_precio = pd.read_sql("""
SELECT c.nombre AS cliente, SUM(v.cantidad * p.precio) AS total_gastado
FROM ventas v
JOIN clientes c ON v.cliente_id = c.cliente_id
JOIN productos p ON v.producto_id = p.producto_id
GROUP BY c.nombre
ORDER BY total_gastado DESC
""", engine)

print(ventas_precio)

# ¿Cuánto se vendió por día?

ventas_dia = ventas.groupby("fecha")["cantidad"].sum().sort_values(ascending=False)
print(ventas_dia)

# Graficar productos más vendidos

import matplotlib.pyplot as plt


ventas.groupby("producto")["cantidad"].sum().plot(kind="bar", color="skyblue")
plt.title("Productos más vendidos")
plt.ylabel("Cantidad")
plt.show()