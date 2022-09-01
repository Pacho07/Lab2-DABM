from Model.Equipo import Equipo


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
        prestamo=input('fecha prestamo: ')
        entregaPrestamo=input('fecha entrega prestamo: ')
        equipo=Equipo.consulta('william',input('nombre del equipo'))
        equipo=equipo
        e = Estudiante(nombre,carnet,prestamo,entregaPrestamo,equipo)
        e.save()


