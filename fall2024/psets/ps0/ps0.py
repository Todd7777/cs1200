#################
#               #
# Problem Set 0 #
#               #
#################


class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param key: the key associated with the vertex of the binary tree
        """
        self.parent = None
        self.left = None
        self.right = None
        self.key = int(key)
        self.size = None

def calculate_sizes(v):
    """
    Recursively calculates the sizes of all the subtrees rooted at descendants of vertex v.
    Each vertex v in the tree will have v.size set to the size of the subtree rooted at v.
    
    :param v: BTvertex, the root of a subtree
    """
    if v is None:
        return 0
    left_size = calculate_sizes(v.left)
    right_size = calculate_sizes(v.right)
    v.size = 1 + left_size + right_size
    return v.size

def FindDescendantOfSize(t, v):
    """
    Finds and returns a vertex w such that 
    t <= w.size <= 2t in the subtree rooted at vertex v.
    
    :param t: int, the lower and upper bounds of the subtree size to find
    :param v: BTvertex, the root of the subtree where we are searching
    :return: BTvertex, the vertex w with the desired subtree size,
    or None if no such vertex exists
    """
    current = v
    while current is not None:
        if t <= current.size <= 2 * t:
            return current
        # Decide which child to traverse based on the size
        if current.left and t <= current.left.size <= 2 * t:
            current = current.left
        elif current.right and t <= current.right.size <= 2 * t:
            current = current.right
        elif current.left and current.left.size > 2 * t:
            current = current.left
        elif current.right and current.right.size > 2 * t:
            current = current.right
        else:
            break  # No suitable child to explore, and current is not suitable either
    return None  # If no such vertex is found
