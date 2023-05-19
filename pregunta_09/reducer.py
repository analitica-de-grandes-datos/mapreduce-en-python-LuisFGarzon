#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    lista = [tuple(line.split("\t")[:3]) for line in sys.stdin]
    lista.sort(key=lambda x: int(x[2]))
    lista = lista[:6]

    for linea in lista:
        sys.stdout.write("{}   {}   {}\n".format(*linea))