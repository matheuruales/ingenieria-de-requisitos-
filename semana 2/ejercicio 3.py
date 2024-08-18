class mayor:
    def dato(self):
        self.valor1 = float(input("ingrese el primer valor numerico:"))
        self.valor2 = float(input("ingrese el segundo valor numerico:"))

    def calculo(self):
        self.valorMayor = None
        if self.valor1 > self.valor2:
            self.valorMayor = self.valor1
        elif self.valor2 > self.valor1:
            self.valorMayor = self.valor2
        else:
            self.valorMayor = "niniguno los valores ingresados son iguales"
        return self.valorMayor
mayor = mayor()
datoa = mayor.dato()
calculo = mayor.calculo()
print(f"el numero mayor es: {mayor.calculo()}")