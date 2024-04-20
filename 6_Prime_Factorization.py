def prime_fact(num):
    if num<0:
        raise Exception('Enter a Positive Number')
    n= 2
    while (n*n<=num):
        while(num>1):
            while num%n==0:
                print(n)
                num=num/n
            n+=1

def main():
    try :
        number = int(input("Enter a number "))
        if number==0:
            raise ValueError("Enter Correct Number")
    except Exception as e :
        print('Enter a Correct Number - ',e)
    else :
        print(prime_fact(number))

if __name__=='__main__':
    main()