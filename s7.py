#WAP that creates two dictionaries. 
#One that stores conversion values from meter to centimeters, and other that stores values from 
#centimeters to meters.
m = int(input("Enter value in meter : "))
meter_convert = dict([('metre',m),('centimetre',m*100)])
print(meter_convert)

cm = int(input("Enter value in centimetre : "))
centimetre_convert = {'centimetre':cm,'metre':cm/100}
print(centimetre_convert)