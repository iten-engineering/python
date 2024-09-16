import threading, time

class Queue(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.messages = []

    def send(self, message):
        with self.lock:
            self.messages.insert(0,message)

    def receive(self):
        with self.lock:
            if len(self.messages) > 0:
                return self.messages.pop()
            return None


"""
queue = Queue()

queue.send("Hello")
queue.send("World")

print( queue.receive())
print( queue.receive())

exit()
"""


def sender(queue, timeout):
    for i in range(10):
        msg = "Message" + str(i)
        queue.send(msg)
        time.sleep(timeout)
    queue.send("END")

def receiver(queue, timeout):
    msg = None
    while msg != "END":
        msg = queue.receive()
        if msg is not None:
            print("Received message:", msg)
        time.sleep(timeout)


queue = Queue()
sender_thread   = threading.Thread(target=sender,   args=(queue,1))
receiver_thread = threading.Thread(target=receiver, args=(queue,1))

sender_thread.start()
receiver_thread.start()

