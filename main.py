import os
from time import sleep

def padre():
    procesosAEjecutar = int(input('-> Padre con PID: %d, Introduce el número de procesos que deseas ejecutar: ' % os.getpid()))

    while procesosAEjecutar > 0:
        newPid = os.fork()
        procesosAEjecutar = procesosAEjecutar - 1
        
        if newPid == 0:
            hijo()
    os._exit(0)
                
def hijo():
    print('\n-> Hijo con PID: %d' % os.getpid())
    sleep(5)
    print('\n-> Hijo con PID: %d, voy a terminar' % os.getpid())
    os._exit(0)
    
if __name__ == '__main__':
    padre()