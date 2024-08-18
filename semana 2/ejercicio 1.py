class telas:

    def ingresarDatos(self):
        self.metros = float(input("ingrese la cantidad de metros que nesesite pedir: "))

    def metrosPulgadas (self):
        self.pulgadas = round(self.metros/0.0254)
        return self.pulgadas
    
telas = telas()
datos = telas.ingresarDatos()
resultado = telas.metrosPulgadas()
print (f"la cantidad de tela en pulgadas a pedir es de: {telas.metrosPulgadas()}")