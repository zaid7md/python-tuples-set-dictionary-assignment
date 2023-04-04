#WAP that has a nested list to store toppers details. Edit the details and reprint the details
details = [['student1','Maths',89],['student2','PPL',87],['student3','physics',80]]
print('Details :',details)
details[0][2]=92
print("Updated details :",details)

t = tuple(details)
print(t)