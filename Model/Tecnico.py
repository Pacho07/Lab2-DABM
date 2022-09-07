import datetime
import BaseDatos
from tabulate import tabulate

class Tecnico:

    @staticmethod
    def ConsultaMante():

        archivo = open("BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')
        #mantenimiento.pop()

        iniRango = input('Ingrese la fecha de inicio a buscar:')
        iniRango = datetime.datetime.strptime(iniRango, "%d/%m/%y")

        finRango = input('Ingrese la fecha final a buscar:')
        finRango = datetime.datetime.strptime(finRango, "%d/%m/%y")

        eqPo = []

        for i in range(len(mantenimiento)):

            iterator = mantenimiento[i].split(';')

            ven =datetime.datetime.strptime(iterator[4], "%d/%m/%y")+ datetime.timedelta(days=int(iterator[3]))


            if ven >= iniRango and ven <= finRango:
                eqPo.append(iterator)

        print('''
        
        
        EQUIPOS QUE TIENEN MANTENIMIENTO EN DICHAS FECHAS
        
        
        ''')

        header = ['nombre', 'referencia', 'proveedor', 'ciclo mantenimiento (dias)', 'ultimo mantenimiento', 'cantidad']
        print(tabulate(eqPo, header, tablefmt="grid"))

        archivo.close()

    @staticmethod
    def regisMante(referencia):
        archivo = open("BaseDatos/Equipos.txt", 'r')
        mantenimiento = archivo.readlines()
        mantenimiento = ''.join(x for x in mantenimiento if x not in '\n')
        mantenimiento = mantenimiento.split('\n')

        arreglado=[]

        for i in mantenimiento:
            iterator = i.split(';')
            if iterator[1]==referencia:
                iterator[4]=datetime.date.today().strftime('%d/%m/%y')
                arreglado.append(';'.join(iterator))

            else:
                arreglado.append(';'.join(iterator))

        archivo.close()

        archivo = open("BaseDatos/Equipos.txt", 'w')

        archivo.write('\n'.join(arreglado))




