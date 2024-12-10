import math

A = float(input())
B = float(input())
C = float(input())

def RCUADRATICAS(A, B, C):
    discri = (B * B) - (4 * A * C)
    if discri < 0:
        return "No tiene soluciones reales"
    elif discri > 0:
        Raiz = math.sqrt(discri)
        x1 = (-B + Raiz) / (2 * A)
        x2 = (-B - Raiz) / (2 * A)
        return f"La ecuación de segundo grado tiene 2 soluciones: X1 = {x1} y X2 = {x2}"
    elif discri == 0:
        x = -B / (2 * A)
        return f"La ecuación de segundo grado tiene una única solución: X = {x}"


resultado = RCUADRATICAS(A, B, C)
print(resultado)

        

