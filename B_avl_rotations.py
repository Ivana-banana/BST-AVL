import sys


class Node:
    __slots__ = ("key", "left", "right", "parent")

    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = {}

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.nodes[key] = self.root
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key, cur)
                    self.nodes[key] = cur.left
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(key, cur)
                    self.nodes[key] = cur.right
                    return
                cur = cur.right

    def _replace(self, old, new):
        # new встаёт на место old у бывшего родителя old
        p = old.parent
        new.parent = p
        if p is None:
            self.root = new
        elif p.left is old:
            p.left = new
        else:
            p.right = new

    def rotate_left(self, a):
        b = a.right
        self._replace(a, b)
        a.right = b.left
        if b.left is not None:
            b.left.parent = a
        b.left = a
        a.parent = b

    def rotate_right(self, a):
        b = a.left
        self._replace(a, b)
        a.left = b.right
        if b.right is not None:
            b.right.parent = a
        b.right = a
        a.parent = b

    def preorder(self):
        res = []
        stack = [self.root] if self.root else []
        while stack:
            node = stack.pop()
            res.append(str(node.key))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    tree = Tree()
    for i in range(1, n + 1):
        tree.insert(int(data[i]))
    m = int(data[n + 1])
    out = []
    pos = n + 2
    for _ in range(m):
        cmd, x = data[pos], int(data[pos + 1])
        pos += 2
        if cmd == "left":
            tree.rotate_left(tree.nodes[x])
        else:
            tree.rotate_right(tree.nodes[x])
        out.append(" ".join(tree.preorder()))
    sys.stdout.write("\n".join(out) + "\n")


main()
