#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
#Construye los siguientes métodos para la clase:

#Un __init_, donde los datos pueden estar vacíos.
#Los setters y para  @property cada uno de los atributos. Hay que validar las entradas de datos.
#crear un metodo mostrar(): Muestra los datos de la persona.
#crear un metodo esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.


class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str):
            self._nombre = valor
        else:
            self._nombre = ""

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self._edad = valor
        else:
            self._edad = 0

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str) and len(valor) >= 5:
            self._dni = valor
        else:
            self._dni = ""

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

    def esMayorDeEdad(self):
        if self.edad >= 18:
         return "Es mayor de edad"
        else:
         return "No es mayor de edad"


class Empleado(Persona):
    def __init__(self, nombre="", edad=0, dni="", salario=0):
        super().__init__(nombre, edad, dni)
        self.salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._salario = valor
        else:
            self._salario = 0

    def mostrar(self):
        return super().mostrar() + f", Salario: {self.salario}€"

    
x = Persona("Jaime", 17, "77345A")
print(x.mostrar())
print(x.esMayorDeEdad())

y = Empleado("Pablo", 30, "08765B", 2000)
print(y.mostrar())
