from typing import Optional, Any


class BinaryNodeAVL:
    def __init__(self, x: Any) -> None:
        self.item: Any = x
        self.left: Optional[BinaryNodeAVL] = None
        self.right: Optional[BinaryNodeAVL] = None
        self.parent: Optional[BinaryNodeAVL] = None
        self.subtree_update()

    def subtree_update_height(self) -> None:
        left_h = get_node_height(self.left)
        right_h = get_node_height(self.right)
        self.height = 1 + max(left_h, right_h)

    def skew(self) -> int:
        return get_node_height(self.right) - get_node_height(self.left)

    def subtree_iter(self):
        if self.left:
            yield self.left.subtree_iter()
        yield self
        if self.right:
            yield self.right.subtree_iter()

    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):
        if self.right:
            return self.right.subtree_first()
        else:
            return self

    def successor(self):
        if self.right:
            return self.right.subtree_first()
        else:
            node = self
            while node.parent and (node is node.parent.right):
                node = node.parent
            return node.parent

    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        else:
            node = self
            while node.parent and (node is node.parent.left):
                node = node.parent
            return node.parent

    def subtree_insert_before(self, B) -> None:
        if self.left:
            node = self.left.subtree_last()
            node.right = B
            B.parent = node
        else:
            self.left = B
            B.parent = self
        self.maintain()

    def subtree_insert_after(self, B) -> None:
        if self.right:
            node = self.right.subtree_first()
            node.left = B
            B.parent = node
        else:
            self.right = B
            B.parent = self

        self.maintain()

    def subtree_delete(self):
        if self.left or self.right:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
                self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            self.parent.maintain()
        return self

    def subtree_rotate_right(self):
        node = self
        assert node.left
        # pointers to nodes
        B, E = node.left, node.right
        A, C = B.left, B.right

        # swap node and B accodring to defined "rotation right" operation
        node, B = B, node
        node.item, B.item = B.item, node.item
        B.left, B.right = A, node
        node.left, node.right = C, E
        if A:
            A.parent = B
        if E:
            E.parent = node

        B.subtree_update_height()
        node.subtree_update_height()

    def subtree_rotate_left(self):
        node = self
        assert node.right
        A, D = node.left, node.right
        C, E = D.left, D.right

        node, D = D, node
        node.item, D.item = D.item, node.item
        D.left, D.right = node, E
        node.left, node.right = A, C
        if A:
            A.parent = node
        if E:
            E.parent = D

        node.subtree_update_height()
        D.subtree_update_height()

    def rebalance(self):  
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left    ()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):
        self.rebalance()
        self.subtree_update_height()
        if self.parent:
            self.parent.maintain()


def get_node_height(node: Optional[BinaryNodeAVL]) -> int:
    if node:
        return node.height
    else:
        return -1


class BinaryTreeAVL:
    def __init__(self, node_type: BinaryNodeAVL = BinaryNodeAVL) -> None:
        self.root = None
        self.size = 0
        self.node_type = node_type

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        if self.root:
            for a in self.root.subtree_iter():
                yield a.item
