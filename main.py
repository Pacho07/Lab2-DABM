import switch as switch

import Model.Equipo
from Model.Equipo import *
from Model.Estudiante import Estudiante
import datetime
from Model.menu import *




Ventana=menu()

option=Ventana.ver()


if option==1:
    Ventana.menuTecnicover()
elif option==2:

    op=Ventana.menuEstudiantes()

    if op == 1:
        menu.menuEstudiantes()
        Estudiante.crearNuevoPrestamo()
    elif op == 2:
        Estudiante.consulPrestamo()
        menu.menuEstudiantes()

    elif op == 3:
        Equipo.verDatosTodos()
        menu.menuEstudiantes()

    elif op == 4:
        Estudiante.devolverPrestamo(input('Ingresar identificador del equipo'))
        menu.menuEstudiantes()

    elif op == 5:
        menu.ver()
    else:
        print('ingresar combinacion numerica valida')
        menu.ver()


elif option==3:
    quit()
else:
    print('combinacion invalida')






