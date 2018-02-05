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
    miles = kilometers*0.621371
    print(miles, 'miles')

if choice == 2:
    kilograms = float(input('Enter number of Kilograms: '))
    pounds = kilograms*2.20462
    print(pounds, 'pounds')
    
if choice == 3:
    liters = float(input('Enter number of Liters: '))
    gallons = liters*0.264172
    print(gallons, 'gallons')

if choice == 4:
    celsius = float(input('Enter Degrees in Celsius: '))
    fahrenheit = celsius*1.8+32
    print(fahrenheit, 'degrees Fahrenheit')

if choice<1 or choice>4:
    print('No.')