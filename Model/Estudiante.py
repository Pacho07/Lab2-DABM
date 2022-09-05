from Model.Equipo import Equipo
import datetime

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

    @staticmethod
    def crearNuevoPrestamo():

        print('REGISTRAR NUEVO ESTUDIANTES')
        nombre=input('nombre: ')
        carnet=input('carnet: ')
        prestamo=int(input('fecha prestamo de forma (%d/%m/%y) :  '))
        entregaPrestamo=int(input('fecha entrega prestamo de forma (%d/%m/%y) :  '))
        equipo=Equipo.consulta(input('serial del equipo que desea prestar: '))
        equipo=''.join(equipo)
        equipo=equipo.split(';')
        equipo=':'.join(equipo)

        prestamo = datetime.datetime.today()
        entregaPrestamo = datetime.datetime.strptime(entregaPrestamo, "%d/%m/%y")

        e = Estudiante(nombre,carnet,prestamo,entregaPrestamo,equipo)
        e.save()


