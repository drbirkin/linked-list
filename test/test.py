import unittest
import time

import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)  # Adds the parent directory to the sys.path

from main import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        llist = LinkedList()
        llist.append(10)
        self.assertEqual(llist.head.data, 10)

    def test_unlink(self):
        llist = LinkedList()
        llist.append(10)
        llist.append(20)
        llist.append(30)
        llist.unlink(20)
        self.assertEqual(llist.head.data, 10)
        self.assertEqual(llist.head.next.data, 30)

    def test_mark_and_sweep(self):
        llist = LinkedList()
        llist.append(10)
        llist.append(20)
        llist.append(30)
        llist.append(40)
        llist.mark(20, 30)
        llist.sweep()
        self.assertEqual(llist.head.data, 10)
        self.assertEqual(llist.head.next.data, 40)

    def test_stress_append_and_unlink(self):
        llist = LinkedList()
        for i in range(1, 10001):
            llist.append(i)
        llist.unlink(5000)
        self.assertEqual(llist.head.data, 1)
        self.assertEqual(llist.head.next.data, 2)

    def test_performance_append(self):
        llist = LinkedList()
        start_time = time.time()
        for i in range(1, 100001):
            llist.append(i)
        end_time = time.time()
        print("Performance Test (Append):", end_time - start_time, "seconds")

    def test_performance_unlink(self):
        llist = LinkedList()
        for i in range(1, 100001):
            llist.append(i)
        start_time = time.time()
        llist.unlink(50000)
        end_time = time.time()
        print("Performance Test (Unlink):", end_time - start_time, "seconds")

if __name__ == '__main__':
    unittest.main()
