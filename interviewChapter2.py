class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext
        

class LinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def addToHead(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def appendToTail(self, data):
        end = Node(data)
        if self.head is None:
            self.head = end
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(end)

    def deleteFirst(self):
        self.head = self.head.getNext()

    def size(self):
        current = self.head
        count = 0
        while(current is not  None):
            count = count+1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        while(current is not None):
            if(data == current.getData()):
                return True
            current = current.getNext()
        return False

    def printList(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

#2.1
def removeDups(linkList):
    seen = []
    current = linkList.head
    prev = None
    while current is not None:
        if current.getData() in seen:
            prev.setNext(current.getNext())
        else:
            seen.append(current.getData())
            prev = current
        current = current.getNext()

#without using an extra data structure
def removeDuplicates(linkList):
    current = linkList.head
    prev = current
    while current is not None:
        runner = current
        while runner.getNext() is not None:
            if ((runner.getNext()).getData() == current.getData()):
                runner.setNext(runner.getNext().getNext())
            else:
                runner = runner.getNext()
        current = current.getNext()

#2.2
#returns data in kth to last element
def findK(linkList, k):
    current = linkList.head
    count = 0
    while current is not None:
        count = count + 1
        current = current.getNext()
    current = linkList.head
    if k <= count:
        for i in range(count-k):
            current = current.getNext()
        return current.getData()

#recursive
def kthToLast(head, k):
    if (head is None):
        return 0
    index = kthToLast(head.getNext(), k) + 1
    if (index == k):
        print("kth to last element is " + str(head.getData()))
    return index

#2.3
def deleteMiddle(midNode):
    midNode.setData(midNode.getNext().getData())
    midNode.setNext(midNode.getNext().getNext())

#2.4
#partition a linked list around a value
def partition(linkList, value):
    newList = LinkedList()
    current = linkList.head
    while current is not None:
        if(current.getData() < value):
            newList.addToHead(current.getData())
        else:
            newList.appendToTail(current.getData())
        linkList.deleteFirst()
        current = linkList.head

    newList.printList()

#2.5
def addIntLists(list1, list2):
    l1curr = list1.head
    l2curr = list2.head

    #fill out linked list with 0's if need be
    while(l1curr.getNext() is not None or l2curr.getNext() is not None):
        if(l1curr.getNext() is None):
            list1.appendToTail(0)
        elif(l2curr.getNext() is None):
            list2.appendToTail(0)

        l1curr = l1curr.getNext()
        l2curr = l2curr.getNext()

    carryover = 0
    sumList = LinkedList()
    sumList.appendToTail(0)
    current = sumList.head

    l1curr = list1.head
    l2curr = list2.head

    #do that good good addition
    while(l1curr is not None):
        dataSum = l1curr.getData() + l2curr.getData() + carryover
        slotdata = dataSum % 10
        carryover = dataSum // 10

        sumList.appendToTail(slotdata)
        l1curr = l1curr.getNext()
        l2curr = l2curr.getNext()
        current = current.getNext()

    if carryover != 0:
        sumList.appendToTail(carryover)
        
    sumList.deleteFirst()
    sumList.printList()
        
#recursive
def addLists(l1, l2, carry):
    if (l1 is None and l2 is None and carry == 0):
        return None

    value = carry
    if l1 is not None:
        value += l1.getData()
    if l2 is not None:
        value += l2.getData()


    result = Node(value % 10)

    if l1 is not None or l2 is not None:
        more = addLists(None if l1 is None else l1.getNext(),
                        None if l2 is None else l2.getNext(),
                        1 if value >= 10 else 0)
        result.setNext(more)

    while result is not None:
        print(result.getData())
        result = result.getNext()

#2.6
def isPalindrome(linkList):
    reverseList = cloneReverse(linkList)
    return checkEqual(linkList, reverseList)

def cloneReverse(linkList):
    current = linkList.head
    newList = LinkedList()
    while current is not None:
        newList.addToHead(current.getData())
        current = current.getNext()

    return newList

def checkEqual(list1, list2):
    #know they'll be the same size but if we didn't we'd have to check
    l1 = list1.head
    l2 = list2.head
    while l1 is not None:
        if l1.getData() != l2.getData():
            return False
        l1 = l1.getNext()
        l2 = l2.getNext()
    return True

#2.7
def intersect(list1, list2):
    l1 = list1.getHead()
    l2 = list2.getHead()
    count1 = 0
    count2 = 0

    #if they ever intersect, the last nodes of each list will be equal to each other
    while l1 is not None:
        count1 = count1 + 1
        l1 = l1.getNext()

    while l2 is not None:
        count2 = count2 + 1
        l2 = l2.getNext()

    #no intersection
    if l1 != l2:
        return None

    if (count1 > count2):
        for i in range(count1-count2):
            list1.deleteFirst()
    elif(count2 > count1):
        for i in range(count2-count1):
            list2.deleteFirst()

    l1 = list1.getHead()
    l2 = list2.getHead()

    while l1 is not None:
        if l1 == l2:
            return l1
        l1 = l1.getNext()
        l2 = l2.getNext()

#2.8
def isALoop(linkList):
    slow = linkList.getHead()
    fast = linkList.getHead()
    collisionPoint = None
    start = True

    while fast.getNext() is not None and fast.getNext().getNext() is not None:
        if slow == fast:
            if start:
                start = False
            else:
                collisionPoint = fast
                slow = linkList.getHead()
                while slow != collisionPoint:
                    slow = slow.getNext()
                    collisionPoint = collisionPoint.getNext()
                return slow
        slow = slow.getNext()
        fast = fast.getNext().getNext()
        
    return None
    

def main():
    list1 = LinkedList()
    list2 = LinkedList()
    
    list1.appendToTail(1)
    list1.appendToTail(3)
    list1.appendToTail(5)

    list2.appendToTail(1)
    list2.appendToTail(3)
    list2.appendToTail(5)

    addIntLists(list1, list2)
    #addLists(list1.getHead(), list2.getHead(), 0)

main()
