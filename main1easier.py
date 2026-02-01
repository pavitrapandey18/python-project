import random 
computer=random.choice([-1,0,1])
youstr=input("Enter Your Choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"gun"}
you=youDict[youstr]

print(f"You chose:- {reverseDict[you]}\nComputer chose:- {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
elif you-computer==-1 or you-computer==2:
    print("You Win!")
else:
    print("you lose....")