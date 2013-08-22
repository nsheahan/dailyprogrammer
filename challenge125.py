import sys

#Assumes a commandline call of python-challenge125.py-targetfile
fileh = open(sys.argv[1], 'r')
text = fileh.read()
text = text.split()

wordcount = 0
lettercount = 0
wordlist = {}
for word in text:
    wordcount += 1
    lettercount += len(word)
    if word in wordlist:
        wordlist[word] += 1
    else:
        wordlist[word] = 1


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
    b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

key = keywithmaxval(wordlist)

print (("Statistics for " + fileh.name + ":"))
print(wordcount, " Words\n", lettercount, " Letters\n")
print("Most common word is: ", key, "\nIt appeared ", wordlist[key], " times")
