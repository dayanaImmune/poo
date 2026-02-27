#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
#Construye los siguientes métodos para la clase:

#Un __init_, donde los datos pueden estar vacíos.
#Los setters y para  @property cada uno de los atributos. Hay que validar las entradas de datos.
#crear un metodo mostrar(): Muestra los datos de la persona.
#crear un metodo esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self,edad=0,nombre="",DNI=""):
        self.__edad=edad
        self.__nombre=nombre
        self.__DNI=DNI
    
    @property
    def edad(self):
        if self.__edad<0:
            return 0
        return self.__edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def DNI(self):
        return self.__DNI
    
    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor,int):
            self.__edad=nuevo_valor
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        if isinstance(nuevo_valor,str):
            self.__nombre=nuevo_valor

    @DNI.setter
    def DNI(self, nuevo_valor):
        if isinstance(nuevo_valor,str):
            self.__DNI=nuevo_valor

    def mostrar(self):
        print(f"Esta persona se llama {self.nombre}, tiene {self.edad} años y su DNI es: {self.DNI}")
    
    def esMayorDeEdad(self):
        if self.edad<18:
            return False
        else:
            return True
        
persona1=Persona(25,"Niamh","50505050L")
persona1.mostrar()
persona1.DNI=54
persona1.nombre="Dennys"
persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad")
else:
    print("Es menor")