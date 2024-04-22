import math

"""
lets assume Quadratic Equation is ax^2+bx+c=0
"""
def roots(a,b,c):
    delta = b*b - 4*a*c
    root_1 = (-b + math.sqrt(delta))/(2*a)
    root_2 = (-b - math.sqrt(delta))/(2*a)
    return root_1,root_2

def main():
    try :
        a = int(input("Enter a for Quadratic Equation - "))
        b = int(input("Enter b for Quadratic Equation - "))
        c = int(input('Enter c for Quadratic Equation - '))
    except Exception as e :
        print(e)
        return main()
    print(roots(a,b,c))

if __name__=="__main__":
    main()
