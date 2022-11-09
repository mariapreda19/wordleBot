import random
import math

file = open("words_list.txt", 'r')

words_list = []
for line in file:
    words_list.append(line)
dim = 11454
n = dim

patterns = []
v = [0, 0, 0, 0, 0, 0]
while v[0] == 0:
    var = ""
    for i in range(1, 6):
        var += str(v[i])
    patterns.append(var)
    i = 5
    while i > 0 and v[i] == 2:
        v[i] = 0
        i -= 1
    v[i] += 1

letter_freq = [[0, 0, 0, 0, 0] for i in range(26)]
for word in words_list:
    for i in range(5):
        letter_freq[ord(word[i])-65][i] += 1

file.close()

#functiile pentru joc

def pattern(pickedWord, guessWord):
    res = ['0'] * 5
    for i in range(5):
        if guessWord[i] == pickedWord[i]:
            res[i] = '2'
            pickedWord = pickedWord[:i] + "#" + pickedWord[i+1:]
            guessWord = guessWord[:i] + "@" + guessWord[i+1:]
        else:
            res[i] = '!'
    for i in range(5):
        if res[i] == '2':
            continue
        ind = pickedWord.find(guessWord[i])
        if ind != -1:
            res[i] = '1'
            pickedWord = pickedWord[:ind] + "#" + pickedWord[ind+1:]
        else:
            res[i] = '0'
    return "".join(res)


#functiile pentru jucator

#def guess():


def filter_words_pattern(guessWord, givenPattern):
    aux = []
    for index in range(len(words_list)-1, -1, -1):
        word = words_list[index]
        #pattern1 = pattern(guessWord, word)
        ok = 0
        if word == "SPRAY":
            print("#")
        for i in range(5):
            if givenPattern[i] == "2" and word[i] != guessWord[i]:
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list[len(words_list) - 1], words_list[index] = words_list[index], words_list[len(words_list) - 1]
                #words_list.pop()
                ok = 1
            if givenPattern[i] == "1" and word.find(guessWord[i]) == -1:
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list[len(words_list) - 1], words_list[index] = words_list[index], words_list[len(words_list) - 1]
                #words_list.pop()
                ok = 1
            if givenPattern[i] == "0" and word.find(guessWord[i]) != -1:
                #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
                #words_list.pop()
                ok = 1
        if ok == 0:
            #words_list[index], words_list[len(words_list) - 1] = words_list[len(words_list) - 1], words_list[index]
            #words_list.pop()
            aux.append(word)
    words_list.clear()
    for i in range(len(aux)):
        words_list.append(aux[i])

def entropy(guessWord):
    events = {possible_pattern: 0 for possible_pattern in patterns}
    for word in words_list:
        current_pattern = pattern(guessWord, word)
        events[current_pattern] += 1
    res = 0
    for possible_pattern in patterns:
        if events[possible_pattern] == 0:
            continue
        prob = events[possible_pattern] / len(words_list)
        res -= prob * math.log2(prob)
    return res

#se poate face si pe litere entropia
#si se aduna informatia de pe fiecare litera


#distribution closer to flat <=> higher entropy
#corpus = words_list
#numar de cate ori apare fiecare litera pe fiecare pozitie
#cand apare A cu galben, caut mai intai cuv in care apare A pe poz cu nr aparitii maxim
#picked_word = words_list[random.randint(0, dim-1)]
#print ("Cuvantul care trebuie ghicit este:", picked_word)
#print (pattern("elegy", "eerie"))

#print (entropy("TAREI"), end="\n")
#print (entropy("TARIE"), end="\n")

'''
#calc cu epsilon
maxim = -100000
sol_list = []
sol_dict = {}
for word in words_list:
    val = entropy(word)
    sol_dict[word] = val
    if val > maxim:
        maxim = val
        sol_list.clear()
        sol_list.append(word)
    else:
        if val == maxim:
            sol_list.append(word)
print (sol_dict)
'''

#picked_word = words_list[random.randint(0, dim-1)]
picked_word = "SPRAY"
print (picked_word)

pattern1 = pattern(picked_word, "TARIE")
filter_words_pattern("TARIE", pattern1)
print ("TARIE", end="\n")
print (words_list)
if picked_word not in words_list:
    print("nu mai e")

sol = "@@@@@"

while pattern(picked_word, sol) != "22222":
    maxim = -1
    sol = "@@@@@"
    for word in words_list:
        val = entropy(word)
        if val > maxim:
            maxim = val
            sol = word
    print(words_list)
    if len(words_list) == 0:
        break
    if len(words_list) == 1:
        print (words_list[0])
        break
    print(sol)
    current_pattern = pattern(picked_word, sol)
    filter_words_pattern(sol, current_pattern)
    if picked_word not in words_list:
        print("nu mai e")

print (sol)