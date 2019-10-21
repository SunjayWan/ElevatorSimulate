def verb_dict(infname):
    textfile = open(infname)
    verbdict = {}
    for line in textfile:
        origin = line.split()[0]
        for word in line.split():
            verbdict[word] = origin
    textfile.close()
    return verbdict
def verb_count(infname):
    dic = verb_dict("verb.txt")
    textfile = open(infname)
    verbdict = {}
    for line in textfile:
        for word in line.split():
            if word in dic.keys():
                verbdict[word] = verbdict.get(word,0) + 1
    textfile.close()
    return verbdict
def test(n):
    dic = verb_count("text.txt")
    result = [[]]
    num = max(dic.values())
    count = 0
    for k,v in dic.items():
        if v < num:
            num = v
            result.append([])
        result[len(result) - 1].append(str(k)+' '+str(v))
        count += 1
        if count == n:
            break
    for i in result:
        for j in sorted(i):
            print(j)