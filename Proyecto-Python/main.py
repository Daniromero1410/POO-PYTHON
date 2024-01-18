"""

Proyecto mysql-Python
1.Abrir Asistente
2.Login o registro 
3.Si elegimos registro, creara un usuario en la bbdd
4.Si elegimos Login, identifica al usuario y nos preguntara
5. Crear Nota, Mostrar Notas,Borrarlas,etc.

"""

from usuarios import acciones



print("""
ACCIONES DISPONIBLES:
      -REGISTRO
      -LOGIN
""")
haz_el = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")
#Creacion de acciones para las pregunta
if accion == "Registro":
    haz_el.registro()

elif accion == "Login":
    haz_el.login()
    
