#WAP to swap two values using tuple assignment
a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
print ("a =",a, "b =",b)
(a,b)=(b,a)
print("a =",a, "b =",b)