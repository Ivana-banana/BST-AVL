import sys

sys.setrecursionlimit(10000)


class Node:
    __slots__ = ("key", "left", "right", "h")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.h = 1


def h(node):
    return node.h if node is not None else 0


def update(node):
    hl = node.left.h if node.left is not None else 0
    hr = node.right.h if node.right is not None else 0
    node.h = (hl if hl > hr else hr) + 1


def bal(node):
    return h(node.right) - h(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a
    update(a)
    update(b)
    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a
    update(a)
    update(b)
    return b


def balance(v):
    update(v)
    b = bal(v)
    if b == 2:
        if bal(v.right) < 0:
            v.right = rotate_right(v.right)
        return rotate_left(v)
    if b == -2:
        if bal(v.left) > 0:
            v.left = rotate_left(v.left)
        return rotate_right(v)
    return v


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node
    return balance(node)


def exists(node, key):
    while node is not None:
        if key == node.key:
            return True
        node = node.left if key < node.key else node.right
    return False


def preorder(root):
    res = []
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        res.append(str(node.key))
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def main():
    data = sys.stdin.buffer.read().decode().split("\n")
    q = int(data[0])
    root = None
    out = []
    for i in range(1, q + 1):
        parts = data[i].split()
        cmd = parts[0]
        if cmd == "add":
            root = insert(root, int(parts[1]))
        elif cmd == "exists":
            out.append("YES" if exists(root, int(parts[1])) else "NO")
        elif cmd == "root":
            out.append(str(root.key) if root else "Empty")
        elif cmd == "height":
            out.append(str(h(root)))
        elif cmd == "print":
            keys = preorder(root)
            out.append(" ".join(keys) if keys else "Empty")
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
