class node:
    #initializing the empty node
    def __init__(self,data):
        self.data = data
        self.next = None


class linklist:
    #initializing linkedlist object
    def __init__(self):
        self.head = None

    def deleteNode(self, key):   
        temp = self.head  
  
        # If head node itself holds the key to be deleted  
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
  
        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next'  
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
  
        # if key was not present in linked list  
        if(temp == None):  
            return
  
        # Unlink the node from linked list  
        prev.next = temp.next
  
        temp = None
  


    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next        

if __name__ == "__main__":
    
    llist = linklist()
    llist.head = node(1)
    second = node(2)
    third = node(3)
    fourth = node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth
    

    llist.deleteNode(2)
    llist.printlist()