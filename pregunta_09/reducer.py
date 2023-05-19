#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    list_tuple = [tuple(line.strip().split("\t")) for line in sys.stdin]
    list_tuple = sorted(list_tuple, key=lambda x: int(x[2]))[:5]

    for tuple in list_tuple:
        sys.stdout.write("{}   {}   {}\n".format(*tuple))