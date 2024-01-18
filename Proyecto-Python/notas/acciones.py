import notas.nota as modelo

class Acciones :

    def crear(self,usuario):
        print(f"Ok {usuario[1]} Crea Nota")
        titulo = input("Introduce el titulo de tu nota")
        descripcion = input("Mete el contenido de tu nota")


        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f"Se ha guardado la nota: {nota.titulo}")
        else: 
            print(f"\n No se ha guardado la nota, lo siento {usuario}")

    def mostrar(self, usuario):
        print(f"notas del Usuario: {usuario[1]}")

        nota= modelo.Nota(usuario[0])
        notas=nota.listar()

        for nota in notas:
            print("\n---------------------------")
            print(nota[2])
            print(nota[3])
            print("\n---------------------------")

    def borrar(self,usuario):
        print(f"\n Borrar Notas ¿Que quieres borrar? {usuario[1]}")


        titulo=input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0],titulo) 
        eliminar = nota.eliminar()

        if eliminar[0] >=1:
            print(f"Se ha eliminado la nota {nota.titulo}")

        else:
            print("La nota no se ha borrado")