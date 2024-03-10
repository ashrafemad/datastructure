
class LinkedListNode:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    head = None
    tail = None

    def insert(self, data):
        node = LinkedListNode(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        return node

    def find(self, data):
        current_node = self.head
        result = None
        while current_node is not None:
            if current_node.data == data:
                result = current_node
                break
            current_node = current_node.next
        return result

    def get_previous(self, node):
        current_node = self.head
        while current_node:
            if current_node.next == node:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        node_with_data = self.find(data)
        if not node_with_data:
            return False
        if node_with_data == self.head == self.tail:
            self.tail = self.head = None
            return True
        if node_with_data == self.head:
            self.head = node_with_data.next
            return True
        elif node_with_data == self.tail:
            previous_node = self.get_previous(node_with_data)
            previous_node.next = None
            self.tail = previous_node
            return True
        else:
            previous_node = self.get_previous(node_with_data)
            previous_node.next = node_with_data.next
            return True

    def reverse(self):
        current_node = self.tail
        while current_node and current_node != self.head:
            previous_node = self.get_previous(current_node)
            current_node.next = previous_node
            current_node = previous_node
        self.head, self.tail = self.tail, self.head
        self.tail.next = None

    def to_list(self):
        current_node = self.head
        nodes_data_list = []
        while current_node:
            nodes_data_list.append(current_node.data)
            current_node = current_node.next
        return nodes_data_list
