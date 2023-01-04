class Node:
    #first in Node class there is two atributes data whih can take a intiger or any complex Number
    #and next work as a pointer
    def __init__(self,data,next):
        self.data = data
        self.next = next
    # I create a new class call  LinkedList
    # and create a instance object head and initialize it with None
class LinkedList:
    def __init__(self):
        self.head=None
    # I create a new class call insert_at_beginning
    
    def insert_at_begining(self,data):
        node = Node(data,self.head) #I Call Node Methods and pass  the data and the head
        self.head = node # and  the head become node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr=" "  
        while itr:
            llstr += str(itr.data)+"------->"
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        c=0
        itr = self.head
        while itr:
            c+=1
            itr =itr.next
        return c
    def remove_at_index(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")
        if index==0:
            self.head = self.head.next
            return 
        c=0
        itr=self.head
        while itr:
            if c== index-1:
                itr.next = itr.next.next
                break
            itr =itr.next
            c+=1     
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")
        if index== 0:
            self.insert_at_begining(data)
            return
        else:
            c=0
            itr= self.head
            while itr:
                if c == index-1:
                    node= Node(data,itr.next)
                    itr.next = node
                    break
                itr= itr.next
                c+=1
                
ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(89)
ll.insert_at_end(33)
ll.insert_at_end(21)
ll.insert_value(["banana", "mango", "grapes", "orange"])
ll.print()
ll.remove_at_index(2)
ll.print()
ll.insert_at(0,'flags')
ll.print()
ll.insert_at(2,"jackfruit")
ll.print()
print("length: " ,ll.get_length())
