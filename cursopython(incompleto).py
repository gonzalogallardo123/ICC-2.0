import sys
puntos = 0
def preguntacorrecta(p):
    print("Bien Hecho")
    p = p + 1000
    return p
def preguntaincorrecta(p):
    print("Eso es incorrecto")
    p = p - 500
    return p
print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
print("¶´´´´´¶´´´´´´¶´´¶¶¶¶´´¶¶´´¶´´´´´¶¶¶´´´´¶¶´´´´´¶")
print("¶´´¶¶¶¶´´¶¶´´¶´´¶¶¶¶´´¶¶´´¶´´¶¶´´¶´´¶¶´´¶´´¶¶¶¶")
print("¶´´´´´¶´´´´´´¶´´¶¶¶¶´´¶¶´´¶´´¶¶´´¶´´¶¶´´¶´´´´´¶")
print("¶¶¶¶´´¶´´¶¶´´¶´´¶¶¶¶´´¶¶´´¶´´¶¶´´¶´´¶¶´´¶¶¶¶´´¶")
print("¶´´´´´¶´´¶¶´´¶´´´´´¶´´´´´´¶´´´´´¶¶¶´´´´¶¶´´´´´¶")
print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
print("")
nombre = str(input("Ingrese su nombre: "))
print("********************************************************************************")
print("Hola",nombre,", bienvenido a este curso basico de Python")
print("Menu: \n\t 1) Comenzar el curso \n\t 2) Elegir un tema \n\t 3) Terminar el programa")
opcion1 = input("Seleccione una opcion: ")
print("********************************************************************************")
if opcion1 == "1":
    print("Para comenzar veremos el comando más basico: print()")
    print("Este comando nos permite imprimir cualquier frase o numero que deseemos")
    frase1 = input("Ingrese una frase para imprimir: ")
    print("********************************************************************************")
    print('Para imprimir tu frase deberas escribir: print("',frase1,'")',sep='')
    print("Ten en cuenta que esta funcion tambien te permitira imprimir resultados matematicos como: print(5+2)")
    print('Ahora te hare una pregunta respecto al comando print ')
    print('Si deseas imprimir la frase "hola mundo", el comando deberá ser: ')
    print('a) print("zapato")')
    print('b) print("hola mundo")')
    print('c) input("hola mundo")')
    respuesta1 = (input("Respuesta: "))
    if respuesta1 == 'b':
        preguntacorrecta(puntos)
    else:
        preguntaincorrecta(puntos)
    print("********************************************************************************")
