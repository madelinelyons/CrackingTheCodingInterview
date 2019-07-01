class Node:
    def __init__(self, key, data, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.data = value
        self.leftChild = lc
        self.rightChild = rc

        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def getRoot(self):
        return self.root

    def put(self, key, data):
        if (self.root is None):
            self.root = Node(key, data)
        else:
            self._put(key, data, self.root)
        self.size = self.size + 1

    def _put(self, key, data, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, data, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, data, parent=currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, data, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, data, parent=currentNode)

    def get(self, key):
        if self.root:
            found = self._get(key, self.root)
            if found:
                return found.data
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        

    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node is not None):
            print(str(node.data) + ' ') 
            self._printTree(node.left)
           
            self._printTree(node.right)


def main():
    tree = Tree()
    tree.put("F", 3)
    tree.put("B", 2)
    tree.put("A", 7)
    tree.put("E", 4)
    tree.put("G", 1)
    tree.put("H", 6)
    tree.put("C", 8)
    tree.put("D", 2)    
    tree.put("I", 4)

    
    print(tree.get("H"))

main()
        
