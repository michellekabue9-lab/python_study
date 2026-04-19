#Create a new python file stringtask.py and attempt the 5 questions below:
#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
text='JOHn'
text=text.casefold()
print(text)
#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
text1='The Dog Breed is German Shepherd'
splitted=text1.split()[2:5]
print(' '.join(splitted))


#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
text2='Defeats for the Clinton forces, this was her moment of triumph'
splitted=text2.split()[3:5]
print(' '.join(splitted))
#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
text3='The lazy dog; ran so fast; it hit the wall.'
split_text=text3.split(';')
print(len(split_text))
#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name='  Joh.n  '
first_name=first_name.strip()
first_name=first_name.replace('.','')
print(first_name)
last_name='Do,e'
last_name=last_name.replace(',','')
print(last_name)
full_name=first_name+' '+last_name
print(full_name)
#Having the string r = '["E","W","C"]' #Manipulate it to display EWC