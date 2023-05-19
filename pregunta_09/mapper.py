#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:
        letter, date, value = line.strip().split('   ')
        sys.stdout.write("{}\t{}\t{}\n".format(letter, date, value))