#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        letra,fecha,valor   =   line.split()
        valor =   int(valor)
        sys.stdout.write('{}   {}   {}\n'.format(letra,fecha,valor))