#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        cols    =   line.split()
        sys.stdout.write('{}\t{}\n'.format(cols[0],cols[2]))