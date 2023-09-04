class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.head_val = None

    def inset_head(self, newdata):
        new_node = Node(newdata)
        # Update the new nodes next val to existing node
        new_node.nextval = self.head_val
        self.head_val = new_node


def list_print(linked_list):
    printval = linked_list.headval
    while printval is not None:
        print(printval.dataval)
        printval = printval.nextval


if __name__ == '__main__':
    list = LinkedList()
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")

    list.headval.nextval = e2
    e2.nextval = e3

    list.inset_head("Sun")
    list_print(list)
