class SllNode:
    def __init__(self, element, next_node=None):
        self.element = element
        self.next = next_node


class MySinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):        
        return None if self.is_empty() else self._head.element

    """
    continue here ...
    """


#----------Double Linked List---------------#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Liste ist leer")
        return self._head.data

    def last(self):
        if self.is_empty():
            raise Exception("Liste ist leer")
        return self._tail.data

    def add_first(self, e):
        new_node = Node(e)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def add_last(self, e):
        new_node = Node(e)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("Liste ist leer")
        data = self._head.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return data

    def remove_last(self):
        if self.is_empty():
            raise Exception("Liste ist leer")
        data = self._tail.data
        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return data


#----------------------------------#



def compute(postfix_expression):
    """
    Evaluate a postfix (Reverse Polish Notation) arithmetic expression.

    Args:
        postfix_expression: A string containing integers and operators (+, -, *, /)
                           separated by whitespaces. Example: "3 4 + 2 * 7 /"

    Returns:
        The computed result as an int or float.

    Raises:
        ValueError: If the expression is invalid or malformed.
        ZeroDivisionError: If division by zero is attempted.
    """
    # Create an appropriate stack
    stack = None

    # Split the expression into tokens
    tokens = postfix_expression.split()

    if not tokens:
        raise ValueError("Empty expression")

    for token in tokens:
        # Check if token is an operator
        if token in ['+', '-', '*', '/']:
            pass
            # ...
        else:
            pass
            # ...

    #...
    return stack.first()

if __name__ == "__main__":
    # Quick manual checks for the standalone postfix evaluator.
    examples = [
        "3 4 + 2 * 7 /",
        "5 1 2 + 4 * + 3 -",
    ]

    for expr in examples:
        print(f"{expr} = {compute(expr)}")
