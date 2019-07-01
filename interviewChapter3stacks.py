class SNode:
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
        

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        item = self.top.getData()
        self.top = self.top.getNext()
        return item

    def push(self, item):
        node = SNode(item)
        node.setNext(self.top)
        self.top = node

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.getData()

    def isEmpty(self):
        return self.top is None

    def getTop(self):
        return self.top

    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def printStack(self):
        current = self.top
        while current is not None:
            print(current.getData())
            current = current.getNext()

class StackOfStacks:
    def __init__(self, threshold):
        self.top = None                 #top is a StackNode. 
        self.threshold = threshold
        self.numStacks = 0

    def pop(self):
        if self.top is None:
            raise Exception("Stack of stacks is empty")
        item = self.top.top.getData()
        if(self.top.top.getNext() is None):
            self.top = self.top.getNext()
        else:
            self.top.top = self.top.top.getNext()
            self.top.removeCount()
        return item

    def push(self, item):
        if self.top is None:
            newStack = StackNode(0)
            self.top = newStack
        
        if self.top.getCount() >= self.threshold:
            lastIndex = self.top.getIndex()
            newStack = StackNode(lastIndex + 1)
            newStack.setNext(self.top)
            self.top = newStack
            
        newNode = SNode(item)
        newNode.setNext(self.top.top)
        self.top.top = newNode
        self.top.updateCount()

    def popAt(self, index):
        if self.top is None:
            raise Exception("Stack of stacks is empty")
        current = self.top
        while current is not None:
            if current.getIndex() == index:
                item = current.top.getData()
                if(current.top.getNext() is None):
                    current = current.getNext()
                else:
                    current.top = current.top.getNext()
                    current.removeCount()
                return item
            current = current.getNext()

        return None


class StackNode:
    def __init__(self, index):
        self.count = 0
        self.index = index
        self.top = None
        self.next = None

    def getIndex(self):
        return self.index

    def updateCount(self):
        self.count = self.count + 1
    def removeCount(self):
        self.count = self.count - 1

    def getCount(self):
        return self.count

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next

class MyQueue:
    def __init__(self):
        self.newestStack = Stack()
        self.oldestStack = Stack()

    def size(self):
        return self.newestStack.size() + self.oldestStack.size()
    
    def add(self, value):
        self.newestStack.push(value)

    def shiftStacks(self):
        if self.oldestStack.isEmpty():
            while not self.newestStack.isEmpty():
                self.oldestStack.push(self.newestStack.pop())

    def peek(self):
        self.shiftStacks() #make sure oldestStack has the elements it cares about
        return self.oldestStack.peek()

    def remove(self):
        self.shiftStacks()
        return self.oldestStack.pop()

def sortStack(stack):
    bufferStack = Stack()
    size = stack.size()
    notInPlace = stack.size()
    currMax = 0
    maxNode = None
    for i in range(size):
        for i in range(notInPlace):
            if stack.getTop().getData() > currMax:
                currMax = stack.getTop().getData()
                maxNode = stack.getTop()
            item = stack.pop()
            bufferStack.push(item)

        stack.push(maxNode.getData())

        notInPlace = notInPlace - 1

        for i in range(notInPlace):
            if bufferStack.getTop().getData() == currMax:
                bufferStack.pop()
            item = bufferStack.pop()
            stack.push(item)

        currMax = 0
        maxNode = None


def main():
    stack = Stack()
    stack.push(10)
    stack.push(4)
    stack.push(28)
    stack.push(6)
    stack.push(14)

    sortStack(stack)
    stack.printStack()
    

    


main()
        
