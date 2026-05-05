# 2, 4, 7, 10, 12....use function

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether 
# the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# def check_number(number):
#     if number%2==0:
#         text='even'
#     else:
#         text='odd'
#         return text
#     print(text)
# check_number(30)
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.
# def check_multiple(number):
#     if number%4==0:
#         text='divisible by 4'
#     else:
#         text='not divible by 4'
#         return text
#     print(text)
# check_multiple(40)

# TASK 4:Write a program which accepts email as form input or 
# from terminal. Validate the email by checking if it's a valid email. 
# def check_email(email):
#     if '@' in email and '.' in email:
#         text='Valid email'
#     else:
#         text='Invalid email'
#         return text
#     print(text)
# check_email('michellekabue@gmail.com')

# TASK 7:
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
def student_marks(marks):
    if marks >100:
        text='Invalid marks'
    elif marks >79:
        text='A'
    elif marks>=60:
        text='B'
    elif marks>=50:
        text='C'
    elif marks>=40:
        text='D'
    else:
        text='E'
        return text
    print(text)
student_marks(960)

# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

