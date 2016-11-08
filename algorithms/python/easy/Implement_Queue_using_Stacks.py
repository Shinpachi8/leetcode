
"""
coafadfljalkf
"""


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Queue()
    a.push(1)
    a.push(2)
    print a.peek()
    print __doc__