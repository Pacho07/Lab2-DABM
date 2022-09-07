from Model.menu import *

class Estudiante:

    def __init__(self, nombre, carnet, fechaPrestamo, fechaentregaPrestamo, equipo):
        self.nombre = nombre
        self.carnet = carnet
        self.fechaPrestamo = fechaPrestamo
        self.fechaentregaPrestamo = fechaentregaPrestamo
        self.equipo=equipo

    def save(self):
        archivo = open('BaseDatos/Estudiantes.txt', 'a')
        linea = ';'.join(
            [self.nombre, self.carnet, self.fechaPrestamo, self.fechaentregaPrestamo, self.equipo])
        archivo.write(linea + '\n')
        archivo.close()

        #aquí quitamos el numero de disponibilidad

        archivo = open("../BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')

        arreglado = []

        for i in mantenimiento:
            iterator = i.split(';')


            if iterator[1] == self.equipo:
                iterator[5] = int(iterator[5]) - 1
                iterator[6] = int(iterator[6]) + 1
                arreglado.append(';'.join(iterator))
            else:
                arreglado.append(';'.join(iterator))

        archivo.close()

        archivo = open("../BaseDatos/Equipos.txt", 'w')

        archivo.write('\n'.join(arreglado))






    @staticmethod
    def consulPrestamo():
        archivo = open("BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')

        arreglado = []

        for i in mantenimiento:
            iterator = i.split(';')
            print(iterator)

            if int(iterator[6])> 0:

                arreglado.append(iterator)

        archivo.close()

        print('''


                EQUIPOS QUE ESTAN PRESTADOS


                ''')



        header = ['nombre', 'referencia', 'proveedor', 'ciclo mantenimiento (dias)', 'ultimo mantenimiento', 'cantidad','cantidad prestada']
        print(tabulate(arreglado, header, tablefmt="grid"))

        archivo.close()



    @staticmethod
    def crearNuevoPrestamo():

        print('REGISTRAR NUEVO ESTUDIANTES')
        nombre=input('nombre: ')
        carnet=input('carnet: ')
        entregaPrestamo=input('fecha entrega prestamo de forma (%d/%m/%y) :  ')
        entregaPrestamo = datetime.datetime.strptime(entregaPrestamo, "%d/%m/%y")

        equipo=Equipo.consulta(input('identificador del equipo que desea prestar: '))
        equipo=''.join(equipo)
        equipo=equipo.split(';')
        equipo=':'.join(equipo)

        prestamo = datetime.datetime.today().strptime('%d/%m/%y')

        entregaPrestamo = datetime.datetime.strptime(entregaPrestamo, "%d/%m/%y")

        validation=Equipo.consulta(nombre)

        if validation[5]==validation[6]:

            print('YA NO HAY MAS EQUIPOS DE ESTA REFERENCIA DISPONIBLES')
            menu.ver()

        else:

            e = Estudiante(nombre,carnet,prestamo,entregaPrestamo,equipo)
            e.save()

    @staticmethod
    def devolverPrestamo(identificador):

        archivo = open("BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')

        arreglado = []

        for i in mantenimiento:
            iterator = i.split(';')

            if iterator[1] == str(identificador):
                iterator[5] = str(int(iterator[5]) + 1)
                iterator[6] = str(int(iterator[6]) - 1)

                arreglado.append(';'.join(iterator))
            else:
                arreglado.append(';'.join(iterator))

        archivo.close()

        archivo = open("BaseDatos/Equipos.txt", 'w')

        archivo.write('\n'.join(arreglado))