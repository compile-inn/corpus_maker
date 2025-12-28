import re

def makeVerses(file):
    fhandle = open(file, "r")
    txt = fhandle.read()
    reg = "[0-9]+:[0-9]+:[0-9]+" # change this to split differently.
    counter = 0 
    lastCh = len(txt)
    corpus = []
    # making the iterator into a list helps accessing it by index.
    matchList = list(re.finditer(reg, txt))

    for match in matchList:
        #print(match.span())
        start = match.span()[0]
        try:
            nextMatch = matchList[counter + 1] # access the next match
            end = nextMatch.span()[0] # txt index of the last character before next match.
        except:
            end = lastCh # points to end of txt when there is no next match
        result = txt[start:end]
        corpus.append(result)
        counter += 1
    return corpus