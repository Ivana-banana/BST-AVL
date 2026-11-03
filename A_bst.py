import sys

sys.setrecursionlimit(10000)


class Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node


def delete(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        m = node.right
        while m.left is not None:
            m = m.left
        node.key = m.key
        node.right = delete(node.right, m.key)
    return node


def exists(node, key):
    while node is not None:
        if key == node.key:
            return True
        node = node.left if key < node.key else node.right
    return False


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


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
    data = sys.stdin.read().split("\n")
    q = int(data[0])
    root = None
    out = []
    for i in range(1, q + 1):
        parts = data[i].split()
        cmd = parts[0]
        if cmd == "add":
            root = insert(root, int(parts[1]))
        elif cmd == "del":
            root = delete(root, int(parts[1]))
        elif cmd == "exists":
            out.append("YES" if exists(root, int(parts[1])) else "NO")
        elif cmd == "height":
            out.append(str(height(root)))
        elif cmd == "print":
            keys = preorder(root)
            out.append(" ".join(keys) if keys else "Empty")
    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


main()
