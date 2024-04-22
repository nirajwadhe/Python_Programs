import random as rm
def unique_number(number_of_coupon):
    coupon_stack = []
    len_of_digit = int(input("Enter a Number of Digit of Unique Code - "))
    for i in range(1,number_of_coupon+1):
        unique_id = rm.randint(int("1"*len_of_digit),int("9"*len_of_digit))
        if unique_id not in coupon_stack :
            coupon_stack.append(unique_id)
    return coupon_stack
def main():
    try :
        number_of_coupon = int(input("Enter a Number of Coupons -"))
    except Exception as e:
        print(e)
        main()        
    print(unique_number(number_of_coupon))

if __name__=="__main__":
    main()
