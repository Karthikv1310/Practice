'''
if condition
'''
'''Project-4-Check Password Strength'''
i=input("Enter your password to check its strength/length: ")
if len(i)>=8:
    print("Strong Password")
if len(i)<8:print("Weak Password")
