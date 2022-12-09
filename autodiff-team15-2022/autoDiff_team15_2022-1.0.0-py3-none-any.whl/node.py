import numpy as np

class Node:
    """A class for representing a Node in a computational graph for reverse mode automatic differentiation.

    Attributes
    ======
        value : int, float, np.int32, np.int64
            The value of the Node
        gradient : int, float, np.int32, np.int64
            The gradient of the Node with respect to the derivative and child Nodes
        children : list of Nodes
            A list of tuples (derivative, child) representing the derivative and children of the Node

    Methods
    ======
        grad()
            Calculates the gradient of a node
        clear()
            Clears a node to a state of no children or gradient stored
        __add__(other)
            Enables addition of nodes with numbers
        __radd__(other)
            Enables addition of nodes with numbers
        __sub__(other)
            Enables subtraction of nodes with numbers
        __rsub__(other)
            Enables subtraction of nodes with numbers
        __mul__(other)
            Enables multiplication of nodes with numbers
        __rmul__(other)
            Enables multiplication of nodes with numbers
        __pow__(other)
            Enables raising a Node to a power or other Node
        __rpow__(other)
            Enables raising a number to a Node
        __truediv__(other)
            Enables division of nodes with numbers
        __rtruediv__(other)
            Enables division of nodes with numbers
        __neg__(other)
            Enables negating a node
        __pos__(other)
            Enables calculation of the positive of a node
    """
    _supported_types = (int, float, np.int32, np.int64)

    def __init__(self, value):
        """Constructor for the Node class.

        Attributes
        ======
            value : int, float, np.int32, np.int64
                The value of the Node
            gradient : int, float, np.int32, np.int64
                The gradient of the Node with respect to the derivative and child Nodes
            children : list of Nodes
                A list of tuples (derivative, child) representing the derivative and children of the Node
        """
        self.value = value
        self.gradient = None
        self.children = []
    
    def grad(self):
        """Calculate the gradient of a Node using the chain rule.
        
        Returns
        ======
        int, float
            The gradient of a Node with respect to its children
            
        Examples
        =======
        # Create a Node and its child, then calculate the gradient
        >>> x = Node(2)
        >>> y = x**3
        >>> print(x.grad())
        0
        >>> print(y.grad())
        6
        """
        # Recursively find gradient if the gradient is none
        if self.gradient is None: 
            # Calculate derivative using chain rule
            self.gradient = sum([derivative * child.grad() for derivative, child in self.children])
        return self.gradient
    
    def clear(self):
        """Clears a Node to a state of no children or gradient stored."""
        # Reset attributes of a Node object to re-use as an input in new function
        self.children = []
        self.gradient = None

    def __add__(self, other):
        """Compute the sum of two Nodes or a Node and a number.

        Parameters
        ======
        self : Node
            The Node to add
        other : int, float, np.int32, np.int64, or Node
            The Node or number to add

        Returns
        =======
        Node
            The sum of two Nodes or a Node and a number

        Examples
        =======
        # Compute the sum of two Nodes
        >>> x = Node(3)
        >>> y = Node(4)
        >>> z = x + y
        >>> print(z.value)
        7
        # Compute the sum of a Node and a number
        >>> x = Node(3)
        >>> z = x + 2
        >>> print(z.value)
        5
        """
        # Support for Node type
        if isinstance(other, Node):
            # Update children of nodes
            z = Node(self.value + other.value)
            self.children.append((1, z))
            other.children.append((1, z))
        # Return error if not a support type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for addition"
            )
        # Support for scalar type
        else:
            # Update children of node
            z = Node(self.value + other)
            self.children.append((1, z))
        return z 

    def __radd__(self, other):
        """Compute the sum of a number and a Node.

        Parameters
        ======
        self : Node
        other : int, float, np.int32, np.int64

        Returns
        =======
        Node
            The sum of a Node and a number

        Examples
        =======
        # Compute the sum of a number and a Node
        >>> x = Node(3)
        >>> z = 2 + x
        >>> print(z.value)
        5
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Calculates the subtraction two Nodes or a number from a Node.

        Parameters
        ======
        self : Node
        other : Node, int, float, np.int32, or np.int64

        Returns
        =======
        Node
            The subtraction of two Nodes or a number from a Node

        Examples
        =======
        # Compute the subtraction of two Nodes
        >>> x = Node(3)
        >>> y = Node(4)
        >>> z = x - y
        >>> print(z.value)
        -1
        # Compute the sum of a Node and a number
        >>> x = Node(3)
        >>> z = x - 2
        >>> print(z.value)
        1

        Raises
        =======
        TypeError: Type `[input type]` is not supported for addition
        """
        # Support for Node type
        if isinstance(other, Node):
            # Update children of nodes
            z = Node(self.value - other.value)
            self.children.append((1, z))
            other.children.append((-1, z))
        # Return error if not a support type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for addition"
            )
        # Support for scalar type
        else:
            # Update children of node
            z = Node(self.value - other)
            self.children.append((1, z))
        return z

    def __rsub__(self, other):
        """Calculates the subtraction of a Node from a number.

        Parameters
        ======
        self : Node
        other : int, float, np.int32, or np.int64

        Returns
        =======
        Node
            The subtraction of a Node from a number

        Examples
        =======
        # Compute the sum of a Node and a number
        >>> x = Node(3)
        >>> z = 2 - x
        >>> print(z.value)
        -1

        Raises
        =======
        TypeError: Type `[input type]` is not supported for subtraction
        """
        return -1*self.__sub__(other)

    def __mul__(self, other):
        """Calculates the product of two Nodes or a Node and a number.

        Parameters
        ======
        self : Node
        other : Node, int, float, np.int32, or np.int64

        Returns
        =======
        Node
            The multiplication of two Nodes or a Node and a number

        Examples
        =======
        # Compute the product of two Nodes
        >>> x = Node(3)
        >>> y = Node(4)
        >>> z = x * y
        >>> print(z.value)
        12
        # Compute the product of a Node and a number
        >>> x = Node(3)
        >>> z = x * 2
        >>> print(z.value)
        6

        Raises
        =======
        TypeError: Type `[input type]` is not supported for multiplication
        """        
        # Support for Node type
        if isinstance(other, Node):
            z = Node(self.value * other.value)
            # Update children of nodes
            self.children.append((other.value, z))
            other.children.append((self.value, z))
        # Return error if not a support type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for multiplication"
            )
        # Support for scalar type
        else:
            # Update children of node
            z = Node(self.value * other)
            self.children.append((other, z))
        return z 
    
    def __rmul__(self, other):
        """Calculates the product of a Node and a number.

        Parameters
        ======
        self : Node
        other : int, float, np.int32, or np.int64

        Returns
        =======
        Node
            The multiplication of a Node and a number

        Examples
        =======
        # Compute the product of a Node and a number
        >>> x = Node(3)
        >>> z = 2 * x
        >>> print(z.value)
        6

        Raises
        =======
        TypeError: Type `[input type]` is not supported for multiplication
        """
        return self.__mul__(other)

    def __pow__(self, other):
        """Calculation of a Node to the power of a number or a Node.

        Parameters
        ======
        self : Node
        other : Node, int, float, np.int32, or np.int64

        Returns
        =======
        Node
            Node raised to the power of a number or a Node

        Examples
        =======
        # Compute a Node raised to the power of a Node
        >>> x = Node(3)
        >>> y = Node(2)
        >>> z = x ** y
        >>> print(z.value)
        9

        # Compute a Node raised to the power of a number
        >>> x = Node(3)
        >>> z = x * 2
        >>> print(z.value)
        9

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """
        # Support for Node type
        if isinstance(other, Node):
            # Update children of nodes
            z = Node(self.value ** other.value)
            self.children.append((other.value * self.value ** (other.value - 1), z))
            other.children.append((self.value ** other.value * np.log(self.value), z))
        # Return error if not a support type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for powers"
            )
        # Support for scalar type
        else:
            # Update children of node
            z = Node(self.value ** other)
            self.children.append((other * self.value ** (other - 1), z))
        return z 
        
    def __rpow__(self, other):
        """Calculation of a number raised to the power of a Node.

        Parameters
        ======
        self : Node
        other : int, float, np.int32, or np.int64

        Returns
        =======
        Node
            Number raised to the power of a Node

        Examples
        =======
        # Compute a Node raised to the power of a number
        >>> x = Node(3)
        >>> z = 2 ** x
        >>> print(z.value)
        8

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """
        z = Node(other ** self.value)
        # Update children of node
        self.children.append((other ** self.value * np.log(other), z))
        return z 

    def __truediv__(self, other):
        """Calculation of a Node divided by a Node or a number.

        Parameters
        ======
        self : Node
        other : Node, int, float, np.int32, or np.int64

        Returns
        =======
        Node
            Node divided by a Node or a number

        Examples
        =======
        # Compute a Node divided by a Node
        >>> x = Node(2)
        >>> y = Node(4)
        >>> z = x / y
        >>> print(z.value)
        0.5

        # Compute a Node divided by a scalar
        >>> x = Node(2)
        >>> z = x / 2
        >>> print(z.value)
        1.0

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """
        # Support for Node type
        if isinstance(other, Node):
            # Update children of nodes
            z = Node(self.value / other.value)
            self.children.append((1 / other.value, z))
            other.children.append((-self.value / (other.value)**2, z))
        # Return error if not a support type
        elif not isinstance(other, self._supported_types):
            raise TypeError(
                f"Type `{type(other)}` is not supported for division"
            )
        # Support for scalar type
        else:
            # Update children of node
            z = Node(self.value / other)
            self.children.append((1 / other, z))
        return z 

    def __rtruediv__(self, other):
        """Calculation of a number divided by a Node.

        Parameters
        ======
        self : Node
        other : int, float, np.int32, or np.int64

        Returns
        =======
        Node
            Number divided by a Node

        Examples
        =======
        # Compute a scalar divided by a Node
        >>> x = Node(2)
        >>> z = 2 / x
        >>> print(z.value)
        1.0

        Raises
        =======
        TypeError: Type `[input type]` is not supported for powers
        """
        z = Node(other / self.value)
        # Update children of node
        self.children.append((-other / (self.value)**2, z))
        return z

    def __neg__(self):
        """Calculation of the negative of a Node.

        Parameters
        ======
        self : Node

        Returns
        =======
        z : Node
            Negative of a Node

        Example
        =======
        # Testing negative of integer
        >>> x = Node(1)
        >>> z = -x
        >>> print(z.value)
        -1
        """
        z = Node(-self.value)
        # Update children of node
        self.children.append((-1, z))
        return z
    
    def __pos__(self):
        """Calculation of the positive of a Node.

        Parameters
        ======
        self : Node

        Returns
        =======
        z : Node
            Positive of a Node

        Example
        =======
        # Testing positive of integer
        >>> x = Node(1)
        >>> z = +x
        >>> print(z.value)
        1.0
        """
        z = Node(self.value)
        # Update children of node
        self.children.append((1, z))
        return z 
    
