import notas.acciones
import usuarios.usuario as modelo

class Acciones:

    def registro(self):
        print("\nINICIO DE REGISTRO")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cual es tu apellido?: ")
        email = input("Introduce tu Email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()

        if registro[0]>=1:
            print(f"\nRegistro completo, bienvenido {registro[1].nombre}")
        else: 
            print("\nNo te has registrado completamente")

    def login(self):
        print("INICIO DE REGISTRO EN EL SISTEMA")

        try:
            email = input("Introduce tu Email: ")
            password = input("Introduce tu contraseña: ")
            

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]},te has registrado en el sistema el {login[5]}")
                self.prox_accions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, intentalo mas tarde ")
    def prox_accions(self,usuario):

        print("""
            Acciones Disponibles :
            -Crear Nota (crear)
            -Mostrar tus notas (mostrar)
            -Eliminar nota (eliminar)
            -Salir (salir)
            """)
        
        accion = input("¿Que quieres hacer?: ")
        haz_el = notas.acciones.Acciones()


        if accion == "crear":
            haz_el.crear(usuario)
            self.prox_accions(usuario)
        elif accion == "mostrar":
            haz_el.mostrar(usuario)
            self.prox_accions(usuario)
        elif accion == "eliminar":
            print("Que deseas eliminar")
            haz_el.borrar(usuario)
            self.prox_accions(usuario)
        elif accion == "salir":
            exit()
        



