days=('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
print(days[3])
print(days[2:5])
#Display Wed
print(days[2])
#Display mon to thur
print(days[0:4])

#convert tuple to list using list
days=list(days)
days.append('Jan')
print(days)
days=tuple(days)