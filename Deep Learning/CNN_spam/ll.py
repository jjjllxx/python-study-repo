class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

# Node 的 str
    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.node_list = []

    def pop(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            self.head = None
        else:
            self.node_list[-2].next = None
        res = self.node_list.pop()
        return res.data

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            self.node_list[-1].next = new_node
        self.node_list.append(new_node)
        return

    def retrieve(self, idx):
        if idx >= len(self):
            return None
        return self.node_list[idx].data

    def pop_start(self):
        if self.head is not None:
            self.head = self.head.next
        res = self.node_list.pop(0)
        return res.data

    def prepend(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        self.node_list.insert(0, new_node)
        return

    def __len__(self):
        return len(self.node_list)

# LinkedList 的 str
    def __str__(self):
        res = ""
        for i in self.node_list:
            if type(i.data) is int:
                res += repr(i.data) + ' -> '
            else:
                res += repr(str(i)) + ' -> '
        return res + 'None'


names = LinkedList()
print(names)
names.append("test")
print(len(names))
print(names.pop())
print(len(names))
names.append("Steve Jobs")
names.append("Jeff Bezos")
names.prepend("Bill Gates")
names.append(10)
print(names.retrieve(0))
print(names.retrieve(1))
print(names.retrieve(2))
print(names)
print(names.pop())
print(names.pop_start())
print(names)
# Node下的str要以str的形式出，linkedlist下面的str以repr形式出，如果在node str下面写repr（self.data），node str就跑不对了，所以要怎么修改呢？
print(str(1))
print(repr(1))
print(str(repr(1)))
print(repr(str(1)))

print(type(1) is int)