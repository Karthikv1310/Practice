'''
if-elsenested if else condition
'''
'''Project-2-ATM'''
#By default pin is:1234 and card swipe position #-- and balance 20000
p=1234
ca="#--"
ba=20000
print("Welcome to KPKP Bank!")
m=input("Please swipe your card: ")
if m!=ca:
    print("Incorrectly card has been swipped")
else:
    print("What do you want to do?")
    a=int(input("1. Deposite 2.Withdrawl: "))
    if a==1:
        p1=int(input("Please enter your pin: "))
        if p1 ==p:
            print("Success")
            x=int(input("How much you want to deposit: "))
            if x>10000:
                print("Limit Exceeded cant deposite more than 100000")
            else:print("Done, Thank you, pls take you card")
        else:
            print("Incorrect pin, pls take your card")
    if a==2:
        p2=int(input("Please enter your pin: "))
        if p2==p:
            print("Success")
            y=int(input("How much you want to withdrawl: "))
            if y>20000:
                print("Withdrawl Exceeded balance")
            else:print("Done, Thank you, pls take you card")
        else:
            print("Incorrect pin, pls take your card")
            
    
