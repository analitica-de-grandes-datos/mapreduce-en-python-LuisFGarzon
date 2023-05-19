#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    orden= [] 
    for line in sys.stdin:

        letra,fecha,valor = line.strip().split(",")
        orden.append([letra,fecha,int(valor)])
    

    elements = sorted(orden, key =lambda x:(x[0],x[2]))
    
    for element in elements:
        sys.stdout.write("{}   {}   {}\n".format(element[0],element[1],element[2]))