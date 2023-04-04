#WAP that prompts the user to enter a message. 
#Now count and print the number of occurrence to each character. 
string = input("Enter a message : ")
for i in range(0,len(string)):
    count = 0 
    for j in string:
        if(string[i]==j):
            count+=1
        
    print(string[i],count)