f = open('minor.txt', 'r')
fe = open('E.txt', 'w+')
fi = open('I.txt', 'w+')
fk = open('K.txt', 'w+')
line = "start"
while line != "":
    german = f.readline()
    english = f.readline()
    deck = f.readline()
    prereq = f.readline()
    cost = f.readline()
    vp = f.readline()
    concise = f.readline()
    description = f.readline()
    result = german + english + deck + prereq + cost + vp + concise + description + "\n"
    if str(deck)[0] == 'E':
        fe.seek(0, 1)
        fe.write(result)
    if str(deck)[0] == 'I':
        fi.seek(0, 1)
        fi.write(result)
    if str(deck)[0] == 'K':
        fk.seek(0, 1)
        fk.write(result)
    line = f.readline()
f.close()
fe.close()
fi.close()
fk.close()
