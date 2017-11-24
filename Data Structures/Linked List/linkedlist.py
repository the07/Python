""" An implementation of the linked list data structure. """

class Node:
    
    def __init__(self, data):
        self.data = data # Assign the data
        self.next = None # Initialise next as None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printList(self):
        print ("Printing linked list")
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
            
    def push(self, new_data):
        """
        Function to push new data to the beginning of the list.
        """
        new_node = Node(new_data)
        
        # Make next of new node point to the current head
        new_node.next = self.head
        
        # Make new node the head of the list
        self.head = new_node
        
    def insertAfter(self, prev_Node, new_data):
        """
        Function to insert a new node after a given node
        """
        
        if prev_Node is None:
            print ("The given node must be in the linked list")
            return
        
        new_Node = Node(new_data)
        
        # Point new node's next to previous node next
        new_Node.next = prev_Node.next
        
        # Point previous node next to new node
        prev_Node.next = new_Node
        
    def append(self, new_data):
        """
        Function to insert a new node at the end of the list
        """
        
        new_Node = Node(new_data)
        
        # If linkedlist is empty, make this new node as the head
        if self.head is None:
            self.head = new_Node
            return
        
        # Else traverse to the last node
        last = self.head
        while (last.next):
            last = last.next
            
        # Change the next of the last node
        last.next = new_Node
        
    def deleteNode(self, key):
        """
        Function to delete a node by key
        """
        
        # Store the head in temp
        temp = self.head
        
        # See if head holds the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        # Traverse the list to locate the key, keep track of previous
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            
        if (temp == None):
            print ("Key not present in the list")
            return
        
        # Unlink the node from the LinkedList
        prev.next = temp.next
        
        temp = None
        
    def deleteAtPosition(self, position):
        """ Function to delete a node at the given position """
        
        # Check to see if linked list is empty
        if self.head is None:
            return
        
        temp = self.head
        
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        # Traverse the list until the given position
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break
            
        if temp is None:
            return
        if temp.next is None:
            return
        
        next_node = temp.next.next
        
        temp.next = None
        
        temp.next = next_node
        
    def getCount(self):
        """ Return the length of the linked list. """
        
        count = 0
        temp = self.head
        
        while (temp):
            count += 1
            temp = temp.next
            
        return count
    
    def swapNodes(self, x, y):
        
        # Nothing to do if x and y are same
        if x == y:
            return
        
        # Search for x and keep track of previous and current
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
            
        # Search for y and keep track of previous and current
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
            
        # If x or y not present, return
        if currX == None or currY == None:
            return
        
        # If x is not the head
        if prevX != None:
            prevX.next = currY
        else: # make y the new head
            self.head = currY
            
        # if y is not head
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX
            
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
        
    def reverseList(self):
        """ Function to reverse a given linked list. """
        
        prev = None
        curr = self.head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
if __name__ == '__main__':
    
    # Driver program to test above function
    llist = LinkedList()
     
    # The constructed linked list is:
    # 1->2->3->4->5->6->7
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print ("Linked list before calling swapNodes() ")
    llist.printList()
    llist.swapNodes(4, 3)
    print( "\nLinked list after calling swapNodes() ")
    llist.printList()
    
    llist.reverseList()
    
    llist.printList()