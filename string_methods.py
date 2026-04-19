text="Software DEVELOPER"
#capitalize
text1=text.capitalize()
print(text1)

#casefold-remove case
text2=text.casefold()
print(text2)
#count-give number of apperarance of a character
text3=text.count("E")
print(text3)

#replace-old,new
text4=text.replace('DEVELOPER','engineer')
print(text4)
#Endswith and startswith return boolean
text5=text.endswith('R')
print(text5)
text6=text.startswith('S')
print(text6)
#lower
text7=text.lower()
print(text7)
#upper
text8=text.upper()
print(text8)

#strip-remove trailing and leading whitespace
text="   Software Developer   "
print(len(text))
text=text.strip()
print(len(text))
print(text)
#split-split a string using a character if the character is not provided it splits with space causing a list
email='michellekabue@gmail.com'
splitted=email.split('@')
print(splitted)

#cleanup
text="   jUnIoR deVelOper  "
text=text.strip()
text=text.capitalize()
print(text)
