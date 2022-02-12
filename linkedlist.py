class cnode:
    def __init__(self, val, tnext=None):
        self.val = val
        self.next = tnext


class linkedlist:

    def __init__(self, val=None, tnext=None):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.size == 0:
            return -1
        if self.size == 1:
            if index != 0:
                return -1
            else:
                return self.head.val
        n = 0
        node = self.head
        while node.next:
            if n == index:
                return node.val
            n += 1;
            node = node.next
        return node.val
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

    def addAtHead(self, val: int) -> None:
        if self.head:
            cur = cnode(self.head.val, self.head.next)
            self.head.val = val;
            self.head.next = cur
        else:
            cur = cnode(val)
            self.head = cur
        self.size += 1
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

    def addAtTail(self, val: int) -> None:
        if not self.head:
            node = cnode(val)
            self.head = node
            self.size += 1
            return
        elif self.size == 1:
            cur = cnode(val)
            self.head.next = cur
            self.size += 1
            return
        node = self.head
        while node.next:
            node = node.next
        cur = cnode(val)
        node.next = cur
        self.size += 1
        """
        Append a node of value val to the last element of the linked list.
        """

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        elif index > self.size:
            return
        else:
            ins = cnode(val)
            node = self.head;
            prev = node;
            n = 0
            while index != n:
                n += 1
                prev = node
                node = node.next
            ins.next = node
            prev.next = ins
            self.size += 1
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or self.size == 0:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
        elif index == self.size - 1:
            node = self.head;
            while node.next.next:
                node = node.next
            node.next = None
            self.size -= 1
        else:
            node = self.head;
            prev = node;
            n = 0
            while index != n:
                n += 1
                prev = node
                node = node.next
            prev.next = node.next
            self.size -= 1
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = linkedlist()
    param_1 = obj.get(1)
    val = 10
    obj.addAtHead(val)
    obj.addAtTail(val)
    obj.addAtIndex(1,val)
    print(obj.get(1))
    print(obj)
    obj.deleteAtIndex(1)

