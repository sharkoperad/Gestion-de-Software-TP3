import random


class Registro:
    def __init__(self, num_proj, titulo, fecha, leng, cant):
        self.numero_projecto = num_proj
        self.titulo = titulo
        self.fecha = fecha
        self.lenguaje = leng
        self.cantidad = cant


def validar_mayor_que(num, lim):
    while num < lim:
        print("Error. Debe ser mayor a, ", lim)
        num = int(input("Ingrese nuevamente: "))
    return num


def crearArreglo(tabla):
    n = int(input("Ingrese la cantidad de componentes del arreglo(mayor que 0): "))
    n = validar_mayor_que(n, 0)
    vec = n * tabla
    return vec

# Funcion: Se le pasa como parametro la cantidad de componenetes ingresados y se
# completan los campos del arreglo aleatoriamente.


def cargarArreglo_random(vec):
    m = len(vec)
    for i in range(m):
        num_proj = random.randint(10000, 99999)
        titulo = f'proyecto {random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}-{random.randint(100, 999)}'
        fecha = random.randrange(2000, 2022)
        leng = random.randrange(1, 12)
        cant = random.randint(0, 100)
        
        vec[i] = Registro(num_proj, titulo, fecha, leng, cant)



