'''
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:

un __init__, donde los datos pueden estar vacios.
los setters y para @property cada uno de los atributos. Hay que validar las entradas de datos.
crear un método mostrar(): muestra los datos de la persona.
crear un metodo esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    #  NOMBRE 
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip() != "":  #"nuevo_nombre.strip() != "" ": es para que no esté en blanco ni para que no se agreguen
                                                                          #números como nombre, y eliminar espacios al inicio y final
            self._nombre = nuevo_nombre

    # EDAD
    @property
    def edad(self):
        if self._edad < 0:
            return 0
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >= 0:
            self._edad = nueva_edad

    # DNI
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni):
        if isinstance(nuevo_dni, str) and len(nuevo_dni.strip()) >= 7:  #para que no supere la longitud de dígitos del dni
            self._dni = nuevo_dni

    # MOSTRAMOS TODO 
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def esMayorDeEdad(self):    #si es mayor de edad... True / False
        return self.edad >= 18


# Ejemplo
persona1 = Persona("Alba", 18, "09232565C")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())
