'''
for loop
project-1-student-grade-tracker

'''
a=["gokul","rajesh","vinay"]
b=[50,60,40]
for i in range(len(a)):
    if b[i]<50:
        print(f"{a[i]} has failed and got only {b[i]}%")
    elif b[i]==50:
        print(f"{a[i]} got average mark of {b[i]}%")
    else:
        print(f"{a[i]} got decent {b[i]}%")
