#5.1
def strInsert(N, M, i, j):
    long = str(N)
    new = long[:-j] + str(M) + long[-2:]
    return int(new)

#print(strInsert(1000000000, 10111, 2, 6))

def insert(N, M, i, j):
    ones = ~0
    left = ones << (j+1)
    right = (1<<i) - 1
    mask = left | right
    clearN = N & mask
    Mshifted = M << i

    return bin(clearN | Mshifted)

#print(insert(1000000000, 11101, 2, 6))

#5.2
def floatToBin(num):
    accum = "."
    remaining = num

    for i in range(1,32):
        if remaining >= pow((1/2), i):
             accum = accum + "1"
             remaining = remaining - pow(1/2, i)
        else:
            accum = accum + "0"

        if remaining == 0:
            return accum

    return "ERROR"

#print(floatToBin(.0625))

#5.3
def bitFlip(num):
    curCount = 0
    max = 0
    seenZero = False
    s = str(num)
    index = 0
    goback = 0

    while index < len(s):
        if s[index] == "1":
            curCount += 1
        elif s[index] == "0" and not seenZero:
            curCount += 1
            seenZero = True
            if index != (len(s)-1):
                goback = index
        elif s[index] == "0" and seenZero:
            if curCount > max:
                max = curCount
            curCount = 0
            seenZero = False
            index = goback
        index = index + 1

    return max

#print(bitFlip(011011101110111001110))

#5.4
def nextNums(num):
    index = len(num) - 1
    swapSmall = False
    swapBig = False
    small = num
    big = num
    
    while index >= 0:
        if num[index] == "1":
            if not swapSmall and index != (len(num) - 1):
                if num[index + 1] == "0":
                    small = small[:index] + "01" + small[index+2:]
                    swapSmall = True
            if not swapBig and index != 0:
                if num[index - 1] == "0":
                    big = big[:index-1] + "10" + big[index+1:]
                    swapBig = True

            if swapSmall and swapBig:
                break

        index = index - 1

    return small, big

def getNext(num):
    c = num
    c0 = 0
    c1 = 0
    while(((c & 1) ==0) and (c != 0)):
        c0 += 1
        c >>= 1

    while((c&1) == 1):
        c1 += 1
        c >>= 1

    if(c0 + c1 == 31 or c0 + c1== 0):
        return -1

    p = c0 + c1

    num |= (1 << p)
    num &= ~((1 << p) - 1)
    num |= (1 << (c1 -1)) - 1

    return bin(num)
    
def getPrev(num):
    temp = num
    c0 = 0
    c1 = 0
    while (temp & 1 == 1):
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1

    while((temp&1) == 0) and (temp != 0):
        c0 += 1
        temp >>= 1

    p = c0 + c1
    num &= ((~0) << (p + 1))

    mask = (1 << (c1 + 1)) - 1
    num |= mask << (c0 - 1)

    return bin(num)

#print(nextNums("0100000"))
print(bin(48))
print(getNext(48))
print(getPrev(48))
        

#5.6

def conversion(n1, n2):
    differences = 0
    while n1 > 0 or n2 > 0:
        if n1 % 2 == 1 and n2 % 2 == 0 or n1 % 2 == 0 and n2 % 2 == 1:
            print(bin(n1))
            print(bin(n2))

            differences += 1

        n1 = n1 >> 1
        n2 = n2 >> 1

    return differences

def conversion2(n1, n2):
    differences = 0
    c = n1^n2
    while c != 0:
        differences = differences + (c & 1)
        c = c >> 1

    return differences

#print(conversion2(29,15))

#5.7

def swapPairs(num):
    print(str(bin(num)))
    evens = num & (0xaaaaaaaa)
    odds = num & (0x55555555)
    evens = evens >> 1
    odds = odds << 1
    
    return bin(evens | odds)

#print(swapPairs(135))

#5.8, does not work

def drawLine(byteArray, width, x1, x2, y):
    startOffset = x1 % 8
    firstFullByte = int(x1 / 8)
    if startOffset != 0:
        firstFullByte += 1

    endOffset = x2 % 8
    lastFullByte = int(x2 / 8)
    if endOffset != 7:
        lastFullByte -= 1

    for b in range(firstFullByte, lastFullByte):
        byteArray[int(width/8) * y + b] = (0xff)

    startMask = ((0xff) >> startOffset)
    endMask = ~((0xff) >> (endOffset + 1))

    if (x1 / 8) == (x2 / 8):
        mask = (startMask & endMask)
        byteArray[int(width / 8) * y + int(x1 / 8)] |= mask
    else:
        if startOffset != 0:
            byteNumber = int(width / 8) * y + firstFullByte - 1
            byteArray[byteNumber] |= startMask
        if endOffset != 7:
            byteNumber = int(width / 8) * y + lastFullByte + 1
            byteArray[byteNumber] |= endMask


#drawLine([5,2,3,1,6,5,8,3,5,7,4,7,5,3,2,8,5,2,3,1,6,5,8,3,5,7,4,7,5,3,2,8,5,2,3,1,6,5,8,3,5,7,4,7,5,3,2,8,5,2,3,1,6,5,8,3,5,7,4,7,5,3,2,8], 32, 0, 16, 4)
    
