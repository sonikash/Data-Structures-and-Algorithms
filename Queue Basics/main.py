from collections import deque

class Queue:
    def __init__(self):
        self.qu = deque()

    def enqueue(self, item):
        self.qu.appendleft(item)

    def dequeue(self):
       return self.qu.pop()

    def is_empty(self):
        return len(self.qu)==0

    def size(self):
        return len(self.qu)

if __name__ == '__main__':
    qu=Queue()
    qu.enqueue({'company':'Walmart', 'Time stamp': '12:30 PM', 'Price': 132})
    qu.enqueue({'company':'Walmart', 'Time stamp': '12:31 PM', 'Price': 132.12})
    qu.enqueue({'company':'Walmart', 'Time stamp': '12:32 PM', 'Price': 130.9})
    qu.enqueue({'company':'Walmart', 'Time stamp': '12:33 PM', 'Price': 131.1})
    print(qu.qu)
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())




