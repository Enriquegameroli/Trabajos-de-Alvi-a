class triángulo():

    def datos(self):
        self.base = float(input("Ingrese la base del triángulo: "))
        self.altura = float(input("Ingrese la altura del triángulo: "))
    
    def calcular_area(self):
        self.area = (self.base * self.altura) / 2
    
    def imprimir_resultado(self):
        print(f"\nResultados:")
        print(f"Base: {self.base} unidades")
        print(f"Altura: {self.altura} unidades")
        print(f"Área del triángulo: {self.area:.2f} unidades cuadradas")
    
    def ejecutar(self):
        self.datos()
        self.calcular_area()
        self.imprimir_resultado()

triangulo = triángulo()
triangulo.ejecutar()



