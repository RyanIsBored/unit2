#Ryan Jones
#2/12/18
#quiz2.py

bothwords = input('Enter two words: ')
firstword, lastword = bothwords.split()

if (len(firstword))>(len(lastword)):
    print('The first word is longer')
if (len(firstword))<(len(lastword)):
    print('The second word is longer')
if (len(firstword))==(len(lastword)):
    print('The words are the same length')

if 'p' in firstword and 'p' in lastword:
    print('Both words have a p')
if 'p' not in firstword and 'p' in lastword:
    print('Only the second word has a p')
if 'p' in firstword and 'p' not in lastword:
    print('Only the first word has a p')

num1 = int(input('Enter two numbers that add up to 12 (first number): '))
num2 = int(input('Enter the second number that adds up to 12: '))
if num1+num2==12:
    print('Correct')
else:
    print('Incorrect')