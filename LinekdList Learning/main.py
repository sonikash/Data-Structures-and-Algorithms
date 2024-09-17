class Node:
    def __init__(self,data=None, next=None):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self): #constructor that will create a LL
        self.head =None

    def insert_at_beginning(self,data): #insertion at beginning of LL
        node =Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):  #insertion at the end of LL
        if self.head is None:
            self.head = Node(data,None)
            return

        itr =self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list): #inserting list into a LL
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_index(self,index,data):
        if index<0 or index>self.length_of_linkedlist():
            return Exception("Invalid index")

        if index==0:
            self.insert_at_beginning(self.data)
            return
        count=0
        itr= self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count=count+1

    def insert_after_value(self,value,data):
        itr=self.head
        while itr:
            if itr.data == value:
                node = Node(data,itr.next)
                itr.next=node
                break
            itr = itr.next

    def length_of_linkedlist(self): #retreiving the length of LL
        count = 0
        itr =self.head
        while itr:
            itr= itr.next
            count= count+1
        return count

    def remove_at_index(self,index): #removing the element at a particular index in LL
        if index<0 or index>=self.length_of_linkedlist():
            print ("Index mentioned for removal is invalid")
            return
        if index==0:
            self.head=self.head.next
            return
        count =0
        itr=self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count = count +1

    def remove_by_value(self,value):
        itr=self.head
        while itr:
            if itr.next.data== value:
                itr.next=itr.next.next
                break
            itr=itr.next

    def print(self): #printing the LL as a string
        if self.head is None:
            print("Linked List is empty")
            return

        itr=self.head  # variable itr that is pointing at the node
        llstr=''       #empty string used to print Linked list data in string format
        while itr:
            llstr=llstr +str(itr.data)+ "--->"
            itr = itr.next

        print(llstr)


if __name__ =='__main__':
    ll=LinkedList()

    ll.insert_values(["audi","mercedes","bmw","bentley","Rolls"])
    ll.print()

    print ("length is:",ll.length_of_linkedlist())
    ll.remove_at_index(-1)
    ll.insert_at_index(3,"Subaru")
    ll.print()
    ll.remove_by_value("bmw")
    ll.insert_after_value("bentley","volkswagen")

    ll.print()




