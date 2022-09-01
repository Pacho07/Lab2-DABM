class menu:

    def __init__(self, laboratorio ):
        self.laboratorio = laboratorio

    def ver(self):
        print('''
          BIENVENIDO AL SISTEMA
          '''.center(50, '*'))

        print('laboratorio: ' + self.laboratorio)
        print('1.Tecnicos')
        print('2.Estudiantes')

        op = input('>>>')
        return op


    def menuTecnicover(self):
        print('''
          MENU TECNICOOS DE LABORATORIO
          '''.center(28, '*'))

        print('1.Comprar equipos')
        print('2.Registrar prestamo')

        op = input('>>>')

        return op



