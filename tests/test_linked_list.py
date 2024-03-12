import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_linked_list_structured_correctly(self):
        self.linked_list.insert(1)
        self.linked_list.insert(2)
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.tail.data, 2)
        self.assertEqual(self.linked_list.head.next.data, 2)
        self.assertIsNone(self.linked_list.tail.next)

    def test_linked_list_to_list_method_returns_list(self):
        self.linked_list.insert(1)
        self.assertIsInstance(self.linked_list.to_list(), list)

    def test_linked_list_insert_successful(self):
        self.linked_list.insert(9)
        self.linked_list.insert(5)
        self.linked_list.insert(2)
        self.linked_list.insert(4)
        self.assertEqual(self.linked_list.to_list(), [9, 5, 2, 4])

    def test_linked_list_with_single_node(self):
        self.linked_list.insert(10)
        self.assertEqual(self.linked_list.head, self.linked_list.tail)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.tail.data, 10)
        self.assertIsNone(self.linked_list.tail.next)
        self.assertIsNone(self.linked_list.head.next)

    def test_find_data_in_linked_list(self):
        to_find_node = self.linked_list.insert(9)
        self.linked_list.insert(5)
        self.linked_list.insert(2)
        self.linked_list.insert(4)
        self.assertIsNotNone(self.linked_list.find(5))
        self.assertEqual(self.linked_list.find(9), to_find_node)
        self.assertIsNone(self.linked_list.find(15))

    def test_delete_node_from_linked_list(self):
        self.linked_list.insert(5)
        previous_of_deleted = self.linked_list.insert(2)
        self.linked_list.insert(4)
        next_after_deletion = self.linked_list.insert(6)

        self.assertTrue(self.linked_list.delete(4))
        self.assertEqual(self.linked_list.to_list(), [5, 2, 6])
        self.assertEqual(previous_of_deleted.next, next_after_deletion)

    def test_delete_from_single_node_linked_list(self):
        self.linked_list.insert(5)
        self.assertTrue(self.linked_list.delete(5))
        self.assertEqual(self.linked_list.to_list(), [])
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)

    def test_delete_head_from_linked_list(self):
        self.linked_list.insert(5)
        expected_new_head = self.linked_list.insert(6)
        self.linked_list.insert(7)
        self.linked_list.insert(8)

        self.assertTrue(self.linked_list.delete(5))
        self.assertEqual(self.linked_list.to_list(), [6, 7, 8])
        self.assertEqual(self.linked_list.head, expected_new_head)
        self.assertEqual(self.linked_list.head.data, 6)

    def test_delete_tail_from_linked_list(self):
        self.linked_list.insert(5)
        self.linked_list.insert(6)
        expected_new_tail = self.linked_list.insert(7)
        self.linked_list.insert(8)

        self.assertTrue(self.linked_list.delete(8))
        self.assertEqual(self.linked_list.to_list(), [5, 6, 7])
        self.assertEqual(self.linked_list.tail, expected_new_tail)
        self.assertEqual(self.linked_list.tail.data, 7)

    def test_delete_non_exist_node(self):
        self.linked_list.insert(5)
        self.assertFalse(self.linked_list.delete(8))
        self.assertEqual(self.linked_list.to_list(), [5])

    def test_reverse_linked_list(self):
        node1 = self.linked_list.insert(5)
        node2 = self.linked_list.insert(6)
        node3 = self.linked_list.insert(7)
        node4 = self.linked_list.insert(8)
        self.assertEqual(self.linked_list.to_list(), [5, 6, 7, 8])
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.to_list(), [8, 7, 6, 5])
        self.assertEqual(self.linked_list.head, node4)
        self.assertEqual(self.linked_list.tail, node1)

    def test_reverse_single_node_linked_list(self):
        node1 = self.linked_list.insert(7)
        self.linked_list.reverse()
        self.assertEqual(self.linked_list.to_list(), [7])
        self.assertEqual(self.linked_list.head, node1)
        self.assertEqual(self.linked_list.tail, node1)

    def test_get_previous_node(self):
        node1 = self.linked_list.insert(5)
        node2 = self.linked_list.insert(6)
        node3 = self.linked_list.insert(7)
        node4 = self.linked_list.insert(8)

        self.assertEqual(self.linked_list.get_previous(node2), node1)
        self.assertIsNone(self.linked_list.get_previous(node1))
        self.assertEqual(self.linked_list.get_previous(node4), node3)

    def test_linked_list_is_cyclic(self):
        node1 = self.linked_list.insert(5)
        node2 = self.linked_list.insert(6)
        node3 = self.linked_list.insert(7)
        node4 = self.linked_list.insert(8)
        node3.next = node2

        self.assertEqual(self.linked_list.is_cyclic(), True)
