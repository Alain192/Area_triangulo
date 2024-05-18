def calcular_area(a, b, c):
    # Calculamos el semiperímetro
    s = (a + b + c) / 2
    # Calculamos el área utilizando la fórmula de Herón
    areat = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return areat

# Solicitamos al usuario que ingrese las longitudes de los tres lados
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Llamamos a la función para calcular el área
areat = calcular_area(lado1, lado2, lado3)

# Imprimimos el resultado
print("El área del triángulo es:", areat)
