#Ryan Jones
#1/30/18
#unitConverter.py

print('1) Kilometers to Miles')
print('2) Kilograms to Pounds')
print('3) Liters to Gallons')
print('4) Celsius to Fahrenheit')

choice = int(input('Choose a number: '))

if choice == 1:
    kilometers = float(input('Enter number of Kilometers: '))

if choice == 2:
    kilograms = float(input('Enter number of Kilograms: '))
    
if choice == 3:
    liters = float(input('Enter number of Liters: '))

if choice == 4:
    celsius = float(input('Enter Degrees in Celsius: '))

else:
    print('No.')