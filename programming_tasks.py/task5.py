# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
num1=input('Enter first number')
num1=int(num1)
num2=input('Enter second number')
num2=int(num2)
num3=input('Enter third number')
num3=int(num3)
if num1>num2 and num1>num3:
    print('First number is largest')
elif num2>num1 and num2>num3:
    print('Second number is largest')
else:
    print('Third number is largest')