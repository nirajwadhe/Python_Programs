# Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not

def main():
    try :
        year_to_check = int(input("Enter a Year - "))
        if len(str(year_to_check))!=4 :
            raise ValueError("Enter a Integer with 4 digits")
    except Exception as e :
        print("Exception Occured - " , e)
        return main()
    else :
        leap_year(year_to_check)

def leap_year(yr) :
    if (yr%400==0) or (yr%4==0 )and (yr%100!=0):
        print(f"Year {yr} is Leap")
    else :
        print(f'Year {yr} is not leap')    


if __name__=="__main__":
    main()