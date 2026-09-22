from collections import deque


class FCFSQueue:
    """
    First-Come, First-Served queue for request processing.
    """

    def __init__(self):
        self.queue = deque()

    def enqueue(self, request):
        """Add a request to the back of the queue."""
        self.queue.append(request)

    def dequeue(self):
        """Remove and return the oldest request."""
        if self.is_empty():
            return None
        return self.queue.popleft()

    def peek(self):
        """Return the oldest request without removing it."""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of requests waiting."""
        return len(self.queue)