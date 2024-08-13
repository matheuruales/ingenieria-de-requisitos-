class granja:

    def ingresarDatos(self):
        print("ingrese el numero de litros")
        self.litros = float(input())
        print("ingrese el precio del galon")
        self.presioGalon = float(input())
    
    def LitrosGalones(self):
        self.galones = (self.litros / 3.785)
        return self.galones
        
    def pago (self):
        pago = self.galones * self.presioGalon
        return pago
    
granja = granja()
litros = granja.ingresarDatos()
litrosGalones = granja.LitrosGalones()
print(f"los galones son {granja.LitrosGalones()} y el pago es de  {granja.pago()}")