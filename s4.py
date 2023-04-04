#WAP that has a list of countries. Creates a set of the countries and print the name of the countries in sorted order
set_countries = set()
for i in range(0,5):
    i = input("Enter country : ")
    set_countries.add(i)

print(set_countries)

print(sorted(set_countries)) #returns a new sorted list form the elements of the set , it does not sorts the set 