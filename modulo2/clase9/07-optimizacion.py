import numpy as np
import time

# Generar 100.000 valores entre 0 y 10
x = np.linspace(0, 10, 10000000)

# Inicio de conteo de tiempo:
start = time.time()

# Calcular f(x) vectorizado
y = np.exp(-x) * np.sin(x)

# medir el tiempo
end = time.time()

print("Tiempo de calculo vectorizado:", end - start, "segundos")