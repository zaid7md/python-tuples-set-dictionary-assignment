#WAP that creates two sets. One of even numbers in range 1-10 and the other has all composite number in range 1-20.
# Demonstrate the use all (), issuperset(), len(), and sum () sunction on the sets.


def composite(n):
    count =0 
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    
    if count == 2 :
        return False
    else:
        return True
    
set1 = set()
for i in range(1,11):
    set1.add(i)

print('set1 :',set1)

set2 = set()
for i in range(2,21):
    if(composite(i)):
        set2.add(i) 
    
print('set2 :',set2)

print(all(set1))
print(all(set2))
print(set1.issuperset(set2))
print(set2.issuperset(set1))
print(len(set1),len(set2))
print(set1.union(set2))