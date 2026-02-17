
from Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, symbol, score):
        if self.root is None:
            self.root = Node(symbol, score)
        else:
            self._insert(self.root, symbol, score)

    def _insert(self, current, symbol, score):
        if score < current.score:
            if current.left is None:
                current.left = Node(symbol, score)
            else:
                self._insert(current.left, symbol, score)
        else:
            if current.right is None:
                current.right = Node(symbol, score)
            else:
                self._insert(current.right, symbol, score)

    def descending(self):
        ordered = []
        self._descending(self.root, ordered)
        return ordered

    def _descending(self, node, ordered):
        if node:
            self._descending(node.right, ordered)
            ordered.append((node.symbol, node.score))
            self._descending(node.left, ordered)
