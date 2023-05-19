#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        limpiar =   line.strip()
        letra,fecha,valor = limpiar.split("   ")
        sys.stdout.write("{},{},{}\n".format(letra,fecha,valor))