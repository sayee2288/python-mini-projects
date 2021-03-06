class node:

    def __init__(self, data=None, next=None):

        print ('Created the node with data {}' .format(data))
        self.data = data
        self.next = next

    def get_data(self):

        return self.data

    def set_data(self, data):

        self.data = data

    def set_next(self, next=None):

        self.next = next

    def get_next(self):

        return self.next


class linked_list:

    def __init__(self, head=None):

        self.head = head

    def insert(self, node):

        if self.head is None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

    def delete(self, data):

        if self.head is None:
            return "Illegal operation"
        else:
            if self.head is None:
                print('No list initialized, illegal operation')
            ptr1 = self.head
            ptr2 = ptr1
            while True:
                if ptr1.data == data:
                    ptr2.next = ptr1.next
                    print ('Deleted the element from \
                        head of the linked list: {}' .format(ptr1.data))
                    break
                elif ptr1.next is None:
                    print('Traversed the linked \
                        list but couldn\'t find {}' .format(data))
                    break
                else:
                    ptr2 = ptr1
                    ptr1 = ptr1.next

    def print_list(self):

        ptr = self.head
        print()
        while True:
            print('{}' .format(ptr.data), end='->')
            if ptr.next is None:
                break
            else:
                ptr = ptr.next
                continue

    def reverseList(self):

           #Initializing values
           prev = None
           curr = self.head
           nex = curr.get_next()
      
           #looping
           while curr:
               #reversing the link
               curr.set_next(prev)     

               #moving to next node      
               prev = curr
               curr = nex
               if nex:
                   nex = nex.get_next()

           #initializing head
           self.head = prev
        
        
my_ll = linked_list()

while True:
    x = int(input('\nPlease select an operation: \n1)insert \n2)delete \n3)Print \n4)reverse the list \n5)exit\n--'))
    if x == 1:
        data = input('Please enter the data to place in the list: ')
        my_node = node(data)
        my_ll.insert(my_node)
    if x == 2:
        data = input('Please enter the element to be removed: ')
        my_ll.delete(data)
    if x == 3:
        my_ll.print_list()
    if x == 4:
        my_ll.reverseList()
    if x == 5:
        break
