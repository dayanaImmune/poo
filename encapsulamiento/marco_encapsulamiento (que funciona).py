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
        if not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = valor

    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        self._edad = valor

   
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        if not isinstance(valor, str):
            raise ValueError("El DNI debe ser una cadena de texto.")
        self._dni = valor

   
    def mostrar(self):
        """Muestra los datos de la persona."""
        return f"Nombre: {self.nombre} | Edad: {self.edad} | DNI: {self.dni}"

    def esMayorDeEdad(self):
        """Devuelve un valor lógico indicando si es mayor de edad (18+)."""
        return self.edad >= 18


if __name__ == "__main__":

    p1 = Persona()
    print("Persona 1 (vacía):", p1.mostrar())
    
    # Asignamos datos usando los setters
    p1.nombre = "Ana"
    p1.edad = 25
    p1.dni = "12345678A"
    print("Persona 1 (actualizada):", p1.mostrar())
    print("¿Ana es mayor de edad?:", p1.esMayorDeEdad())

    # Creamos una persona directamente con datos
    p2 = Persona("Luis", 15, "87654321B")
    print("\Persona 2:", p2.mostrar())
    print("¿Luis es mayor de edad?:", p2.esMayorDeEdad())