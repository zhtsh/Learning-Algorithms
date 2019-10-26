#! /usr/bin/python
# coding=utf8


class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class List(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __len__(self):
        size = 0
        node = self.root
        while node is not None:
            size +=1
            node = node.get_next()
        return size

    def add(self, data):
        node = self.root
        pre_node = None
        while node is not None:
            pre_node = node
            node = node.get_next()
        current_node = Node(data)
        if pre_node is None:
            self.root = current_node
        else:
            pre_node.set_next(current_node)

    def remove(self, data):
        node = self.root
        pre_node = None
        while node is not None:
            if node.get_data() == data:
                if pre_node is None:
                    self.root = node.get_next()
                else:
                    pre_node.set_next(node.get_next())
            pre_node = node
            node = node.get_next()

    def search(self, data):
        node = self.root
        while node is not None:
            if node.get_data() == data:
                return True
            node = node.get_next()
        return False


class BidNode(object):

    def __init__(self, data, pre_node=None, next_node=None):
        self.data = data
        self.pre_node = pre_node
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_pre(self):
        return self.pre_node

    def set_pre(self, pre_node):
        self.pre_node = pre_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class BidList(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def __len__(self):
        size = 0
        node = self.root
        while node is not None:
            size +=1
            node = node.get_next()
        return size

    def add(self, data):
        node = self.root
        pre_node = None
        while node is not None:
            pre_node = node
            node = node.get_next()
        current_node = BidNode(data)
        if pre_node is None:
            self.root = current_node
        else:
            pre_node.set_next(current_node)
            current_node.set_pre(pre_node)


    def remove(self, data):
        node = self.root
        while node is not None:
            if node.get_data() == data:
                if node.get_pre() is None:
                    self.root = node.get_next()
                else:
                    node.get_pre().set_next(node.get_next())
                if node.get_next():
                    node.get_next().set_pre(node.get_pre())
            node = node.get_next()

    def search(self, data):
        node = self.root
        while node is not None:
            if node.get_data() == data:
                return True
            node = node.get_next()
        return False


if __name__ == '__main__':
    # single list
    l = List()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(1)
    l.add(4)
    l.add(3)
    l.add(5)
    print('size: {}'.format(len(l)))
    print('search node 3: {}'.format(l.search(3)))
    print('search node 6: {}'.format(l.search(6)))
    l.remove(1)
    print('size: {}'.format(len(l)))
    l.remove(5)
    print('size: {}'.format(len(l)))
    l.remove(7)
    print('size: {}'.format(len(l)))

    # bidrectional list
    bl = BidList()
    bl.add(1)
    bl.add(2)
    bl.add(3)
    bl.add(1)
    bl.add(4)
    bl.add(3)
    bl.add(5)
    print('size: {}'.format(len(bl)))
    print('search node 3: {}'.format(bl.search(3)))
    print('search node 6: {}'.format(bl.search(6)))
    bl.remove(1)
    print('size: {}'.format(len(bl)))
    bl.remove(5)
    print('size: {}'.format(len(bl)))
    bl.remove(7)
    print('size: {}'.format(len(bl)))