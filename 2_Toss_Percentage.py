'''Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails'''

import random as rm

def flip_coin() :
    try :
        number = int(input("Enter a Number of times to flip - "))  
        if number>0 :
            x=0
            heads = 0
            tails = 0
            while x!=number :
                ran_num = rm.randint(0,1)
                if ran_num==0 :
                    heads+=1
                else :
                    tails+=1
                x+=1

            print(f"Percentage of Heads are {(heads/number)*100} %")
            print(f"Percentage of Heads are {(tails/number)*100} %")    
        else :
            print("Enter +ve Number")
            return flip_coin()           
    except :
        print("Enter Positive Integer")
        flip_coin()

if __name__=="__main__":
    flip_coin()