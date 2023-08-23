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
    def unlink(self, data):
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
                
    def mark(self, *data):
        current = self.head
        while current:
            if current.data in data:
                current.marked = True
            
            current = current.next
                
    def sweep(self):
        current = self.head
        
        while current:
            next_node = current.next
            prev_node = current.prev
            
            if getattr(current, 'marked', False):
                current.next = current.prev = None
                
                if next_node:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                
                if prev_node:
                    prev_node.next = next_node
                else:
                    self.head = prev_node
                    
                current = next_node
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

# llist.append_right(20)
# llist.append_right(10)
# llist.append_right(30)
# llist.append_right(10)

for i in range(1, 101):
    llist.append_right(i)

# unlink
# Pros and Cons
# Pros:

# Direct removal without the need for marking and sweeping.
# Efficient for immediate deletion without memory overhead.
# Cons:

# Requires careful manipulation of pointers.
# Immediate deletion may result in small performance overhead, especially for large lists
llist.unlink(10)

# mark and sweep
# Pros and Cons
# Pros:

# Delayed deletion improves performance during traversal.
# Reduces memory fragmentation compared to immediate deletion.
# Can be advantageous when deletion is a costly operation.
# Cons:

# Requires additional memory for marking nodes.
# May lead to a minor delay in memory reclamation (sweep phase).
# More complex implementation than immediate deletion.
llist.mark(3, 19, 22)
llist.sweep()




# Displaying the linked list
llist.display_forward()
llist.display_backward()
