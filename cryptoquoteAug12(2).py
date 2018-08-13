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

N_DICTS=10
POP_N = []

#find highest number of letter
highest = 0
for number in puzzle:
    if number == ' ':
        continue
    if int(number) > highest:
        highest = int(number)

def generateDict():
    '''generate a replacements dict'''
    replacements = {}
    for i in range(highest):
        new_replacement = random.choice(alphabet)
        while new_replacement in replacements.values():
            new_replacement = random.choice(alphabet)
        replacements[str(i + 1)] = new_replacement
    return replacements

def scoreDict(d):
    '''Scores a replacement dict according to how
    many words are in the wordlist'''
    newpuzzle = list(puzzle)
    #replace numbers with letters
    for thing in newpuzzle:
        if thing in d:
            newpuzzle = replace1(thing,d[thing],newpuzzle)
        elif thing == ' ':
            continue
        else:
            newletter = random.choice(alphabet)
            while newletter in d.values():
                newletter = random.choice(alphabet)
            newpuzzle = replace1(thing,newletter,newpuzzle)
    score = 0
    newpuzzle = convertDict(newpuzzle)
    for word in newpuzzle:
        if word in wordlist:
            score += 1
    return score,newpuzzle

def mutateDict(r):
    '''replaces letters in replacement dict'''
    #output = dict(replacements)
    num = random.randint(1,5)#highest)
    for i in range(1):
        ind = str(random.randint(1,highest))
        new_replacement = random.choice(alphabet)
        while new_replacement in r.values():
            new_replacement = random.choice(alphabet)
        r[ind] = new_replacement
    return r

def replace1(letterin,letterout,mylist):
    '''replaces mystery number with corresponding letter'''
    output = list(mylist)
    for i,thing in enumerate(output):
        if thing == letterin:
            output[i] = letterout
        else:
            output[i] = thing
    return output

def main():
    global POP_N
    high_score = 0
    newpuzzle = list(puzzle)
    for i in range(N_DICTS):
            newDict = generateDict()
            POP_N.append(newDict)

    while True:
        
        #firstDict = random.choice(POP_N) #first dict
        POP_N.sort(key=scoreDict)
        '''for a in POP_N:
            print(scoreDict(a),end=',')'''
        bestDict = POP_N[-1]
        POP_N = POP_N[-N_DICTS:]

    
        high_score,bestpuzzle = scoreDict(bestDict)
        '''pool = random.sample(POP_N,10)
        for n in pool:
            new = mutateDict(n)
            pool.remove(n)
            pool.append(new)
        POP_N += pool'''
        newDict = mutateDict(bestDict)
        newscore,newpuzzle = scoreDict(newDict)
        #print("High:",high_score,"new:",newscore)
        if newscore <= high_score:
            continue
        
        #words = convertDict(bestpuzzle)
        print(bestpuzzle,high_score)
        bestDict = dict(newDict)
        high_score = newscore
        if high_score >= len(newpuzzle):
            break
    

def convertDict(newpuzzle):
    #convert to list of words

    output = ''
    for string in newpuzzle:
        output += string

    words = output.split()

    return words

main()
