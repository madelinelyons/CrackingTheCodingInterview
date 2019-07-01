#1.1
def isUnique(s1):
    s1 = s1.lower()
    charList = []
    charList = [0 for x in range(26)]
    for i in range(len(s1)):
        index = ord(s1[i]) - 97 #a = 0, b = 1, etc
        charList[index] = charList[index] + 1
        if charList[index] > 1:
            return False
    return True

print(isUnique("asdflkjgsd"))

#1.2
#1st attempt- wrong because a word that contains the letters of the other string
#might not contain all of them. could have duplicate letters

'''
def CheckPerm(s1, s2):
    if(len(s1) != len(s2)):
        return False
    for i in range(len(s1)):
         if(s1[i] not in s2):
            return False

    return True


print(CheckPerm("taco", "taaa"))
'''

def CheckPerm(s1, s2):
    countS1 = CountEachElement(s1)
    countS2 = CountEachElement(s2)

    if (countS1 == countS2):
        return True
    else:
        return False

def CountEachElement(s):
    count = {}
    for i in range(len(s)):
        if(s[i] not in count):
            count[s[i]] = 1
        else:
            count[s[i]] = count[s[i]] + 1

    return(count)

#print(CheckPerm("porcupine", "orcupnipe"))

#1.3
def URLify(s):
    s = s.replace(" ", "%20")
    print(s)

#URLify("Mr John Smith")

#1.4
def PalinPerm(s):
    s = s.replace(" ", "")
    countList = CountEachElement(s)

    numOdd = 0
    for x in countList:
        if(countList[x] % 2 != 0):
            numOdd+= 1

    return(numOdd <= 1)

#print(PalinPerm("rarecac"))

#1.5
def oneAway(s1, s2):
    if(abs(len(s1) - len(s2))>1):
        return False

    if(len(s1)==len(s2)): #replacement
        differenceFound = False
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                if(differenceFound):
                    return False
                else:
                    differenceFound = True
        return True

    else: #insertion or deletion
        if(len(s1)>len(s2)):
            return(oneEditInsert(s1, s2))
        if(len(s1)<len(s2)):
            return(oneEditInsert(s2, s1))

def oneEditInsert(s1, s2):
    index2 = 0
    while (index2 < len(s2)):
        if (s1[index2] != s2[index2]):
            newStr = s1.replace(s1[index2], "")
            return(newStr == s2)

        index2+=1
    return(True)

#print(oneAway("pale","ale"))

#1.6
def StrComp(s1):
    compAccum = ""
    curLetter = s1[0]
    curAccum = 1

    for i in range(1, len(s1)):
        if(len(compAccum)>len(s1)):
            return s1

        if(s1[i] != curLetter):
            compAccum = compAccum + curLetter + str(curAccum)
            curLetter = s1[i]
            curAccum = 1
        else:
            curAccum = curAccum + 1

    compAccum = compAccum + curLetter + str(curAccum)

    if(len(compAccum) <len(s1)):
        return compAccum
    else:
        return s1
    
#print(StrComp("aabbcccdd"))

#1.7
def rotateMatrix(M):
    if (len(M) != len(M[0]) or len(M) == 0):
        return False

    n = len(M)

    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = M[first][i]
            M[first][i] = M[last - offset][first]
            M[last-offset][first] = M[last][last-offset]
            M[last][last-offset] = M[i][last]
            M[i][last] = top

    return(M)

#print(rotateMatrix([[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33]]))

#1.8
def zeroMatrix(M):
    #copy matrix M into new matrix
    zeroM = [[0 for x in range(len(M))] for y in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M)):
            zeroM[i][j] = M[i][j]

    #if entry is 0, overwrite everywhere u're supposed to. (does lots of duplicate work)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if (M[i][j]==0):
                for k in range(len(M)):
                    zeroM[k][j] = 0
                for k in range(len(M[0])):
                    zeroM[i][k] = 0
                    
    return(zeroM)

#better way: 2 arrays keeping track of rows and columns with 0's then build it

def zeroMatrix2(M):
    zeroXlocation = []
    zeroYlocation = []

    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                zeroXlocation.append(i)
                zeroYlocation.append(j)

    for n in range(len(zeroXlocation)):
        for i in range(len(M)):
            M[i][zeroYlocation[n]] = 0
        for j in range(len(M[0])):
            M[zeroXlocation[n]][j] = 0

    return(M)

#print(zeroMatrix2([[2,4,1],[1,0,2],[1,3,2],[1,8,9]]))

#1.9
def rotationSub(s1, s2):
    rotS = s1
    for i in range(len(s1)):
        if (rotS == s2):
            return True
        rotS = rotate(rotS)
        print(rotS)

    return False

def rotate(s):
    newS = s[1:len(s)] + s[0]
    return newS

#print(rotationSub("erbottlewat", "waterbottle"))

#heckin clever book way
def rotationSub2(s1, s2):
    s1twice = s1 + s1
    if s2 in s1twice:
        return True
    else:
        return False

#print(rotationSub2("erbottlewat", "waterbottle"))
