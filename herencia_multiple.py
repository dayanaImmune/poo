class Universidad:
    def __init__(self, nombre_uni):
        self.nombre_uni = nombre_uni

class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, nombre, edad, nombre_uni, especialidad):
        Universidad.__init__(self, nombre_uni)
        Carrera.__init__(self,especialidad)
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, estudia {self.especialidad} en la universidad {self.nombre_uni}")

estudiante1 = Estudiante("Pepe", 19, "IMMUNE", "Ingenieria de software")
estudiante1.mostrar_datos()
print(Estudiante.__mro__) #method resolution order 

class Uno:
    def metodo(self):
        print("uno")

class Dos(Uno):
    def metodo(self):
        print("dos")

class Tres(Uno):
    def metodo(self):
        print("tres")

class Cuatro(Dos, Tres):
    def metodo_final(self):
        print("cuatro")

obj = Cuatro()
obj.metodo()


class Guardar:
    def añadir_usuario(self, usuario):
        print("tilin")
    def editar_usuario(self, usuario):
        print("sigma")
    
