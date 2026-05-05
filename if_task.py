#ake three inputs from a user, separately. Print the largest of the numbers.
  #  Hint: Determine what type of data is taken in as input.
  #take 4 inputs from a user separately.Print the largest of the numbers

num1=float(input('enter first number'))
num2=float(input('enter first number'))
num3=float(input('enter first number'))
num4=float(input('enter first number'))


if num1>num2 and num1>num3 and num1>num4:
     print(num1)
elif num2>num1 and num2>num3 and num2>num4:
     print(num2)
elif num3>num1 and num3>num2 and num3>num4:
     print(num3)
else :
     print(num4)

#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
balance=input('Enter balance')
balance=float(balance)
if balance<100:
     print('insufficient funds')
elif balance>=100 and balance<=1000:
     print('moderate balance')
else:
     print('High balance')
#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

number=input('Enter number')
number=int(number)
if number<10:
     print('small')
elif number>=10 and number<=50:
     print('medium')
else:
     print('large')
##4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
email=input('Enter email')
pasword=input('Enter password')
if email==correct_email and password==correct_password:
     print('Access granted')
else:
     print('Access')