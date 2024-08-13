class Node:
    def __init__(self, node_val=None):
        self.node_val = node_val
        self.next_node = None


class MyLinkedList:
    def __init__(self):
        self.head_node = None


def print_linked_list(linked_list):
    node = linked_list.head_node
    while node is not None:
        print(node.node_val)
        node = node.next_node


def merge_list(list_a, list_b):
    node_a = list_a.head_node
    node_b = list_b.head_node
    list_c = MyLinkedList()
    node_c = None
    if node_a is None and node_b is None:
        return list_c
    if node_a is not None and node_b is not None:
        if node_a.node_val >= node_b.node_val:
            node_c = Node(node_b.node_val)
            node_b = node_b.next_node
            list_c.head_node = node_c
        else:
            node_c = Node(node_a.node_val)
            node_a = node_a.next_node
            list_c.head_node = node_c
    if node_a is None:
        node_c = Node(node_b.node_val)
        node_b = node_b.next_node
        list_c.head_node = node_c
    if node_b is None:
        node_c = Node(node_a.node_val)
        node_a = node_a.next_node
        list_c.head_node = node_c

    while node_a is not None and node_b is not None:
        if node_a.node_val >= node_b.node_val:
            node_c.next_node = Node(node_b.node_val)
            node_b = node_b.next_node
        else:
            node_c.next_node = Node(node_a.node_val)
            node_a = node_a.next_node
        node_c = node_c.next_node
    while node_a is not None:
        node_c.next_node = Node(node_a.node_val)
        node_a = node_a.next_node
        node_c = node_c.next_node

    while node_b is not None:
        node_c.next_node = Node(node_b.node_val)
        node_b = node_b.next_node
        node_c = node_c.next_node

    return list_c


if __name__ == '__main__':
    list_a = MyLinkedList()
    node1 = Node(1)
    node3 = Node(3)
    node5 = Node(5)
    list_a.head_node = node1
    node1.next_node = node3
    node3.next_node = node5
    # print_linked_list(list_a)

    list_b = MyLinkedList()
    node2 = Node(2)
    node4 = Node(4)
    node6 = Node(6)
    list_b.head_node = node2
    node2.next_node = node4
    node4.next_node = node6
    # print_linked_list(list_b)

    list_c = merge_list(list_a, list_b)
    print_linked_list(list_c)
