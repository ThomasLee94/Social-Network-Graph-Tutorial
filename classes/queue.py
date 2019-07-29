#!python

from classes.linkedlist import LinkedList, Node 

class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self) -> bool:
        """Return True if this queue is empty, or False otherwise."""
        # is_empty() is ll class method
        return self.list.is_empty()
    
    def length(self) -> int:
        """Return the number of items in this queue."""
        # length() is a ll class method
        return self.list.length()

    # ─── HEAD IS FRONT ──────────────────────────────────────────────────────────────

    # ─── TAIL IS BACK ───────────────────────────────────────────────────────────────

    def enqueue(self, item):
        """Insert the given item at the back of this queue."""
        # ! Best & worst runtime = O(1), is not dependent on length of queue

        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""

        if self.list.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty."""
        # ! Worst & best case runtime = O(1), not dependent on length of ll
        
        # case: no nodes
        if self.list.length() < 1:
            raise ValueError("No available nodes")
        # case: empty dequeue
        if self.list.is_empty():
            raise ValueError("Linked list is empty")
        # store data
        output_data = self.front()
        # delete node containing that data
        self.list.delete(output_data)
        # return data
        return output_data

