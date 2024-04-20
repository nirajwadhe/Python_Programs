def main():
    try :
        power_number = int(input("Enter a Power - "))
        if power_number<0 or power_number>31 :
            raise ValueError("Enter a number between range")
        
    except Exception as e :
        print(e)
        main()
    else :
        print(power(power_number))    

def power(number):
        return 2**(number)
    

if __name__ == "__main__":
    main()