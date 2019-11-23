class Node():

    def __init__(self,vlaue):
        self.value  = vlaue
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

#   Traversing the the LinkedList - Time Complexity - O(N)
    def traverseLinkedList(self):
        temp = self.head
        if temp == None: return
        while temp != None:
            print(temp.value)
            temp = temp.next


#   Insert a Node at a Head - Time Complexity O(N)
    def insetHead(self,var):
        newNode = Node(var)
        newNode.next = self.head
        self.head = newNode

#   Insert a Node at end of LinkedList - Time Complexity O(N)
    def insetAtEnd(self,var):
        temp = self.head
        if temp == None:
            self.head = Node(var)
            return
        elif temp.next == None:
             temp.next = Node(var)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Node(var)

#   Insert a Node at a position - Time Complexity O(N)
    def insetAtPosition(self,position,val):
        newNode = Node(val)
        if position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            count = 1
            temp = self.head
            while count < position-1:
                temp = temp.next
                count = count+1
            newNode.next = temp.next
            temp.next = newNode



if __name__ == "__main__":
    ll = LinkedList()
    ll.insetHead("H3")
    ll.insetAtEnd("E")
    ll.insetAtEnd("V")
    ll.insetHead("H2")
    ll.insetAtEnd("A")
    ll.insetHead("H1")
    ll.insetAtEnd("A")
    ll.insetAtPosition(1,"I")
    ll.traverseLinkedList()




#   Insert a Node at head
#   Insert a Node at end
#   Insert a Node at a position
#   Inserting Item after another Item
#   Inserting Item before another Item
