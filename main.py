class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current = self.head
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            return
        while current.next.data != self.head.data:
            current = current.next
        # append node and refer to the beginning
        current.next = new_node
        new_node.next = self.head

    # delete node based on value
    def unlink(self, data):
        current = self.head
        tmp = None
        # case header = data
        if self.head.data == data:
            self.head = current.next
            current.next = None
            current = self.head
        # case between header
        while current.next.data != self.head.data:
            next_node = current.next
            if next_node.data == data:
                tmp = next_node.next
                next_node.next = None
                current.next = tmp

                current = current.next
            else:
                current = next_node

    def mark(self, *data):
        current = self.head
        # check header
        if self.head.data in data:
            self.head.marked = True
        # exclude header include footer
        while current.next.data != self.head.data:
            if current.next.data in data:
                current.next.marked = True

            current = current.next

    def sweep(self):
        current = self.head
        tmp = None
        if getattr(self.head, "marked", False):
            self.head = current.next
            current.next = None
            current = self.head

        while current.next.data != self.head.data:
            next_node = current.next
            if getattr(current.next, "marked", False):
                tmp = next_node.next
                if not tmp:
                    tmp = self.head
                    print(tmp.data, current.data, getattr(tmp, "marked", False))
                next_node.next = None
                current.next = tmp
                current = current.next
            else:
                current = next_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
            if current.data == self.head.data:
                print("Begin of the node")
                return
            print(current.data)


# Creating a linked list
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(20)
llist.append(10)

# llist.append(20)
# llist.append(10)
# llist.append(30)
# llist.append(10)

# for i in range(1, 101):
#     llist.append(i)

# unlink
# Pros and Cons
# Pros:

# Direct removal without the need for marking and sweeping.
# Efficient for immediate deletion without memory overhead.
# Cons:

# Requires careful manipulation of pointers.
# Immediate deletion may result in small performance overhead, especially for large lists
# llist.unlink(10)

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
llist.mark(20,30)
llist.sweep()


# Displaying the linked list
llist.display()
# llist.display_backward()
