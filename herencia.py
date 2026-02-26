class Cliente:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Tel: {self.telefono}"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []  # Listado de clientes

    def incluir_cliente(self, cliente):
        """Añade un objeto Cliente a la lista."""
        self.clientes.append(cliente)
        print(f"✅ Cliente añadido: {cliente.nombre} {cliente.apellido}")

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
        """Muestra todos los clientes de la empresa (función extra para comprobar)."""
        print(f"\n--- Listado de clientes de {self.nombre} ---")
        if not self.clientes:
            print("No hay clientes registrados.")
        for cliente in self.clientes:
            print(cliente)
        print("---------------------------------------\n")


# ==========================================
# EJEMPLO DE USO
# ==========================================

if __name__ == "__main__":
    # 1. Crear empresa
    mi_empresa = Empresa("Tech Solutions")

    # 2. Crear clientes
    cliente1 = Cliente("Ana", "García", "600111222")
    cliente2 = Cliente("Luis", "Pérez", "600333444")

    # 3. Incluir clientes
    mi_empresa.incluir_cliente(cliente1)
    mi_empresa.incluir_cliente(cliente2)
    
    mi_empresa.mostrar_todos()

    # 4. Buscar cliente
    print("Buscando cliente con teléfono 600111222:")
    encontrado = mi_empresa.buscar_cliente("600111222")
    if encontrado:
        print(f"Encontrado: {encontrado}")

    # 5. Modificar cliente
    print("\nModificando el teléfono de Luis...")
    mi_empresa.modificar_cliente("600333444", nuevo_telefono="600999888")
    
    mi_empresa.mostrar_todos()

    # 6. Borrar cliente
    print("Borrando a Ana...")
    mi_empresa.borrar_cliente("600111222")
    
    mi_empresa.mostrar_todos()