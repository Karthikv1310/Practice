'''
if-else/nested if else condition
'''
'''Project-2-Customer-Feedback-System'''
#By default feedback 1,2,3,4,5
v,w,x,y,z=1,2,3,4,5
print("Customer Feedback")
a=int(input("Please enter your feedback on the scale of 5: "))
if a==1:
    print("Bad")
    n=input("Please provide your suggestion: ")
    if n=="":
        print("Provide suggestion")
        n=input("Please provide your suggestion: ")
        print("Do the process again")
        
    else:print("Thanks for your suggestion")
    
    
if a==2:
    print("Below Average")
    n1=input("Please provide your suggestion: ")
    if n1=="":
        print("Provide suggestion")
        n1=input("Please provide your suggestion: ")
        print("Do the process again")
        
    else:print("Thanks for your suggestion")
    
if a==3:
    print("Average")
    n2=input("Please provide your suggestion: ")
    if n2=="":
        print("Provide suggestion")
        n2=input("Please provide your suggestion: ")
        print("Do the process again")
        
    else:print("Thanks for your suggestion")
    
if a==4:
    print("Great")
    n2=input("Please provide your suggestion: ")
    if n2=="":
        print("Provide suggestion")
        n2=input("Please provide your suggestion: ")
        print("Do the process again")
        
    else:print("Thanks for your suggestion")
    
if a==5:
    print("Excellent")
    print("Thanks for your suggestion")

            
    
