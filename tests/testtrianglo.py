import unittest

def calcular_area(a, b, c):
    # Calculamos el semiperímetro
    s = (a + b + c) / 2
    # Calculamos el área utilizando la fórmula de Herón
    areat = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return areat

class TestCalcularArea(unittest.TestCase):

    def test_area_triangulo_equilatero(self):
        # Triángulo equilátero, todos los lados tienen la misma longitud
        self.assertEqual(calcular_area(3, 3, 3), 3.8971143170299753)

    def test_area_triangulo_rectangulo(self):
        # Triángulo rectángulo, lados 3, 4, 5
        self.assertEqual(calcular_area(3, 4, 5), 6.0)

    def test_area_triangulo_escaleno(self):
        # Triángulo escaleno, lados 7, 8, 9
        self.assertEqual(calcular_area(7, 8, 9), 26.832815729997478)

if __name__ == '__main__':
    unittest.main()