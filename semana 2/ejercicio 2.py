class pisina:
    def datos (self):
        self.largo = float(input("ingrese el largo de la pisina en metros:"))
        self.ancho = float(input("ingrese el ancho de la pisina en metros:"))
        self.alto = float(input("ingrese el alto de la pisina en metros:"))
        self.precio = float(input("ingrese el precios del metro cubico de agua"))

    def calculo (self):
        self.area = self.largo*self.ancho*self.alto
        self.pago = round(self.area*self.precio)
        return self.pago
    
pisina = pisina()
datos = pisina.datos()
calculo = pisina.calculo()
print(f"el pago que deve realizar por llenar la pisina es de: {pisina.calculo()}")
