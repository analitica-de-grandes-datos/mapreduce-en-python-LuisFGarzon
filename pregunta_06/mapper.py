#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for linea in sys.stdin:
        clean = linea.strip()
        sys.stdout.write("{}\t{}\n".format(clean.split(" ")[0],clean.split("  ")[2]))