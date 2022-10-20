from __future__ import annotations
from inspect import CORO_CLOSED
from multiprocessing import parent_process


class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ForestNode(object):
    def __init__(self, val=None, parent=None, children=[]):
        self.val = val
        self.parent = parent
        self.children = children


class MatrixNode(object):
    def __init__(self, coord: tuple[int,int]=None, neighbours: MatrixNode=[]):
        self.coord = coord
        self.neigbours = neighbours


class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class ChainNode(object):
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
