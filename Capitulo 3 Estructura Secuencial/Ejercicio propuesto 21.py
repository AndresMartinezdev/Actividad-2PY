# Dado 3 lados de un triángulo
L1 = float(input())
L2 = float(input())
L3 = float(input())

# Calcular Área, Perímetro y Semiperímetro
Perimetro = L1 + L2 + L3
Semiperimetro = Perimetro / 2
Area_triangulo = (Semiperimetro * (Semiperimetro - L1) * (Semiperimetro - L2) * (Semiperimetro - L3)) ** 0.5

# Elegir L1 como base y calcular altura
Altura = (2 * Area_triangulo) / L1

# Mostrar resultados
print(f"Perímetro: {Perimetro}")
print(f"Semiperímetro: {Semiperimetro}")
print(f"Área: {round(Area_triangulo, 2)}")
print(f"Altura relativa a la base {L1}: {round(Altura, 2)}")
 