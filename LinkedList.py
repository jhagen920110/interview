# this code insert node to the first

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getCurrent(self):
        return self.data

    def getNext(self):
        return self.next

class List:
    def __init__(self):
        self.current = None

    def add(self, value):
        node = Node(value) # create a node with value(data)
        node.next = self.current # update node just created
        self.current = node # update current node-pointer

    def print(self):
        node = self.current
        while node:
            print(node.data)
            node = node.next
    def clear(self):
        self.__init__()


exampleList = List()
exampleList.add(5) # add 5. (Node with 5).next = None, which means it is last node
exampleList.add(4) # add 4. (Node with 4).next = 5, so List looks like (4->5->None)
exampleList.add(3) # so on and so forth
exampleList.add(2)
exampleList.add(1)
exampleList.print() # we will see 1 2 3 4 5
