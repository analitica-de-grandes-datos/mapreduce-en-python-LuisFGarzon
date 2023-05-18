#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    for line in sys.stdin:
        clean   =   line.strip()
        key, val = clean.split(",")
        sys.stdout.write("{}\t{}\n".format(key,val))