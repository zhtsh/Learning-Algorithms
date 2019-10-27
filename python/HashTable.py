#! /usr/bin/python
# coding=utf8


class Node(object):

    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def get_data(self):
        return self.key, self.value

    def set_data(self, key, value):
        self.key = key
        self.value = value

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
        key, value = data
        node = self.root
        pre_node = None
        while node is not None:
            if node.get_data()[0] >= key:
                break
            pre_node = node
            node = node.get_next()
        current_node = Node(key, value)
        if node is None and pre_node is None:
            self.root = current_node
        elif node is None:
            pre_node.set_next(current_node)
        else:
            if node.get_data()[0] == key:
                node.set_data(key, value)
            elif pre_node is None:
                current_node.set_next(node)
                self.root = current_node
            else:
                pre_node.set_next(current_node)
                current_node.set_next(node)

    def remove(self, key):
        node = self.root
        pre_node = None
        while node is not None:
            if node.get_data()[0] == key:
                if pre_node is None:
                    self.root = node.get_next()
                else:
                    pre_node.set_next(node.get_next())
                break
            pre_node = node
            node = node.get_next()

    def search(self, key):
        node = self.root
        while node is not None:
            if node.get_data()[0] == key:
                return node.get_data()[1]
            node = node.get_next()
        return None

class HashMap(object):

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def __len__(self):
        sizes = [len(item) if item else 0 for item in self.slots]
        print('sizes: {}'.format(sizes))
        return sum(sizes)

    def put(self, key, value):
        index = self.hashfunc(key)
        print('put {} index: {}, value: {}'.format(key, index, value))
        if self.slots[index] is None:
            node_list = List()
            self.slots[index] = node_list
        else:
            node_list = self.slots[index]
        node_list.add((key, value))

    def get(self, key):
        index = self.hashfunc(key)
        print('get {} index: {}'.format(key, index))
        if self.slots[index] is None:
            return None
        else:
            return self.slots[index].search(key)

    def remove(self, key):
        index = self.hashfunc(key)
        print('remove {} index: {}'.format(key, index))
        if self.slots[index] is not None:
            self.slots[index].remove(key)

    def hashfunc(self, key):
        return hash(key) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    hm = HashMap(8)
    hm['aaa'] = 1
    hm['bbb'] = 2
    hm['ccc'] = 3
    hm['111'] = 4
    hm['222'] = 5
    hm['333'] = 6
    hm['ddd'] = 7
    hm['fff'] = 8
    hm['444'] = 9
    hm['555'] = 10
    hm['666'] = 11
    hm['777'] = 12
    print('size: {}'.format(len(hm)))
    print('111 value: {}'.format(hm['111']))
    print('ccc value: {}'.format(hm['ccc']))
    print('444 value: {}'.format(hm['444']))
    print('fff value: {}'.format(hm['fff']))
    print('abc value: {}'.format(hm['abc']))
    hm.remove('777')
    hm.remove('111')
    hm.remove('aaa')
    hm.remove('abc')
    print('size: {}'.format(len(hm)))
    hm['abc'] = 1
    hm['efg'] = 1
    hm['345'] = 1
    hm['123'] = 1
    hm['876'] = 1
    print('size: {}'.format(len(hm)))