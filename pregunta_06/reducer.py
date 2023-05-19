#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave = None
    maxx = None
    minn = None
    for linea in sys.stdin:

        key, val = linea.split("\t")
        val = float(val)

        if key == clave:
            if val > maxx:
                maxx = val
            if val < minn:
                minn = val
        else:
            if clave is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(clave, maxx, minn))

            clave = key
            maxx = val
            minn = val

    sys.stdout.write("{}\t{}\t{}\n".format(clave, maxx, minn))