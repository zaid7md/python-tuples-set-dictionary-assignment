#WAP that generate a set of prime numbers and another set of odd numbers. 
#Demonstrate the results of union, intersection, difference, and symmetric difference operation on these sets

def prime(n):
    count =0 
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    
    if count == 2 :
        return True
    else:
        return False

prime_set = set()
for i in range(2,101):
    if(prime(i)):
        prime_set.add(i) 

odd_set = set()

for j in range(1,101,2):
    odd_set.add(j)

print('Prime set :',prime_set)
print()
print('Odd set :',odd_set)
print()
        

print('Union',prime_set.union(odd_set))
print()
print('Intersection',prime_set.intersection(odd_set))
print()
print('Difference',prime_set.difference(odd_set))
print()
print('Symmetric differnce',prime_set.symmetric_difference(odd_set))