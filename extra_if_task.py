#1.
#Write a program that checks login credentials:
#"Access granted" if email = "admin@gmail.com" and password = "Admin@123"
#"Wrong password" if email is correct but password is wrong
#"Email not found" otherwise
email=input('Enter email :')
password=input('Enter password :')
correct_email='admin@gmail.com'
correct_password='Admin@123'
if email==correct_email and password==correct_password:
    print('Access granted')
elif email==correct_email and password!=correct_password:
    print('Wrong password')
else:
    print('Email not found')
#2.
#Create a program that validates an email:
#"Invalid email" if it does not contain "@" or "."
#"Gmail account" if it ends with "@gmail.com"
#"Other email provider" otherwise
email=input('Enter email')
if '@' not in email or '.' not in email:
    print('Invalid email')
elif  email.endswith('@gmail.com'):
    print('Gmail account')
else:
    print('Other email provider')
#3.
#Write a program that checks password strength:
#"Weak" if length < 6
#"Moderate" if length 6–10 and contains at least one digit
#"Strong" if length > 10 and contains both digits and uppercase letters
password=input('Enter password')
if len(password)<6:
    print('Weak')
elif len(password)>=6 and len(password)<=10:
    print('moderate')
elif len(password)>10 and password!=password.isalpha() and password!=password.islower():
    print('strong')
else:
    print('Does not meet required strength')
#4.
#Write a program that checks a password:
#"Invalid" if it does not start with a capital letter
#"Invalid" if it does not end with a number
#"Valid password" otherwise
if password[0]!=password.isupper()
#5.
#Write a program that takes a number and checks:
#"Fizz" if divisible by 3
#"Buzz" if divisible by 5
#"FizzBuzz" if divisible by both
#Otherwise print the number
number=input('Enter number')
number=int(number)
if number % 3 ==0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 ==0:
    print('Buzz')

else:
    print('number')
#6.
#Create a program that takes a score and prints a grade:
#A (≥ 80)
#B (70–79)
#C (60–69)
#D (50–59)
#F (< 50)
score=input('Enter score')
score=int(score)
if score>=80:
    print('A')
elif score>=70 and score<=79:
    print('B')
elif score>=60 and score<=69:
    print('C')
elif score>=50 and score<=59:
    print('D')
else:
    print('F')
#7.
#Create a program that takes two numbers and prints:
#"Equal" if same
#"First is greater"
#"Second is greater"
num1=input('Enter first number')
num1=int(num1)
num2=input('Enter second number')
num2=int(num2)
if num1==num2:
    print('Equal')
if num1>num2:
    print('first is greater')
if num2>num1:
    print('second is greater')
#8.
#Write a program that takes a day number (1–7) and prints:
#Weekday (1–5)
#Weekend (6–7)
#Invalid input otherwise

#9.
#Create a program that takes a temperature and prints:
#"Freezing" if ≤ 0
#"Cold" if 1–15
#"Warm" if 16–30
#"Hot" if > 30
temp=int(temp)
if temp<=0:
    print('Freezing')
elif temp>=1 and temp<=15:
    print('Cold')
elif temp<=16 and temp>=30:
    print('Warm')
else:
    print('Hot')

#10.
#Create a program that takes a year and prints:
#"Leap year" if divisible by 4
#"Century year" if divisible by 100
#"Common year" otherwise
year=('Enter year')
year=int(year)
if year % 4 ==0:
    print('Leap year')
elif  year % 100==0:
    print('Century year')
else:
    print('Common year')