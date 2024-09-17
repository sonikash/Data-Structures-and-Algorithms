from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.qu = deque()

    def enqueue(self, item):
        self.qu.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            return self.qu.pop()
        else:
            return None


    def is_empty(self):
        return len(self.qu)==0

    def place_order(self,queue,orders,stop_event):
        index=0
        while not stop_event.is_set():
            order = orders[index]
            queue.enqueue(order)
            print(f"order placed:{order}")
            index = (index+1)%len(orders)
            time.sleep(0.5)


    def serve_order(self, queue,stop_event):
        while not stop_event.is_set() or not queue.is_empty():
            time.sleep(2)
            if not queue.is_empty():
                order = queue.dequeue()
                print(f"Order is served:{order}")

            else:
                print("No orders to Serve")

if __name__ == '__main__':
    qu=Queue()
    Order=['Pizza','Burger','Biryani','Sandwhich','Noodles']
    stop_event=threading.Event()
    t1 = threading.Thread(target=qu.place_order, args=(qu,Order,stop_event,))
    t2 = threading.Thread(target=qu.serve_order, args=(qu, stop_event,))
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(10)
    stop_event.set()
    t1.join()
    t2.join()


