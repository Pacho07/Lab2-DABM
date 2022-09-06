import switch as switch

import Model.Equipo
from Model.Equipo import *
from Model.Estudiante import Estudiante
import datetime
from Model.menu import *

Ventana=menu(input('INGRESAR NOMBRE DEL LABORATORIO: '))

option=Ventana.ver()

if option==1:
    Ventana.menuTecnicover()
elif option==2:
    Ventana.menuEstudiantes()
elif option==3:
    quit()
else:
    print('combinacion invalida')






