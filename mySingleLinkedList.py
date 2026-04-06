class MySinglyLinkedList:
    
    class _Node:
        def __init__(self, element, next_node=None):
            self.element = element
            self.next = next_node

    def __init__(self):
        self._head = None   # erstes Element
        self._tail = None   # letztes Element (NEU)
        self._size = 0      # Anzahl der Elemente

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            return None
        return self._head.element

    # Laufzeit: O(1)
    def add_first(self, e):
        new_node = self._Node(e, self._head)
        self._head = new_node

        # wenn Liste vorher leer war → neues Element ist erstes UND letztes
        if self._size == 0:
            self._tail = new_node

        self._size += 1

    # Laufzeit: O(1)
    def remove_first(self):
        if self.is_empty():
            return None

        value = self._head.element
        self._head = self._head.next
        self._size -= 1

        # wenn Liste leer wird → tail zurückgesetz
        if self._size == 0:
            self._tail = None

        return value

    # NEU: letztes Element anzeigen
    # Laufzeit: O(1) (wegen self.tail kein Durchlaufen mehr nötig sonst wäre es O(n)
    def last(self):
        if self.is_empty():
            return None
        return self._tail.element

    # NEU: Element am Ende hinzufügen
    # Laufzeit: O(1) (wegen self.tail kein Durchlaufen mehr nötig sonst wäre es O(n) )
    def add_last(self, e):
        new_node = self._Node(e)

        if self.is_empty():
            # erstes Element in der Liste
            self._head = new_node
            self._tail = new_node
        else:
            # direkt hinten anhängen
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

