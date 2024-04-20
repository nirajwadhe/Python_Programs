'''
Take User Name as Input. Ensure UserName has min 3 char
Logic -> Replace <<UserName>> with the proper name
O/P -> Print the String with User Name
'''

def main():
    username = input("Enter a username - ")
    try:
        if len(username) > 3  :
            print(f"Hello {username}, How are you?")    
        else :
            print(len(username)/0)
    except :  
        print("Enter a Valid Username - ")  
        main()

# def main():
#     username = input("Enter a Username - ")
#     if len(username) > 3 :
#         print(f"Hello {username}, How are you?") 
#     else :
#         main()    

if __name__ == "__main__":
    main()


                

