#WAP that has a list of numbers (both positive and negative).
#Make a new tuple that has only positive values from this list
a = int(input("Enter szie of list : "))
l = []
for i in range(a):
    c = int(input("Enter number : "))
    l.append(c)

positive = []

for i in l :
    if i > 0:
        positive.append(i)

t = tuple(positive)
print("Positive tuple :",t)



