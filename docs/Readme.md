# UD1-2 Generación de procesos en Python
## **Ejercicio 1**


Este programa permite que un proceso padre genere diferentes procesos hijos realizando los siguientes pasos:

1. Primero el proceso padre preguntará al usuario el número de procesos hijos que quiere ejecutar.

2. A continuación el proceso padre creará con **os.fork()** tantos procesos hijos como indicó el usuario.

3. Al ejecutarse los procesos hijos mostrarán los PID de cada uno de ellos, y morirán al pasar 5 segundos desde que comenzó su ejecución.

> __AVISO:__ *Este programa sólo es compatible con sistemas **Linux***.