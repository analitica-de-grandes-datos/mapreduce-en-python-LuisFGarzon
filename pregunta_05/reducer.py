#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave = None
    tot = 0
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == clave:
            tot += val
        else:
            if clave is not None:
                sys.stdout.write("{},{}\n".format(clave, tot))

            clave = key
            tot = val

    sys.stdout.write("{}\t{}\n".format(clave, tot))