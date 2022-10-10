
class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        self.childs = []

    def is_root(self):
        return self.parent == None

    def is_leaf(self):
        return len(self.childs) == 0

    def add_child(self, value):
        node = Node(value, self)
        self.childs.append(node)
        return node


class Testdata:

    @staticmethod
    def bulid_helloworld():
        root = Node("H")

        e = root.add_child("E")
        e.add_child("L")
        e.add_child("L")
        e.add_child("O")

        w = root.add_child("W")
        w.add_child("O")
        w.add_child("R").add_child("L")

        root.add_child("D")

        return root


class Recursion:

    def run(self, root):
        self.visit(root)

    def visit(self, node):
        print(node.value)
        for child in node.childs:
            self.visit(child)


class Traverse:

    def run(self, root):
        self.traverse(root)

    def traverse(self, node):
        stack = []
        stack.append(node)

        while len(stack) > 0:
            node = stack.pop()
            print(node.value)
            for child in reversed(node.childs):
                stack.append(child)


if __name__ == '__main__':
    root = Testdata.bulid_helloworld()

    print("Recursion:")
    recursion = Recursion()
    recursion.run(root)

    print("Traverse:")
    traverse = Traverse()
    traverse.run(root)
