# 1. Clase para gestionar el almacenamiento
class Guardar:
    def __init__(self):
        self.base_datos = []

    def añadir_usuario(self, usuario):
        self.base_datos.append(usuario)
        print(f"Usuario {usuario['email']} guardado.")

    def editar_usuario(self, email, nueva_pass):
        for usuario in self.base_datos:
            if usuario['email'] == email:
                usuario['pass'] = nueva_pass
                print("Contraseña editada.")

# 2. Clase para gestionar el acceso
class Login:
    def verificar(self, email, password, lista_usuarios):
        for u in lista_usuarios:
            if u['email'] == email and u['pass'] == password:
                return True
        return False

# 3. Clase Usuario que hereda de ambas (Herencia Múltiple)
class Usuario(Guardar, Login):
    def __init__(self, email, password):
        # Inicializamos la clase padre Guardar para tener la lista
        Guardar.__init__(self)
        self.email = email
        self.password = password

    def registrarse(self):
        # Usamos el método heredado de Guardar
        datos = {"email": self.email, "pass": self.password}
        self.añadir_usuario(datos)

    def hacer_login(self, email_ingresado, pass_ingresada):
        # Usamos el método heredado de Login
        if self.verificar(email_ingresado, pass_ingresada, self.base_datos):
            print(f"Login exitoso. Bienvenido {email_ingresado}")
        else:
            print("Error: Credenciales incorrectas.")

# --- PRUEBA DEL EJERCICIO ---

# Creamos el usuario según el ejemplo de la imagen
nuevo_usuario = Usuario("user@gmail.com", "1234")

# Añadir usuario
nuevo_usuario.registrarse()

# Intentar login
nuevo_usuario.hacer_login("user@gmail.com", "1234")