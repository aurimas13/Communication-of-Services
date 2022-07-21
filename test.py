from queue import Queue
import random
import threading
import multiprocessing as mp

MAX_QSIZE = 10  # max queue size
BUFF_SIZE = 100  # total number of iterations/items to process


class Producer:
    def __init__(self, queue, buff_size=BUFF_SIZE):
        self.queue = queue
        self.buff_size = buff_size

    def run(self):
        for _ in range(self.buff_size):
            self.queue.put(random.randint(0, 100))


class Consumer:
    def __init__(self, queue):
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            item = self.queue.get()
            self.queue.task_done()
            print(item)


def main():
    q = Queue(maxsize=MAX_QSIZE)

    producer = Producer(q)
    producer_thread = threading.Thread(target=producer.run)

    consumer = Consumer(q)
    consumer_thread = threading.Thread(target=consumer.run)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    q.join()

if __name__ == "__main__":
    main()