import random as rm

def gambler(goal,stake,bet):
    wins = 0
    losses = 0
    while stake>=0 or stake>=goal :
        gamble = rm.randint(0,1)
        if gamble==1 :
            wins+=1
            stake+=bet
        else :
            losses+=1  
            stake-=bet
    print(f"Wining % are - {(wins/(wins+losses))*100}")
    print(f"Lossing % are - {(losses/(wins+losses))*100}")
               
def main():
    try :
        goal = int(input("Enter a Goal to Achieve - "))
        stake = int(input("Enter a Stake - "))
        bet = int(input("Enter a bet - "))
    except Exception as e :
        print(e)
        return main()
    gambler(goal,stake,bet)

if __name__=="__main__":
    main()
