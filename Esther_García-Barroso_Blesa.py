# Vamos a crear tres clases
# Guardar -- añadir usuario, editar usuario
# Login   -- metodo(email y contraseña) --> email: user@gmail.com, pass: 1234
# Usuario -- debe registrarse y hacer login

class Guardar:
    def __init__(self, email, passw):
        self.email = email
        self.passw = passw
        print(f"Usuario añadido: {email}")

    def edit_usuario(self, email, passw):
        self.email = email
        self.passw = passw
        print(f"Editado información del usuario: {email}")

class Login:
    def metodo_login(self, email, passw):
        if email == "user@gmail.com" and passw == "1234":
            print("Login correcto. Ahora puedes añadir o editar usuarios.")
        else:
            print("Credenciales incorrectas. No puedes añadir usuarios.")

class Usuario(Guardar, Login):
    def __init__(self, email, passw):
        super().__init__(email, passw)

usuario1 = Usuario("user@gmail.com", "1234")
usuario1.edit_usuario("esthergbblesa@gmail.com", "1234")

usuario1.metodo_login("user@gmail.com", "1234")
usuario1.metodo_login("resu@gmail.com", "0000")