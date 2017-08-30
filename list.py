class Node():

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):

        self.head = Node("root")

    def add(self, data):

        head = self.head
        while head.next is not None:
            head = head.next

        head.next = Node(data)

    def remove(self, data):

        head = self.head
        while head.next.data != data:
            head = head.next

        head.next = head.next.next

    def show(self):

        head = self.head
        while head is not None:
            print head.data
            head = head.next


def test_list():

    ll = LinkedList()
    ll.add("sean")
    ll.add("john")
    ll.add("katie")
    ll.show()
    ll.remove("john")
    ll.show()


test_list()
