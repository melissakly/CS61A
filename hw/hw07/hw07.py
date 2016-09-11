# Linked Lists (do not modify the following class!)


class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

# Q1

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)

# Q2 (and Extra Question)

def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    seen = []
    while link != Link.empty:
        seen += [link]
        link = link.rest 
        if link in seen:
            return True 
    return False  

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

# Trees (do not modify the following class!)

class Tree:
    def __init__(self, entry, children=[]):
        for c in children:
            assert isinstance(c, Tree)
        self.entry = entry
        self.children = children

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.entry, children_str)

    def is_leaf(self):
        return not self.children

# Q3

def cumulative_sum(t):
    """
    Mutates t where each node's entry becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
            return t
    else:
        for child in t.children:
            cumulative_sum(child)
            t.entry += sum([child.entry])

# Q4

def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    """
    if t.is_leaf():
        return True
    if len(t.children) == 1:
        return True
    elif t.entry < t.children[0].entry and t.entry > t.children[1].entry:
            return False
    for c in t.children:
        return is_bst(c)

        #if bst_min(t.children) <= t.entry and bst_max(t.children) >= t.entry: #checks left and right node of children and compare it to the root
            #return True   
        #def bst_max(t): #wanted to index through the right children by setting index to 1 and finding the max value by iterating through the list of of children
            #index = 1
            #if is_leaf(t):
             #   return entry(t)
            #else:
                #index += 1
                #return max[bst_max(c) for c in t.children]
        #def bst_min(t): #wanted to index through the left children by setting index to 0 and finding the min value by iterating through the list of of children
            #index = 0
            #if is_leaf(t):
                #return entry(t)
            #else:
                #index += 1
                #return min[bst_min(c) for c in t.children]

     #def bst_max(self): #disc 9 references
        #if self.right is tree.empty:
                #return self.entry
        #return self.right.max
    #def bst_min (self): 
        #if self.left is tree.empty:
            #return self.entry
        #return self.left.min"""


# Sets (do not modify the following function!)

import time

def timeit(func):
    """Returns the time required to execute FUNC() in seconds."""
    t0 = time.perf_counter()
    func()
    return time.perf_counter() - t0

# Q5

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    >>> add_up(151, range(0, 200000, 2))
    False
    >>> timeit(lambda: add_up(151, range(0, 200000, 2))) < 1.0
    True
    >>> add_up(50002, range(0, 200000, 2))
    True
    """
    for x in lst:
        for y in lst:
            if x > n or y > n:
                return False 
            if x!=y and (x + y) == n:
                return True
    return False

# Q6

def missing_val(lst0, lst1):
    """Assuming that lst0 contains all the values in lst1, but lst1 is missing
    one value in lst0, return the missing value.  The values need not be
    numbers.

    >>> from random import shuffle
    >>> missing_val(range(10), [1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> big0 = [str(k) for k in range(15000)]
    >>> big1 = [str(k) for k in range(15000) if k != 293 ]
    >>> shuffle(big0)
    >>> shuffle(big1)
    >>> missing_val(big0, big1)
    '293'
    >>> timeit(lambda: missing_val(big0, big1)) < 1.0
    True
    """
    s = set(lst0).difference(lst1)
    return list(s)[0]

    #new set with elements in s but not in t
