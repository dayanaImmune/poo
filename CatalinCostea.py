# Vamos a crear tres clases
# Guardar -- añadir un usuario, editar usuario (debe mostrar añadido con exito y luego otro print editado con éxito)
# Login -- método(que necesite email y contraseña) -- el email permitido: user@gmail.com, pass: 1234 si nos dan bien estos datos el usuario ha iniciado sesión con éxito y si no que diga que los datos no coinciden.
# Usuario -- debe poder añadir un usuario y hacer login. No hace falta una lista para los usuarios con un print es suficiente.

class Guardar:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        print("Añadido con éxito")
    
    def editar_usuario(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        print("Editado con éxito")

class Login:
    def iniciar_sesion(self, email, contraseña):
        if email == "user@gmail.com" and contraseña == "1234":
            print("El usuario ha iniciado sesión con éxito")
        else:
            print("Los datos no coinciden")

class Usuario(Guardar, Login):
    def __init__(self, nombre, email, contraseña):
        super().__init__(nombre, email, contraseña)

primer_usuario = Usuario("Catalin", "user@gmail.com", "1234")

primer_usuario.editar_usuario("Catalin Costea", "user@gmail.com", "1234")

primer_usuario.iniciar_sesion("user@gmail.com", "1234")

primer_usuario.iniciar_sesion("otro@gmail.com", "5644")