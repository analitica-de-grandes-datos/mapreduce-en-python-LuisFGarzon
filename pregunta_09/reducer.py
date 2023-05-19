#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    delta = 0
    for line in sys.stdin:
        delta += 1
        key,val1,val2   =   line.split()
        val2 =   int(val2)
        sys.stdout.write('{}   {}   {}\n'.format(key,val1,val2))
        if delta == 6:
            break