#1. Write a Python Program to Find the Factorial of a Number?
n=int(input("Enter the number "))
Num=n
for i in range(n-1,1,-1):
    n*=i

print(f"{n} is factorial of {Num}")


#2. Write a Python Program to Display the multiplication Table?
N=int(input("Enter the number "))
for i in range(1,11):
    print(f"{N}X{i}={N*i}")
#3. Write a Python Program to Print the Fibonacci sequence?
def Fibonacci(n):
        a = 0
        b = 1
        output = []
        for i in range(n):
            output.append(a)

            a, b = b, a + b

        return output
print(Fibonacci(9))

#4. Write a Python Program to Check Armstrong Number?
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#5. Write a Python Program to Find Armstrong Number in an Interval?
# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

    # order of number
    order = len(str(num))

    # initialize sum
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
#6. Write a Python Program to Find the Sum of Natural Numbers?
number=int(input('Enter the number '))
if number<0:
    print("please enter positive number ")
else:
    sum=0
    while number>0:
        sum+=number
        number-=1
    print(f"the sum of  natural number is {sum} ")