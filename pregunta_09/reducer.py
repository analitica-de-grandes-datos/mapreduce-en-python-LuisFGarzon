#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == '__main__':
    res = [line.strip().split(",") for line in sys.stdin]
    res = sorted(res, key=lambda x: int(x[2]))[:6]
    for j in res:
        sys.stdout.write("{}   {}   {}\n".format(*j))

