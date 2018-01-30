#Ryan Jones
#1/29/18

age = int(input('Enter your age: '))

if age > 15:
    print('You can watch R movies')
elif age > 12:
    print('You can watch PG-13 movies')
elif age > 6:
    print('You can watch PG movies')
else:
    print('You can watch G movies')