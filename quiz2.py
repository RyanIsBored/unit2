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