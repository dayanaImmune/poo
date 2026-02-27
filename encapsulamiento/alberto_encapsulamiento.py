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
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            if nuevo_valor != "":
                self._nombre = nuevo_valor
            else:
                print("El nombre no puede estar vacio rellenalo")
        else:
            print("El nombre debe de contener texto")

    @property
    def edad(self):
        if self._edad < 0:
            return 0
        return self._edad

    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            if nuevo_valor >= 0:
                self._edad = nuevo_valor
            else:
                print("La edad no puede ser negativa.")
        else:
            print("La edad son números enteros")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, nuevo_valor):
        if isinstance(nuevo_valor, str):
            if nuevo_valor != "":
                self._dni = nuevo_valor
            else:
                print("El DNI está vacio, completalo")
        else:
            print("El DNI debe de ser numerico.")

    def mostrar(self):
        print("Nombre:", self._nombre)
        print("Edad:", self.edad)  # usa el getter
        print("DNI:", self._dni)

    def esMayorDeEdad(self):
        return self.edad >= 18
    
persona1 = Persona("Ana", 20, "47999652U")
persona2= Persona("Fructuoso",40,"51777895P")

persona1.mostrar()
persona2.mostrar()
