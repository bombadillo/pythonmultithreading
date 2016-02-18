import Queue
from modules.worker import Worker

WORKERS = 2

queue = Queue.Queue(0)

for i in range(WORKERS):
    Worker(queue).start() 

for i in range(10):
    queue.put(i)

for i in range(WORKERS):
    queue.put(None)
