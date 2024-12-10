import math

class Circulo:
    def __init__(self, radio):
        self.radio = int(radio)

    def calcular_area(self):
        return float(math.pi * self.radio**2)

    def calcular_perimetro(self):
        return float(2 * math.pi * self.radio)


class Rectangulo:
    def __init__(self, base, altura):
        self.base = int(base)
        self.altura = int(altura)

    def calcular_area(self):
        return float(self.base * self.altura)

    def calcular_perimetro(self):
        return float(2 * (self.base + self.altura))


class Cuadrado:
    def __init__(self, lado):
        self.lado = int(lado)

    def calcular_area(self):
        return float(self.lado**2)

    def calcular_perimetro(self):
        return float(4 * self.lado)


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = int(base)
        self.altura = int(altura)

    def calcular_area(self):
        return float((self.base * self.altura) / 2)

    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return float(self.base + self.altura + hipotenusa)


class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = int(diagonal_mayor)
        self.diagonal_menor = int(diagonal_menor)
        self.lado = int(lado)

    def calcular_area(self):
        return float((self.diagonal_mayor * self.diagonal_menor) / 2)

    def calcular_perimetro(self):
        return float(4 * self.lado)


class Trapecio:
    def __init__(self, base_mayor, base_menor, lado, altura):
        self.base_mayor = int(base_mayor)
        self.base_menor = int(base_menor)
        self.lado = int(lado)
        self.altura = int(altura)

    def calcular_area(self):
        return float((self.base_mayor + self.base_menor) * self.altura / 2)

    def calcular_perimetro(self):
        return float(self.base_mayor + self.base_menor + (2 * self.lado))


class PruebaFiguras:
    @staticmethod
    def main():
        circulo = Circulo(2)
        rectangulo = Rectangulo(1, 2)
        cuadrado = Cuadrado(3)
        triangulo = TrianguloRectangulo(3, 5)
        rombo = Rombo(4, 5, 3)
        trapecio = Trapecio(10, 5, 2, 3)

        print(f"Área del círculo: {circulo.calcular_area()}")
        print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")

        print(f"Área del rectángulo: {rectangulo.calcular_area()}")
        print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

        print(f"Área del cuadrado: {cuadrado.calcular_area()}")
        print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")

        print(f"Área del triángulo: {triangulo.calcular_area()}")
        print(f"Perímetro del triángulo: {triangulo.calcular_perimetro()}")

        print(f"Área del rombo: {rombo.calcular_area()}")
        print(f"Perímetro del rombo: {rombo.calcular_perimetro()}")

        print(f"Área del trapecio: {trapecio.calcular_area()}")
        print(f"Perímetro del trapecio: {trapecio.calcular_perimetro()}")


if __name__ == "__main__":
    PruebaFiguras.main()
