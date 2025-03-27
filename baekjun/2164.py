import sys

class Queue:
    first = 0
    next = 0
    queue = []

    @classmethod
    def initqueue(cls, n):
        cls.queue = list(range(1, n + 1))

    @classmethod
    def enqueue(cls, n):
        if cls.next < len(cls.queue):
            cls.queue[cls.next] = n
            cls.next += 1

    @classmethod
    def dequeue(cls):
        cls.first += 1
        if cls.first >= len(cls.queue):
            cls.first = 0 

    @classmethod
    def changequeue(cls):
        cls.queue.append(cls.queue[cls.first])
        cls.dequeue()

    @classmethod
    def printqueue(cls):
        print(cls.queue[cls.first])

# 입력값 받기
n = int(sys.stdin.readline())
Queue.initqueue(n)

for i in range(n - 2):
    Queue.dequeue()
    Queue.changequeue()

if n > 1:
    Queue.dequeue()

Queue.printqueue()