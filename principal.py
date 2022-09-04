from registro import *
import math

##Actualizado 4/9 20:39
def mostrar_menu():
    menu = """ 
     ============================================================================= 
    \t\t\t\t\t\t\t  Menu de Búsqueda 
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
        print("\t\t\t\t\t\t\t\tError, opcion no valida")
        print("\t\t\tRecuerde que la opcion elegida tiene que estar entre el ", inf, " y el ", sup, ".")
        num = int(input("\t\t\t\t\t\t\t\t Ingrese nuevamente: "))
    return num


def verificar(vec):
    if vec[0] is None:
        return -1
    return 0, vec


def convert_lan(num):
    languages = ("0", "Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go")
    return languages[num]


def display_tabla():
    cad = "{:<20}{:<20}{:<10}{:<10}{:^10}".format("Número de Proyecto", "Titulo", "Fecha", "Lenguaje",
                                                  "Cantidad de Líneas de Código")
    return cad


# Funcion: Se pasa como parametro el vector creado e imprime sus respectivos componentes en el orden asignado anteriormente en los titulos de la tabla a mostrar.
def display_one(vec):
    cad = "{:<20}{:<20}{:<10}{:<10}{:^10}".format(vec.numero_projecto, vec.titulo, vec.fecha, vec.lenguaje,
                                                  vec.cantidad)
    return cad

def principal():
    cont = [0] * 10
    op = -1
    while op != 8:
        mostrar_menu()
        op = int(input("\t\t\t\t\t\t\tIngrese opcion elegida (1 al 8): "))
        print()
        op = validar_entre(op, 1, 8)

        if op == 1:
            tabla = [None]
            projectos = crearArreglo()
            tabla.append(cargarArreglo_random(projectos))
            print('\t\t\t\t\t\t\t   La Opcion que eligio es la 1.')
            print("\t\t\t\t\t\t\t   Se han cargado los projectos de manera alteratoria.")
            if len(projectos) == 0:
                print("\n\t\t\t\t\t\t\t\t\t\tNo hay projectos")
                return
        elif op == 2:
            print("\t\t\t\t\t\t\t\t\t Lista de Projectos: \n")
            print(display_tabla())
            for i in range(len(projectos)):
                print(display_one(projectos[i]))

        elif op == 4:
            print('\t\t\t\t\t\t\t\tLa Opcion que eligio es la 4.')
            i4 = opcion4(projectos)

        elif op == 5:
            print('\t OPCION 5 RESUMEN POR AÑO: ')
            acumulador = opcion5(projectos)

        elif op == 6:
            item6 = opcion6(projectos)
            if item6 == -1:
                print("\n\t\t\t\t\t\t\t\t\t\t\tError...Arreglo no cargado")
            elif item6 is None:
                print("\n\t\t\t\t\t\t\tNo hay proyectos con este lenguaje")
            else:
                print(
                    "Lenguajes: 1. Python, 2. Java, 3. C++, 4. Javascript, 5. Shell, 6. HTML, 7. Ruby, 8. Swift, 9. C#, 10. VB, 11. Go")
                print(display_tabla())
                for i in range(len(item6)):
                    print(display_one(item6[i]))
        elif op == 7:
            determinar_mayor(acumulador)

        elif op == 8:
            print('\t\t\t\t\t\t\t\t\tNos vemos pronto!')


def opcion4(vec):
    can = []
    print("\n\t\t\t\t\t\t\t\tLista valida de lenguajes: ")
    print(
        "                           1 = Python           6 = HTML             \n"
        "                           2 = Java             7 = Ruby             \n"
        "                           3 = C++              8 = Swift            \n"
        "                           4 = Javascript       9 = C#               \n"
        "                           5 = Shell            10 = VB              \n"
        "                                                11 = GO              \n")

    sel = int(input("\n     Ingresar el codigo del lenguaje de la cual desesa saber el total de lineas de código: "))
    sel = validar_entre(sel, 0, 11)
    for j in range(len(vec)):
        if sel == vec[j].lenguaje:
            can.append(vec[j].cantidad)
            a = sum(can)
    sp = print("\t\t\t\t\t\tLa cantidad de lineas de código de " + str(convert_lan(sel)) + " es de: ", a)


# 5) Resumen por año: Calcular la cantidad de proyectos por año de actualización,
# considerando los años entre 2000 y 2022 incluidos ambos.
# Mostrar los resultados solo de los años que tengan algún proyecto de software.
def opcion5(vec):
    fech = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
    acumulador = 23 * [0]
    n = len(vec)
    for i in range(n):
        for j in range(23):
            if vec[i].fecha == fech[j]:
                a = fech[j] % 1000
                acumulador[a] += 1
    for q in range(23):
        if acumulador[q] != 0:
            print('Año', fech[q], 'Tiene', acumulador[q], 'proyectos')
    return acumulador

def opcion6(vec):
    # creacion del vector secundario donde se agregaran los articulos nuevos.
    langi = []
    print('\t\t\t\t\t\t\tLa Opcion que eligio es la numero 6.')
    a = int(input("'\t\t\t\t\t\t\t\t¿Qué lenguaje necesita?: "))
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
def determinar_mayor(vec):
    fecha = (2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)
    may = 0
    for i in range(len(vec)):
        if vec[i] > may:
            may = vec[i]
    if may != 0:
        print('Los años con mas proyectos')
        for j in range(len(vec)):
            if vec[j] == may:
                print('Año:', fecha[j], 'con', vec[j], 'proyectos')

if __name__ == '__main__':
    principal()
