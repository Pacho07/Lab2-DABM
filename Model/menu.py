
from Model.Tecnico import *
from Model.Equipo import *







class menu:

    @staticmethod
    def ver():

        print('''
          BIENVENIDO AL SISTEMA
          '''.center(50, '*'))

        print('1.Tecnicos')
        print('2.Estudiantes')
        print('3.salir')

        op = input('>>>')
        return int(op)


    @staticmethod
    def menuTecnicover():
        print('''
          MENU TECNICOOS DE LABORATORIO
          '''.center(28, '*'))

        print('1.Comprar equipos')
        print('2.Consultar equipo')
        print('3.Ver todos los equipos')
        print('4.Eliminar equipo')
        print('5.Modificar equipo')
        print('6.Consultar Mantenimiento')
        print('7.Hacer mantenimiento')
        print('8.Volver')

        op = int(input('>>>'))



        if op==1:
            Equipo.crear()
            menu.menuTecnicover()
        elif op==2:
            Equipo.consulta(input('ingresar nombre de persona que desea buscar'))
            menu.menuTecnicover()
        elif op==3:
            Equipo.verDatosTodos()
            menu.menuTecnicover()

        elif op==4:
            Equipo.eliminar(input('equipo que desea eliminar'))
            menu.menuTecnicover()

        elif op==5:
            Equipo.modificar(input('ingrese el nombre de quien desea modificar'))
            menu.menuTecnicover()

        elif op==6:
            Tecnico.ConsultaMante()
            menu.menuTecnicover()

        elif op==7:
            Tecnico.regisMante(input('ingrese identificador del equipo a realizar mantenimiento'))
            menu.menuTecnicover()
        elif op==8:
            menu.ver()

        else:
            print('por favor poner una combinacion numerica correcta')
            menu.menuTecnicover()

    @staticmethod
    def menuEstudiantes():


        print('''
                  MENU ESTUDIANTES
                  '''.center(28, '*'))

        print('1.Hacer un nuevo prestamo')
        print('2.Consultar equipos prestados')
        print('3.ver todos los equipos ')
        print('4.devolver prestamos')
        print('5.volver')


        op = int(input('>>>'))

        return op




