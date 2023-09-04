class MNode:
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


if __name__ == '__main__':
    l_list = MyLinkedList()
    l_list.head_node = MNode("Monday")

    print_linked_list(l_list)
