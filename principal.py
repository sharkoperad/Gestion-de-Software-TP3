from registro import *
import math

def mostrar_menu():        
    menu= """
    =============================================================================
    \t\t\t\t\t\t\tMenu de Búsqueda
    =============================================================================
    1. Cargar proyectos
    2. Listar proyectos
    3. Actualizar proyecto
    4. Resumen por lenguaje
    5. Resumen por año
    6. Filtrar lenguaje
    7. Productividad
    8. Salir del Programa
    =============================================================================
    """
    print(menu)

def validar_entre(num, inf, sup):
    while num < inf or num > sup:
        #############VICKY
        print("Error, opcion no valida")
        #############VICKY
        num = int(input("Ingrese nuevamente: "))
    return num

def verificar(vec):
    if vec[0] is None:
        return -1
    return 0, vec

def convert_lan(num):
    languages = ("Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go")
    return languages[num]

#############VICKY, ACA NO HAGAS NADA

def display_tabla():
    cad = "{:<20}{:<20}{:<10}{:<10}{:^10}".format("Número de Proyecto", "Titulo", "Fecha", "Lenguaje", "Cantidad de Líneas de Código")
    return cad

#############VICKY TAMPOCO

# Funcion: Se pasa como parametro el vector creado e imprime sus respectivos componentes en el orden asignado anteriormente en los titulos de la tabla a mostrar.
def display_one(vec):
    cad = "{:<20}{:<20}{:<10}{:<10}{:^10}".format(vec.numero_projecto, vec.titulo, vec.fecha, vec.lenguaje, vec.cantidad)
    return cad, vec

def principal():
    tabla = [None]
    projectos = crearArreglo()
    if len(projectos) == 0:
        print("\nNo hay projectos")
        return
    cont = [0] * 10
    op = -1
    while op != 8:
        mostrar_menu()
        op = int(input("Ingrese opcion elegida (1 al 8): "))
        print()
        op = validar_entre(op, 1, 8)

        if op == 1:
            cargarArreglo_random(projectos)
            print("Se han cargado los projectos.")
        elif op == 2:
            print("Lista de Projectos: \n")
            print(display_tabla())
            for i in range(len(projectos)):
                print(display_one(projectos[i]))

        elif op == 4:
            i4 = opcion4(projectos, cont)
            print(i4)

        elif op == 5:
            i5 = opcion5(projectos)
            if i5 == -1:
                print("No hay nada")
            elif i5 is None:
                print("000")
            else:
                print(display_tabla())
                for i in range(len(i5)):
                    print(display_one(i5[i]))

        elif op == 6:
            item6 = opcion6(projectos)
            if item6 == -1:
                print("\nError...Arreglo no cargado")
            elif item6 is None:
                print("\nNo hay projectos con este lenguaje")
            else:
                print("Lenguajes: 1. Python, 2. Java, 3. C++, 4. Javascript, 5. Shell, 6. HTML, 7. Ruby, 8. Swift, 9. C#, 10. VB, 11. Go")
                print(display_tabla())
                for i in range(len(item6)):
                    print(display_one(item6[i]))


def opcion4(vec, cont):
    can = []
    print("\nLista valida de lenguajes: ")
    print(
          "1 = Python      5 = Shell      9 = C#\n"
          "2 = Java        6 = HTML       10 = VB\n"
          "3 = C++         7 = Ruby       11 = Go\n"
          "4 = Javascript  8 = Swift\n")
    sel = int(input("\nIngresar el codigo del lenguaje de la cual desesa saber el total de lineas de código: "))
    sel = validar_entre(sel, 0, 12)
    for j in range(len(vec)):
        if sel == vec[j].lenguaje:
            can.append(vec[j].cantidad)
            a = sum(can)
    print("La cantidad de lineas de código es de: ")
    print(a)

# 5) Resumen por año: Calcular la cantidad de proyectos por año de actualización,
# considerando los años entre 2000 y 2022 incluidos ambos.
# Mostrar los resultados solo de los años que tengan algún proyecto de software.
def opcion5(vec):
    fech = []
    #############VICKY

    x = int(input(' Ingrese año a buscar: '))
    for i in range(len(vec)):
        if x == vec[i].fecha:
            fech.append(vec[i])
    return fech
    #vector = [0] * 23

    # x = int(input(' buscar año: '))
    # for i in range(len(vec)):
    #    if x == vec[i].fecha:
    #        vector.append(x)

    #print(x)

def opcion6(vec):
    # creacion del vector secundario donde se agregaran los articulos nuevos.
    langi = []
    a = int(input("¿Qué lenguaje necesita?: "))
    #############VICKY
    for i in range(len(vec)):
        if a == vec[i].lenguaje:
            langi.append(vec[i])
    # Ordenamiento por numero
    m = len(langi)
    if m == 0:
        return None
    for i in range(m - 1):
        for j in range(i + 1, m):
            if langi[i].numero_projecto > langi[j].numero_projecto:
                langi[i], langi[j] = langi[j], langi[i]
    return langi


# 7) Productividad: A partir del resultado obtenido en el punto 5, determinar el año con mayor cantidad de proyectos actualizados,
# considerando mostrar todos los años si fuera más de uno con dicha cantidad.


if __name__ == '__main__':
    principal()


