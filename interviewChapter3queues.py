class QNode:
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

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def getFirst(self):
        if self.first is None:
            raise Exception("Queue is empty")
        return self.first

    def getLast(self):
        if self.first is None:
            raise Exception("Queue is empty")
        return self.last

    def add(self, item):
        node = QNode(item)
        if self.last is not None:
            self.last.next = node    
        self.last = node
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            raise Exception("Queue is empty")
        data = self.first.getData()
        self.first = self.first.getNext()
        if self.first is None:
            self.last is None
        return data

    def peek(self):
        if self.first is None:
            raise Exception("Queue is empty")
        return self.first.getData()

    def isEmpty(self):
        return self.first is None

    def printQueue(self):
        current = self.first
        while current is not None:
            print(current.getData())
            current = current.getNext()

def combineQueues(queue1, queue2):
    while not queue2.isEmpty():
        queue1.add(queue2.getFirst().getData())
        queue2.remove()
    return queue1

def dequeueAny(queue):
    queue.remove()

def dequeueCat(queue):
    current = queue.getFirst()
    otherPetQ = Queue()
    
    while current is not None:
        if current.getData() != "cat":
            otherPetQ.add(current.getData())
            queue.remove()
        else:
            cat = queue.remove()
            if not otherPetQ.isEmpty():
                queue = combineQueues(otherPetQ, queue)
            return queue
        current = current.getNext()

def dequeueDog(queue):
    current = queue.getFirst()
    otherPetQ = Queue()
    
    while current is not None:
        if current.getData() != "dog":
            otherPetQ.add(current.getData())
            queue.remove()
        else:
            cat = queue.remove()
            if not otherPetQ.isEmpty():
                queue = combineQueues(otherPetQ, queue)
            return queue
        current = current.getNext()

def main():
    queue = Queue()
    queue.add("cat")
    queue.add("dog")
    queue.add("bird")
    queue.add("cat")
    queue.add("dog")
    queue.add("cat")
    queue.add("cat")
    queue.add("dog")

    queue = dequeueDog(queue)
    queue.printQueue()



main()
