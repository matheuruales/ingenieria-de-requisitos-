class Terreno:

    def ingresarDatos(self):
        print("Ingrese el valor de la base del rectángulo del terreno:")
        self.rectangulo1 = float(input())
        print("Ingrese el valor de la altura del rectángulo del terreno:")
        self.rectangulo2 = float(input())
        print("Ingrese la altura del triángulo:")
        self.triangulo1 = float(input())

    def calcularAreaTotal(self):
        areaRectangulo = self.rectangulo1 * self.rectangulo2
        areaTriangulo = (self.rectangulo1 * self.triangulo1) / 2
        area_total = areaRectangulo + areaTriangulo
        return area_total
    
terreno = Terreno()
datos = terreno.ingresarDatos()
area = terreno.calcularAreaTotal()
print(f"el area del terreno es de {terreno.calcularAreaTotal()}")