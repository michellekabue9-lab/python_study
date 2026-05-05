#1. write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age=input('What is your age')
age=int(age)
if age>=18:
    license=input('Do you have a license yes/no')
    if license=='yes':
        print('Eligible to vote')
    else:
        print('Not eligible to vote')
else:
    print('you are too young to drive')
# 2.Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

credit_score=input('Enter credit score')
credit_score=int(credit_score)
if credit_score>700:
    annual_income=input('Enter annual income')
    annual_income=int(annual_income)
    if annual_income>50000:
        print('Loan approved')
    else:
        print('income requirement not met')
else:
    print('Credit score too low')


