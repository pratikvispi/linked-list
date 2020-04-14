class node:
    #initializing the empty node
    def __init__(self,data):
        self.data = data
        self.next = None


class linklist:
    #initializing linkedlist object
    def __init__(self):
        self.head = None


    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next


    def push(self, new_data):
        # for adding at the beginning of the linked list
        new_node = node(new_data)

        new_node.next = self.head

        self.head = new_node  


    def insertAfter(self,prev_node,new_data):

        # for adding at the given point of the linked list
        if(prev_node is None):
            print("invalid node selection beacause previous doesn't exists ")
        
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self , new_data):

        new_node = node(new_data)

        if(self.head is  None):  #checking linked list is empty or not
            self.head = new_node
            return 

        last = self.head
        while(last.next): #traversing till end of the linked list
            last = last.next
        last.next = new_node
     
      








if __name__ == "__main__":
    
    llist = linklist()
    llist.head = node(1)
    second = node(2)
    third = node(3)
    fourth = node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = None
    llist.push(0)#push operation at the begining 

    llist.insertAfter(third,13)#inserting at given index

    llist.append(78)#appending new node at last

    llist.printlist() #printing whole linked list