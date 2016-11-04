# this code will insert node to the last

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return 'Node ['+str(self.value)+']'

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, x):
        if self.first == None: # if the list is empty, make the node as first node and last node
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first: # if there is one node, make new node as last node and existing node.next point to node just created
            self.last = Node(x, None)
            self.first.next = self.last
        else:                         # else, save created node to current and add it to the lastNode.next, then update self.last to current (created node)
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def __str__(self):
        while(self.first != self.last): # print node until last node
            print(self.first)
            self.first = self.first.next
        print(self.first) # print last node


    def clear(self):
        self.__init__()

LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.__str__() # final should be Node [1] Node [2] Node [3]
