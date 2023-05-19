#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    curkey = None
    lista = []
    
    for line in sys.stdin:
        key, val = line.split()
        val = int(val)
        
        if key != curkey:
            if curkey is not None:
                sys.stdout.write('{}\t{}\n'.format(curkey, ','.join(map(str, lista))))
                
            curkey = key
            lista = []
        
        lista.append(val)
    
    if curkey is not None:
        sys.stdout.write('{}\t{}\n'.format(curkey, ','.join(map(str, lista))))