class Node:
    def __init__(self, value=None):
        self.node_value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head_node = None

    def insert(self, value):
        if self.head_node is None:
            self.head_node = Node(value)
        else:
            self.next_node = Node(value)

    def listprint(list):
        printval = list.head_node
        while printval is not None:
            print(printval.node_value)
            printval = printval.next_node


if __name__ == '__main__':
    list = LinkedList()
    list.insert("Mon")
    list.insert("Tue")
    list.insert("Wed")
    list.listprint()
