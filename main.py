class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # tmp

    def append_left(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def append_right(self, data):
        new_node = Node(data)

        if not self.tail:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        # overwrite the reference with current node
        self.tail = new_node


    # delete node based on value
    def remove(self, data):
        current = self.head
        # print(current, self.head)
        while current:
            next_node = current.next
            prev_node = current.prev

            if current.data == data:
                current.next = current.prev = None

                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node

                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                # current is holding the ref of self.head but self.head is the node variable which needs to update as well, if removes head
                current = next_node
                # return
            else:
                current = next_node

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
# llist.append_left(10)
# llist.append_left(20)
# llist.append_left(30)
# llist.append_left(20)

llist.append_right(20)
llist.append_right(10)
llist.append_right(30)
llist.append_right(10)

llist.remove(10)

# Displaying the linked list
llist.display_forward()
llist.display_backward()
