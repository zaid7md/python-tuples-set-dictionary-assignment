#WAP that accepts different number of arguments and returns sum of only the positive values passed to it.

a = int(input('Enter the size of list : '))
l = []
for i in range(a):
    c = int(input('Enter number : '))
    l.append(c)

sum = 0
for i in l :
    sum = sum + i

print("Sum =",sum)
