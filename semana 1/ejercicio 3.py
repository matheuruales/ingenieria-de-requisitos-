class pagos:

    def ingresoDatos(self):
        print("ingrese el numero de horas trabajadas en la semana")
        self.horas = float(input())
        print("ingrese el precio de pago por hora")
        self.pagoPorHora = float(input())

    def pagoSemanal(self):
        self.pagoSemanal = self.horas * self.pagoPorHora
        return self.pagoSemanal
    
pagos = pagos()
pagos.ingresoDatos()
print(f"el pago de la semana es de: {pagos.pagoSemanal()}")

