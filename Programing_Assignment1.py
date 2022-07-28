# 1. Write a Python program to print "Hello Python"?
print("Hello Python")
# 2. Write a Python program to do arithmetical operations addition and division.?
A=4
B=8
# Addition
print(A+B)
# Division
print(A/B)
# 3. Write a Python program to find the area of a triangle?
# Three sides of the triangle is a, b and c:

a = float(input('Enter first side: '))

b = float(input('Enter second side: '))

c = float(input('Enter third side: '))
 # calculate the semi-perimeter.

s = (a + b + c) / 2

   # calculate the area.

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)



# 4. Write a Python program to swap two variables?
X=10
Y=11
   # create a temporary variable and swap the values
tem=X
X=Y
Y=tem
print(X,Y)


# 5. Write a Python program to generate a random number?
import random
n = random.randint(0,11)
print(n)