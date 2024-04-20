def main():
    n_harmonic = int(input("Enter a nth harmonic number "))
    try :
        if n_harmonic==0:
            raise ValueError("Enter Correct Number")
    except Exception as e :
        print('Enter a Correct Number - ',e)
    else :
        print(harmonic_number(n_harmonic))

def harmonic_number(num):
    if num==1 :
        return 1
    else :
        return (1/num)+harmonic_number(num-1)
    

if __name__=="__main__":
    main()