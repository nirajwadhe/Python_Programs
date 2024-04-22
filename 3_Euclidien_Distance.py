import math
def euclidian_dist(x1,y1):
    print(f"Euclidian distance for {x1} and {y1} is {math.pow(math.pow(x,2)+math.pow(y,2),1/2)}")

def main():
    global x,y
    try :
        x= int(input("Enter a 1st side - "))
        y = int(input("Enter a 2nd side - "))
    except Exception as e :
        print(e)
        main()  
    euclidian_dist(x,y)
if __name__=="__main__":
    main()
