
"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase:

Un __init_, donde los datos pueden estar vacíos.
Los setters y para  @property cada uno de los atributos. Hay que validar las entradas de datos.
crear un metodo mostrar(): Muestra los datos de la persona.
crear un metodo esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""

class Persona:

    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._edad = valor

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str):
            self._dni = valor

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def esMayorDeEdad(self):
        return self.edad >= 18


# Prueba
p1 = Persona("Ana", 20, "12345678A")
p1.mostrar()
print(p1.esMayorDeEdad())