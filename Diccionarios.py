#Crear diccionario Python
class Estudiante:
    def __init__(self, datos):
        self.datos = datos
        
    def get_dato(self, clave):
        return self.datos.get(clave)
    
    def set_dato(self, clave, valor):
        self.datos[clave] = valor
        
    def mostrar_datos(self):
        return self.datos

# Creación del objeto con datos personales
estudiante = Estudiante({  
    "Nombre": "Laura",
    "Matricula": "231690498-2",
    "Edad": 27,
    "Peso": 67,
    "Telefono": "3111453376",
    "Domicilio": "Villa de Robledo #9",
    "Carrera": "CDIA"
})  

# Acceso a elementos
print(estudiante.get_dato("Nombre"))       # Laura
print(estudiante.get_dato("Carrera"))      # CDIA
print(estudiante.datos["Telefono"])        # 3111453376 (Telefono)

# Modificación de elementos
estudiante.set_dato("Edad", 28)
estudiante.set_dato("Direccion", "Calle 123")
estudiante.datos["Peso"] = 68  # Modificación directa

print(estudiante.mostrar_datos())