#ONLINE BANKING SYSTEM

print("Welcome The Dulanto Bank!")
username="dulanto2004"
passworduser="danieldulanto"
cont=0
balance=2000.0
valor=False
while(cont<3 and valor!=True):
    user=input("Enter your username:")
    password=input("Enter your password:")
    if username==user and password==passworduser:
        valor=True
    else:
        print ("You're wrong! Come back to enter\n")
        cont+=1
if valor:
    print("What do you want?:\n1 Deposite\n2 Withdraw\n3 View\n4 Transfer money\n")
    display=int(input("Insert the number you want to do:"))
    if display==1:
        amount=float(input("Enter the amount you want to deposit: "))
        balance+=amount
        print("Your new balance is:")
        print(balance)
    elif display==2:
        withdraw=float(input("Enter the amount to withdraw:"))
        if withdraw<=balance:
            balance-=withdraw
            print("You have withdrawn: ")
            print(withdraw)
            print("\nYour new balance is: ")
            print(balance)
        else:
            print("You can't withdraw that amount of money")
    elif display==3:
        print("Your balance is: ")
        print(balance)
    elif display==4:
        user2=input("Enter to what user do you want to transfer money?")
        transfer=float(input("Enter the amount that you want to transfer:"))
        if transfer<=balance:
            balance-=transfer
            print("You have transferred to "+user2+" : ")
            print(transfer)
            print("\nYour new balance is: ")
            print(balance)
        else:
            print("You can't deposit that amount of money")
    else:
        print("Incorrect number!")
else:
    print("Sorry, come back later! ")    