class Calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: No se puede dividir entre cero."

# Llamada a la clase Calculadora
calculadora = Calculadora()

# Imprimir los resultados obtenidos
print("Suma:", calculadora.suma())
print("Resta:", calculadora.resta())
print("Multiplicación:", calculadora.multiplicacion())
print("División:", calculadora.division())

