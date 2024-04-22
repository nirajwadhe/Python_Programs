import numpy as np
import random as rm
def main():
    elements = []
    try :
        M = int(input("Enter number of Rows -"))
        N = int(input("Enter numner of Columns -"))
    except Exception as e :
        print(e)
        main()

    for i in range(0,M*N):
        elements.append(rm.randrange(-100,100))

    print(reshape_array(elements,M,N))

def reshape_array(element,rows,columns):
    arr = np.array(element)
    return arr.reshape(rows,columns)

if __name__=="__main__":
    main()
