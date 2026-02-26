class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono 
    
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def incluir_clientes(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente añadido: {cliente.nombre} {cliente.apellido}")

    def buscar_cliente(self, telefono):
        for cliente in self.clientes:
            if cliente.telefono == telefono:
                return cliente
        return None

    def modificar_cliente(self, telefono, nuevo_nombre=None, nuevo_apellido=None, nuevo_telefono=None):
        """Modifica los datos de un cliente existente buscándolo por su teléfono actual."""
        cliente = self.buscar_cliente(telefono)
        if cliente:
            if nuevo_nombre:
                cliente.nombre = nuevo_nombre
            if nuevo_apellido:
                cliente.apellido = nuevo_apellido
            if nuevo_telefono:
                cliente.telefono = nuevo_telefono
            print(f"✅ Cliente con teléfono {telefono} modificado con éxito.")
            return True
        else:
            print(f"❌ Error: No se encontró ningún cliente con el teléfono {telefono}.")
            return False

    def borrar_cliente(self, telefono):
        """Elimina un cliente de la lista usando su teléfono."""
        cliente = self.buscar_cliente(telefono)
        if cliente:
            self.clientes.remove(cliente)
            print(f"🗑️ Cliente {cliente.nombre} {cliente.apellido} eliminado.")
            return True
        else:
            print(f"❌ Error: No se encontró ningún cliente con el teléfono {telefono}.")
            return False

    def mostrar_todos(self):
        print(f"\n--- Listado de clientes de {self.nombre} ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        for cliente in self.clientes:
            print(cliente)
        print("---------------------------------------\n")