#Ryan Jones
#1/31/18

number = int(input('Enter a number: '))

if number%2==0 and number%3==0:
    print(number,'is divisible by both 2 and 3')
elif number%2==0:
    print(number,'is divisible by 2')
elif number%3==0:
    print(number,'is divisible by 3')
else:
    print(number,'is not divisible by either 2 or 3')