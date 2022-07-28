#1. Write a Python program to convert kilometers to miles?
kilometers=float(input("Enter the value"))
Miles=kilometers*0.621371
print(Miles)
#2. Write a Python program to convert Celsius to Fahrenheit?
Celsius=float(input("enter the value "))
Fahrenheit=(Celsius * 9/5) + 32
print(Fahrenheit)

#3. Write a Python program to display calendar?
 # importing calendar module
import calendar
# To take month and year input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# display the calendar
print(calendar.month(year, month))
#4. Write a Python program to solve quadratic equation?
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#5. Write a Python program to swap two variables without temp variable?
X=10
Y=11
X,Y=Y,X
print(X,Y)
