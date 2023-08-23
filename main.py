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
    def unlink(self, *data):
        current = self.head
        tmp = None
        while current:
            next_node = current.next
            if current.next.data in data:
                data = list(data).remove(current.next.data)
                tmp = next_node.next
                next_node.next = None
                if data and len(data) >= 1:
                    next_node = tmp
                else:    
                    current.next = self.head
                    return
                current = next_node
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
# llist.mark(3, 19, 22)
# llist.sweep()




# Displaying the linked list
llist.display()
# llist.display_backward()
