"""mark=int(input())
if(mark>35):
    print("pass")
else:
    print("fail"
income=int(input("income:"))
if(income>7000):
    print("not eligible for scholarship")
else:   
 print("eligible for scholarship")
a=10
print(a/2)
b=11
print(b%2)
a=int(input("Enter a value:"))
if(a%3==0 and a%5==0):
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")
a= int(input("even or odd:"))
if(a%2==0):
    print("even")
else:
    print("odd")
score= int (input("Enter your score: "))
if(score<35):
    print("poor sudent")
elif(score>35 and score<70):
        print("average student")
elif(score>70 and score<100):
    print("good student")
else:
     print("invalid score")
a= int(input("a:"))
b= int(input("b:"))
operation= input("add/ sub/ mul/ div:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("invalid operation")
score= int(input("score precentage"))
if(score>=70):
    name= input("enter your name:")
    age=input("enter your age:")
    department=input("enter your department:")
    location=input("enter your location:")
    print("you are eligible for scholarship")
else:
    print("you are not eligible for scholarship")
salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))

if salary >= 20000 or age <= 25:
    loan = int(input("Enter the loan amount: "))
    
    if loan <= 50000:
        print("You are eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")"""
tamil=float(input("enter tamil mark:"))
english=float(input("enter english mark:"))
maths=float(input("enter maths mark:")) 
scinece=float(input("enter science mark:"))
social=float(input("enter social mark:"))
total=tamil+english+maths+scinece+social
average=total/5
print(f"total mark: {total}")
print(f"average mark: {average}")
if(average<=35):
    print("additional classes are required")
else:
    print("you are good to go")