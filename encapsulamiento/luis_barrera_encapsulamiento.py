class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre, self.edad, self.dni = nombre, edad, dni

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, v): self._nombre = v if isinstance(v, str) else ""

    @property
    def edad(self): return self._edad
    @edad.setter
    def edad(self, v): self._edad = v if isinstance(v, int) and v >= 0 else 0

    @property
    def dni(self): return self._dni
    @dni.setter
    def dni(self, v): self._dni = v if isinstance(v, str) else ""

    def mostrar(self):
        print(self.nombre, self.edad, self.dni)

    def esMayorDeEdad(self):
        return self.edad >= 18
p = Persona("Ana", 20, "12345678A")
p.mostrar()
print(p.esMayorDeEdad())