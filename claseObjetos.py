class Vehiculo:
    def __init__(self, marca, tipo, nivel_gasolina):
        self.marca = marca
        self.tipo = tipo
        self.nivel_gasolina = nivel_gasolina

    def encender(self):
        if self.nivel_gasolina < 10:
            print(f"El {self.tipo} {self.marca} necesita gasolina.")
        else:
            print(f"El {self.tipo} {self.marca} está encendido.")

    def arrancar(self):
        print(f"El {self.tipo} {self.marca} está arrancando con {self.nivel_gasolina}% de combustible.")

class Motocicleta(Vehiculo):
    def __init__(self, marca, nivel_gasolina):
        super().__init__(marca, "moto", nivel_gasolina)

class Automovil(Vehiculo):
    def __init__(self, marca, nivel_gasolina):
        super().__init__(marca, "carro", nivel_gasolina)

# Función para obtener datos del usuario
def obtener_datos_vehiculo():
    marca = input("Introduce la marca del vehículo: ")
    tipo = input("Introduce el tipo de vehículo (motocicleta/automóvil): ").lower()
    nivel_gasolina = int(input("Introduce el nivel de combustible (%): "))

    if tipo == "motocicleta":
        return Motocicleta(marca, nivel_gasolina)
    elif tipo == "automóvil":
        return Automovil(marca, nivel_gasolina)
    else:
        raise ValueError("Tipo de vehículo no válido.")

# Crear instancias de las clases Motocicleta y Automovil basadas en la entrada del usuario
try:
    vehiculo = obtener_datos_vehiculo()
    vehiculo.encender()
    vehiculo.arrancar()
except ValueError as e:
    print(e)