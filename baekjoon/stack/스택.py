import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not len(self.items) == 0:
            print(self.items.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.items))

    def empty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if not len(self.items) < 1:
            print(self.items[-1])
        else:
            print(-1)


T = int(input())
stack = Stack()
for t in range(T):
    command = list(input().split())

    if command[0] == 'push':
        stack.push(command[1])

    elif command[0] == 'pop':
        stack.pop()

    elif command[0] == 'size':
        stack.size()

    elif command[0] == 'empty':
        stack.empty()

    elif command[0] == 'top':
        stack.top()