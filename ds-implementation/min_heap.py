#min_heap = linked list
#parent = 1
#left_child = parent * 2
#right_child = parent * 2 + 1

class Heap():

    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def insert(self, value):
        self.heaplist.append(value)
        self.size += 1
        count = self.size
        while count > 1:
            if self.heaplist[count] < self.heaplist[int(count/2)]:
                temp = self.heaplist[count]
                self.heaplist[count] = self.heaplist[int(count/2)]
                self.heaplist[int(count/2)] = temp
            count = int(count/2)

    def remove(self):
        r_value = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.heaplist.pop()
        self.size -= 1
        count = 1
        while (count * 2) < self.size:
            if self.heaplist[int(count/2)] is not None and self.heaplist[int(count/2) + 1] is not None:
                if self.heaplist[int(count/2)] < self.heaplist[int(count/2) + 1]:
                    temp = self.heaplist[int(count/2)]
                    self.heaplist[int(count/2)] = self.heaplist[count]
                    self.heaplist[count] = temp
                else:
                    temp = self.heaplist[int(count/2) + 1]
                    self.heaplist[int(count/2) + 1] = self.heaplist[count]
                    self.heaplist[count] = temp
        return r_value

    def print_heap(self):
        count = 1
        while count <= self.size:
            print(self.heaplist[count])
            count += 1

## Driver Code
my_heap = Heap()
while True:
    x = int(input('\nPlease select an operation: \n1)insert \n2)remove \n3)Print \n4)exit\n--'))
    if x == 1:
        data = int(input('Please enter the data to place in the list: '))
        my_heap.insert(data)
    if x == 2:
        x = my_heap.remove()
        print(x)
    if x == 3:
        my_heap.print_heap()
    if x == 4:
        break
