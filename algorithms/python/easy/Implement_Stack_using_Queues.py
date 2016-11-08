#! /env/bin/python2
# coding=utf-8

import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input_queue = Queue.Queue()
        self.output_queue = Queue.Queue() 
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input_queue.put(x)
        
        

    def pop(self):
        """
        :rtype: nothing
        """
        length = self.input_queue.qsize()
        if (length > 1):
            while(self.input_queue.qsize() != 1):
                self.output_queue.put(self.input_queue.get())
            
            self.input_queue = self.output_queue
            self.output_queue = Queue.Queue()
        elif (length == 1):
            self.input_queue.get()
        

        

    def top(self):
        """
        :rtype: int
        """
        length = self.input_queue.qsize()
        if (length > 1):
            while(self.input_queue.qsize() != 1):
                self.output_queue.put(self.input_queue.get())

            x = self.input_queue.get()
            self.output_queue.put(x)
            
            self.input_queue = self.output_queue
            self.output_queue = Queue.Queue()
            
        elif (length == 1):
            x = self.input_queue.get()
            self.input_queue.put(x)
        
        return x
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.input_queue.qsize() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Stack()
    if a.empty():
        print "True"
    else:
        print "False"