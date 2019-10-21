##def text_stat(infname,*statfile):
##    worddict = {}
##    num = 0
##    textfile = open(infname)
##    
##    for line in textfile:
##        wordlist = line.split()
##        for word in wordlist:
##            word = word.strip(",.:'!?()-_$/`~\"\\")
##            if word == '':
##                continue
##            worddict[word] = worddict.get(word,0) + 1
##            num += 1
##    textfile.close()
##    if statfile:
##        statefile = statfile[0]
##        outfile = open(statefile,"w")
##        for word in sorted(worddict.keys()):
##            outfile.write(word + "," + str(worddict[word]) + "\n")
##        outfile.close()
##        return num,len(worddict)
##    else:
##        return worddict
##    
##def text_mostused20(infname):
##    textdict = text_stat(infname)
##    result = {}
##    for k,v in textdict.items():
##        result[v] = k
##    count = 0
##    for k in reversed(sorted(result.keys())):
##        print (result[k],k)
##        count += 1
##        if count == 20:
##            break
##text_mostused20("sun1.txt")
#
#
##
#class Time:
#    def __init__(self,hours,minutes,seconds):
#        self._hours = hours
#        self._minutes = minutes
#        self._seconds = seconds
#    def hours(self):
#        return self._hours
#    def minutes(self):
#        return self._minutes
#    def seconds(self):
#        return self._seconds
#    def __add__(self,another):
#        nseconds = (self._seconds + another._seconds)%60
#        nminutes = (self._minutes + another._minutes + (self._seconds + another._seconds)//60)%60
#        nhours = (self._hours + another._hours + (self._minutes + another._minutes 
#                                                  + (self._seconds + another._seconds)//60))%60
#        return Time(nhours,nminutes,nseconds)
#
#class Time2:
#    def __init__(self,seconds):


