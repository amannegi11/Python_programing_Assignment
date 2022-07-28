#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
n=float(input("Enter the number "))
if n<0:
    print("the number is Negative")
elif n>0:
    print("the number is positive")
else:
    print("the number is Zero")

#2. Write a Python Program to Check if a Number is Odd or Even?
num=int(input("Enter the number "))
if num%2==0:
    print("num is even")
else:
    print("num is odd")

#3. Write a Python Program to Check Leap Year?
year=int(input(" Enter the Year "))
if year%400==0 and year%100==0:
    print("The year {} is a leap year ".format(year))
elif year%4==0 and year%100!=0:
    print("The year {} is a leap year ".format(year))
else:
    print("The year {} is not a leap year".format(year))
#4. Write a Python Program to Check Prime Number?
Num=int(input(" Enter the number:- "))
if Num==1 or Num==2:
    print(f"{Num} is a prime number")
if Num>2:
    c=0
    for i in range(2,Num):
        if Num%i==0:
            c=1
    if c!=1:
        print(f'{Num} is prime number')
    else:
        print(f"{Num} is not prime number")

#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lst=[]
for i in range(1,10000):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
    if c!=1:
        lst.append(i)
print(lst)