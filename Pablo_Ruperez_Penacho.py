# Ejercicio
# Vamos a crear tres clases

# Guardar -- añadir usuario, editar usuario
# Login -- metodo(email y contraseña) --> email _ user@gmail.com, pass: 1234
# Usuario -- debe poder añadir usuario y hacer login

class Guardar:

    def añadir_usuario(self, nuevo_usuario):
        self.nuevo_usuario = nuevo_usuario
        print("Usuario añadido con éxito")
     
    def editar_usuario(self, nuevo_nombre):
        self.nuevo_usuario = nuevo_nombre
        print("Usuario editado con éxito")
        
class Login:
    
    def login(self, email, contraseña):
        self.email = email
        self.contraseña = contraseña

        if email == "user@gmail.com" and contraseña == "1234":
            print("Login con éxito")
        else:
            print("Error")


class Usuario(Guardar, Login):
    
    def guardar(self, usuario):
        Guardar().añadir_usuario(usuario)
    
    def editar(self, usuario):
        Guardar().editar_usuario(usuario)
    
    def logear(self,correo,contraseña):
        Login().login(correo,contraseña)

pepe = Usuario()
pepe.guardar("Pepe")
pepe.editar("Tot")

pepe.logear("user@gmail.com","1234")

