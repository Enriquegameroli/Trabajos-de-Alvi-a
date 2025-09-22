class PromedioAlumnos:
    def leer_datos(self):
        self.alumnos = []
        for i in range(10):
            nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
            calificacion = float(input(f"Ingrese la calificación de {nombre}: "))
            self.alumnos.append((nombre, calificacion))
    
    def procesar_datos(self):
        total = sum(calificacion for _, calificacion in self.alumnos)
        self.promedio_grupal = total / 10
        self.destacados = [alumno for alumno in self.alumnos if alumno[1] > 9.5]
    
    def imprimir_resultados(self):
        print("\n--- Resultados del análisis ---")
        print(f"Promedio grupal: {self.promedio_grupal:.2f}")
        print("\nAlumnos con calificación mayor a 9.5:")
        for nombre, calificacion in self.destacados:
            print(f"- {nombre}: {calificacion:.2f}")
    
    def ejecutar(self):
        self.leer_datos()
        self.procesar_datos()
        self.imprimir_resultados()

grupo = PromedioAlumnos()
grupo.ejecutar()


