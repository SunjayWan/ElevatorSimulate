infname = input("name of the file you want to check:")
textdic = {}
result = []
textfile = open(infname)
for line in textfile:
    for word in line.split():
        textdic[word] = textdic.get(word,0) + 1
        if textdic[word] == 1:
            result.append(word)
textfile.close()
for i in sorted(result):
    print(i)


