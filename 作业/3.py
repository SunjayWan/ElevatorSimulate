def text_stat(infname,statfile = None):
    statdic = {}
    num = 0
    textfile = open(infname)
    
    for line in textfile:
        wordlist = line.split()
        for word in wordlist:
            word = word.strip(",.:'!?()-_$/`~\"\\")
            if word == '':
                continue
            statdic[word] = statdic.get(word,0) + 1
            num += 1
    textfile.close()
    if statfile:
        outfile = open(statfile,"w")
        for word in sorted(statdic.keys()):
            outfile.write(word + "," + str(statdic[word]) + "\n")
        outfile.close()
    return statdic
    
def test(infname):
    textdict = text_stat(infname)
    result = [[]]
    num = max(textdict.values())
    count = 0
    for k,v in textdict.items():
        if v < num:
            num = v
            result.append([])
        result[len(result) - 1].append(str(k)+' '+str(v))
        count += 1
        if count == 20:
            break
    for i in result:
        for j in sorted(i):
            print(j)

