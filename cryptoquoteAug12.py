'''Cryptography Test
Aidan's puzzle
August 12, 2018'''

import random

file = 'C:\\Users\\Farrell Family\\Desktop\\wordlist.txt'

with open(file)as f:
    lst = []
    for line in f.readlines():
        lst.append([x for x in line.split()])
    wordlist = []
    for thing in lst:
        for word in thing:
            wordlist.append(word)
        

#print(wordlist[:10])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

puzzle = ['1','2','2',' ','3','4','5','6',\
          ' ','7','1','8','9',' ','1','6','9',\
          ' ','7','9','2','4','10','11',' ','12','4',\
          ' ','5','8']

letter = {'1':'a','2':'l','3':'y','12':'t',
          '8':'s','4':'o','5':'u','6':'r','7':'c','9':'e'}

'''Solution: "all your base are belong to us"???'''

def replace1(letterin,letterout,mylist):
    output = list(mylist)
    for i,thing in enumerate(output):
        if thing == letterin:
            output[i] = letterout
        else:
            output[i] = thing
    return output

def main():

    newpuzzle = list(puzzle)

    for thing in newpuzzle:
        if thing in letter:
            newpuzzle = replace1(thing,letter[thing],newpuzzle)
        elif thing == ' ':
            continue
        else:
            newletter = random.choice(alphabet)
            while newletter in letter:
                newletter = random.choice(alphabet)
            newpuzzle = replace1(thing,newletter,newpuzzle)
    output = ''
    for string in newpuzzle:
        output += string

    words = output.split()
    
    print(words)

main()
