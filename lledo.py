# Vamos a crear tres clases
# Guardar -- añadir usuario, editar usuario
# Login   -- metodo(email y contraseña) --> email: user@gmail.com, pass: 1234
# Usuario -- debe registrarse y hacer login

class Guardar:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        print(f"Usuario registrado: {self.email}")

    def añadir_usuario(self, email, password):
        self.email = email
        self.password = password
        print(f"Usuario añadido: {self.email}")

    def editar_usuario(self, nuevo_email, nuevo_password):
        self.email = nuevo_email
        self.password = nuevo_password
        print(f"Usuario editado: {self.email}")


class Login:
    def metodo_login(self, email, password):
        if email == "user@gmail.com" and password == "1234":
            print("Login correcto.")
        else:
            print("Credenciales incorrectas.")


class Usuario(Guardar, Login):
    def __init__(self, email, password):
        super().__init__(email, password)

usuario1 = Usuario("user@gmail.com", "1234")

usuario1.editar_usuario("user@gmail.com", "1234")

usuario1.metodo_login("user@gmail.com", "1234")
usuario1.metodo_login("otro@gmail.com", "0000")

