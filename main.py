class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # tmp

    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = self.tail = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # delete node based on value
    def remove(self, data):
        current = self.head
        # print(current, self.head)
        prev_node = None
        while current:
            if current.data == data:
                tmp = current.next
                current.next = None
                print(tmp, current.next)
                if prev_node:
                    prev_node.next = tmp
                else:
                    self.head = tmp
                # current is holding the ref of self.head but self.head is the node variable which needs to update as well, if removes head
                current = tmp
                # return
            else:
                prev_node = current
                current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print('None')


# Creating a linked list
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(20)
# llist.remove(20)

# Displaying the linked list
llist.display_forward()
llist.display_backward()
