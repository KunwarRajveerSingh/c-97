intro = input('introduce yourself:-')
charcount = 0
wordcount = 1
for i in intro:
    charcount = charcount+1
    if(i==' '):
        wordcount = wordcount+1
print('total characters are', charcount)
print('total words are', wordcount)    