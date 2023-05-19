#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    orden= [] 
    for line in sys.stdin:

        key, val1, val2 = line.strip().split(",")
        val2 = int(val2)
        orden.append([key,val1,val2])
    

    objetivo = sorted(orden, key =lambda x:(x[2]))
    
    for j in range(0,6):
        sys.stdout.write("{}   {}   {}\n".format(objetivo[j][0],objetivo[j][1],objetivo[j][2]))