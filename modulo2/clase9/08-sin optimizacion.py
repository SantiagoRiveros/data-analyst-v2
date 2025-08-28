import time
import math

# Parámetros
start_val = 0
stop_val = 10
num = 10000000

# Generar 100.000 valores entre 0 y 10 (tipo linspace)
step = (stop_val - start_val) / (num - 1)
x = [start_val + i * step for i in range(num)]

# Inicio de conteo de tiempo:
start = time.time()

# Calcular f(x) = e^(-x) * sin(x) con math
y = [math.exp(-val) * math.sin(val) for val in x]

# medir el tiempo
end = time.time()

print("Tiempo de calculo con bucle:", end - start, "segundos")
