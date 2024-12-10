import math  
# Leer lado del triángulo
Lado_del_triangulo = float(input("Introduce el lado del triángulo equilátero: "))

# Calcular Perímetro
Perimetro = 3 * Lado_del_triangulo

# Calcular Altura usando Pitágoras
Cateto1 = Lado_del_triangulo / 2
Hipotenusa = Lado_del_triangulo
Altura = math.sqrt(Hipotenusa**2 - Cateto1**2)

# Calcular Área
Area_del_Triangulo = (Lado_del_triangulo * Altura) / 2

# Mostrar resultados
print(f"Perímetro: {Perimetro}")
print(f"Altura: {round(Altura, 2)}")
print(f"Área del triángulo: {round(Area_del_Triangulo, 2)}")
