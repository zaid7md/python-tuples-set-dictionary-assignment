#WAP that has a dictionary of states and their codes. 
#Add another state in the pre-defined dictionary, print all the items in the dictionary
#and try to print code for a state that does not exist. Set a default value prior to printing. 

d = dict([('Delhi',1),('UP',2),('Los Santos',3),('Abu Dhabi',4)])
print(d)
d.update([('Ohio',5)])
print(d)
default_value = 0
print(d.get('Washington DC',default_value))