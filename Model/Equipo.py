from tabulate import tabulate
import datetime


class Equipo:

    def __init__(self, nombre, referencia, proveedor, cicloMante, ultMante, cantidad,diaMante):

        self.nombre = nombre
        self.referencia = referencia
        self.proveedor = proveedor
        self.cicloMante = cicloMante
        self.ultMante = ultMante
        self.cantidad = cantidad


    @staticmethod
    def verDatos(self):
        header = ['nombre', 'referencia', 'proveedor', 'ciclo mantenimiento (dias)', 'ultimo mantenimiento', 'cantidad', 'necesidad de mantenimiento']
        datos = [[self.nombre, self.referencia, self.proveedor, self.cicloMante, self.ultMante, self.cantidad]]
        print(tabulate(datos, header, tablefmt="grid"))

    @staticmethod
    def verDatosTodos():
        header = ['nombre', 'referencia', 'proveedor', 'ciclo mantenimiento (dias)', 'ultimo mantenimiento', 'cantidad', 'necesidad de mantenimiento']
        archivo = open("../BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')


        manteAyuda=[]

        for i in range(len(mantenimiento)):

            iterator= mantenimiento[i].split(';')

            manteAyuda.append(iterator)

        print(tabulate(manteAyuda, header, tablefmt="grid"))

        archivo.close()




    def save(self):
        archivo = open("../BaseDatos/Equipos.txt", 'a')
        linea = ';'.join(
            [self.nombre, self.referencia, self.proveedor, self.cicloMante, self.ultMante, self.cantidad])
        archivo.write(linea + '\n')
        archivo.close()

    @staticmethod
    def consulta(nombre):
        archivo = open("../BaseDatos/Equipos.txt", 'r')
        prestamos = archivo.readline()
        flag = 'falso'
        while (flag == 'falso'):
            if nombre in prestamos:
                flag = 'verdadero'
            else:
                prestamos = archivo.readline()
        prestamos = ''.join(x for x in prestamos if x not in '\n')
        header = ['nombre', 'referencia', 'proveedor', 'ciclo mantenimiento', 'ultimo mantenimiento', 'cantidad']
        datos = [list(prestamos.split(';'))]

        print(tabulate(datos, header, tablefmt="grid"))

        return prestamos
        archivo.close()

    def eliminar(self, nombre):
        archivo = open('BaseDatos/Equipos.txt', 'r')
        buscando = archivo.readlines()
        pos = 0

        for i in range(len(buscando)):
            if nombre in buscando[i]:
                pos = i
                break
        buscando.pop(pos)
        archivo.close()
        archivo = open("../BaseDatos/Equipos.txt", 'w')

        archivo.write(''.join(buscando))
        archivo.close()

    def modificar(self, nombre):

        archivo = open("../BaseDatos/Equipos.txt", 'r')
        buscando = archivo.readlines()
        pos = 0

        for i in range(len(buscando)):
            if nombre in buscando[i]:
                pos = i
                break

        referencia = input('ingrese la referencia')
        proveedor = input('ingrese el proveedor')
        cicloMante = input('ingrese el ciclo mantenimiento')
        ultMante = input('ingrese el ultimo mantenimiento')
        cantidad = input('ingrese la cantidad')

        linea = ';'.join([nombre, referencia, proveedor, cicloMante, ultMante, cantidad + '\n'])
        archivo.close()
        buscando[pos] = linea
        archivo = open("../BaseDatos/Equipos.txt", 'w')

        archivo.write(''.join(buscando))
        archivo.close()

    @staticmethod
    def crear():

        print('REGISTRAR NUEVO EQUIPO')
        nombre = input('nombre: ')
        referencia = input('referencia: ')
        proveedor = input('proveedor: ')

        cicloMan = int(input('ciclo de mantenimiento entero de (dias): '))
        ultimoMan = input('ultimo mantenimiento de forma (%d/%m/%y) : ')
        cantidad = input('cantidad: ')

        ultimoMan = datetime.datetime.strptime(ultimoMan, "%d/%m/%y")





        e = Equipo(nombre, proveedor, referencia, cicloMan, ultimoMan, cantidad)
        e.save()

        return e


Equipo.verDatosTodos()