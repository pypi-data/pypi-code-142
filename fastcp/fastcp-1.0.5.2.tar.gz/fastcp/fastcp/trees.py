"""
    Format: 
    
    class TreeNode:
        def __init__(self, val, left = None, right = None) -> None:
            self.val = val
            self.left = left
            self.right = right;
        
    Example: 
        root = TreeNode(10);
        root.left = TreeNode(5);
        root.right = TreeNode(20);
"""
from collections import deque as _deque;

class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right;
        
def Create(value):
    """
    Args:
        value (int): value to insert into the TreeNode
    Returns:
        TreeNode: returns a node with value
        Complexity: O(1)
    
    Example: 
        root = create(10);
        root.left = trees.create(20); 
        root.right = trees.create(30);
    """
    node = TreeNode(value)
    return node
    
def Inorder(root):
    """
    Args:
        root (TreeNode): root node of Tree
    Returns:
        List: returns a List containing inorder traversal of nodes
        Complexity: O(Log N)
    
    Example: 
        arr = trees.inorder(root);
    """
    arr = []
    def traverse(root, arr):
        if (root == None): return;
        traverse(root.left, arr);
        arr.append(root.val);
        traverse(root.right, arr);
    traverse(root, arr);
    return arr;

def Preorder(root):
    """
    Args:
        root (TreeNode): root node of Tree
    Returns:
        List: returns a List containing preorder traversal of nodes
        Complexity: O(Log N)
        
    Example: 
        arr = trees.preorder(root);
    """
    arr = []
    def traverse(root, arr):
        if (root == None): return;
        arr.append(root.val);
        traverse(root.left, arr);
        traverse(root.right, arr);
    traverse(root, arr);
    return arr;

def Postorder(root):
    """
    Args:
        root (TreeNode): root node of Tree
    Returns:
        List: returns a List containing postorder traversal of nodes
        Complexity: O(Log N)
    
    Example: 
        arr = trees.postorder(root);
    """
    arr = []
    def traverse(root, arr):
        if (root == None): return;
        traverse(root.left, arr);
        traverse(root.right, arr);
        arr.append(root.val);
    traverse(root, arr);
    return arr;

def Levelorder(root):
    """
    Generates Level Order Traversal of Tree
    Args:
        root (TreeNode): Root node of tree
    Returns:
        List[List]: returns a 2D list containing nodes in level order traversal
        Complexity: O(N*N)
    
    Example: 
        arr = trees.levelorder(root);
    """
    arr = [];
    if (root):
        queue = _deque([root]); n = 1;
        while(n):
            vec = []; temp = None;
            for i in range(n):
                temp = queue.popleft();
                vec.append(temp.val);
                if (temp.left): queue.append(temp.left);
                if (temp.right): queue.append(temp.right);
            arr.append(vec); n = len(queue);
    del queue; del vec;
    return arr;

def NodeSum(root):
    """
    Returns the Sum of all the nodes in the Tree
    Args:
        root (TreeNode): Root node of tree
    Returns:
        Int : if tree is empty returns 0 else retuns the sum of all the nodes in the tree
        Complexity: O(N Log N)
    
    Example: 
        arr = trees.levelorder(root);
    """
    if root == None: return 0;
    return sum(Inorder(root));

def Search(root, key) -> bool:
    """
    A function that searches the tree for the given node
    Args:
        root (TreeNode): root node of tree to Search
        key (any): value/node to search for

    Returns:
        bool: returns True if node is found else returns False
    """
    def traverse(root, key):
        if root == None: return
        if root.val == key: return True;
        a = traverse(root.left, key)
        b = traverse(root.right, key);
        return a or b
    if traverse(root, key): return True;
    return False;


