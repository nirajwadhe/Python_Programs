def main():
    list_of_num = []
    try :
        number = int(input("Enter a Number - "))
        while number!=0:
            number = int(input("Enter a Number -"))
            list_of_num.append(number)
    except Exception as e:
        print(e)
    three_sum(list_of_num)

def three_sum(list_num):
    for i in range(len(list_num)):
        for j in range(i+1,len(list_num)):
            for k in range(j+2,len(list_num)):
                if list_num[i]+list_num[j]+list_num[k]==0 :
                    print(f'Yes {list_num[i]},{list_num[j]},{list_num[k]} are triplets')

if __name__=="__main__":
    main()