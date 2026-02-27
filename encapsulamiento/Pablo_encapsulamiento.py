"""

Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase:

Un __init_, donde los datos pueden estar vacíos.
Los setters y para  @property cada uno de los atributos. Hay que validar las entradas de datos.
crear un metodo mostrar(): Muestra los datos de la persona.
crear un metodo esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
2509CEBF - 1º CEBF - Object Oriented Programming (10)

"""

class Persona:
    def __init__(self, nombre = False, edad = False, dni = False):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = str(dni)

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor,str):
            self.__nombre = nuevo_valor

    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad >0:
            self.__edad = nueva_edad
        
    @dni.setter
    def dni(self, nuevo_dni):
        if len(nuevo_dni) == 9 and nuevo_dni[:-1].isdigit() and nuevo_dni[-1].isalpha():
            self.__dni = nuevo_dni

    def mostrar(self):
        return(f"El nombre de la persona es {self.__nombre}, su edad es {self.__edad} años y su DNI es {self.__dni}")
    
    def esmayoredad(self):
        if self.__edad >= 18:
            return(f"Es mayor de edad tiene {self.__edad} años")

p = Persona()
p.nombre = "Pablo"
p.edad = 18
p.dni = "04268156T"
print(p.mostrar())  
print(p.esmayoredad())  
    