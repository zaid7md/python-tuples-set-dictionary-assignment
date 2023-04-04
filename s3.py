#WAP that creates two sets- squares and cubes in range 1-10.
# Demonstrate the use of update (), pop(), remove (), add(), and clear () function.


set1 = set()
for i in range(1,11):
    if i**2 >=1 and i**2 <=10:
        set1.add(i)
print('set1',set1)

set2 = set()
for i in range(1,11):
    if i**3 >=1 and i**3 <=10:
        set2.add(i)
print('set2',set2)

set1.update(set2)
print('update',set1)
set1.pop()
print('pop:',set1)
set1.remove(2)
print('remove',set1)
set1.add(10)
print('add',set1)
set1.clear()
print('clear',set1)