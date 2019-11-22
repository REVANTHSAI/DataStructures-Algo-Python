class Node():

    def __init__(self,vlaue):
        self.value  = vlaue
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

#   Traversing the the LinkedList
#   Time Complexity - O(N)
    def traverseLinkedList(self,node):
        temp = self.head
        if temp == None: return
        while temp != None:
            print(temp.value)
            temp = temp.next
        temp.next = None

#   Insert a Node at end of LinkedList
#   Time Complexity O(N)
    def insetAtEnd(self,nodeVar):
        temp = self.head
        if temp == None: elf.head = nodeVar

        while temp.next != None:
            temp = temp.next
        temp.next.next = nodeVar

#   Traverse a LinkedList
#   Insert a Node at head
#   Insert a Node at end
#   Insert a Node at a position
#   Inserting Item after another Item
#   Inserting Item before another Item
