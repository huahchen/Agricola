f = open('occ.txt', 'r')
f1e = open('1E.txt', 'w+')
f3e = open('3E.txt', 'w+')
f4e = open('4E.txt', 'w+')
f1i = open('1I.txt', 'w+')
f3i = open('3I.txt', 'w+')
f4i = open('4I.txt', 'w+')
f1k = open('1K.txt', 'w+')
f3k = open('3K.txt', 'w+')
f4k = open('4K.txt', 'w+')
line = "start"
while (line != ""):
    german = f.readline()
    english = f.readline()
    numPlayer = f.readline()
    deck = f.readline()
    concise = f.readline()
    description = f.readline()
    result = german + english + numPlayer + deck + concise + description + "\n"
    if str(numPlayer)[0] == '1':
        if str(deck)[0] == 'E':
            f1e.seek(0, 1)
            f1e.write(result) 
        if str(deck)[0] == 'I':
            f1i.seek(0, 1)
            f1i.write(result) 
        if str(deck)[0] == 'K':
            f1k.seek(0, 1)
            f1k.write(result) 
    if str(numPlayer)[0] == '3':
        if str(deck)[0] == 'E':
            f3e.seek(0, 1)
            f3e.write(result) 
        if str(deck)[0] == 'I':
            f3i.seek(0, 1)
            f3i.write(result) 
        if str(deck)[0] == 'K':
            f3k.seek(0, 1)
            f3k.write(result) 
    if str(numPlayer)[0] == '4':
        if str(deck)[0] == 'E':
            f4e.seek(0, 1)
            f4e.write(result) 
        if str(deck)[0] == 'I':
            f4i.seek(0, 1)
            f4i.write(result) 
        if str(deck)[0] == 'K':
            f4k.seek(0, 1)
            f4k.write(result) 
    line = f.readline()
f.close()
f1e.close()
f3e.close()
f4e.close()
f1i.close()
f3i.close()
f4i.close()
f1k.close()
f3k.close()
f4k.close()
