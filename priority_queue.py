import sys
from operator import methodcaller


class PriorityQueue(object):

    def __init__(self):
        self.queue = []
        self.vals = []
        self.output = []
        line = sys.stdin.readline()
        self.operations = int(line.strip())
        self.read_input()
        self.perform_operations()
        self.get_output()

    def read_input(self):
        for i in range(self.operations):
            line = sys.stdin.readline()
            operation = line.strip().split(' ')
            self.queue.append(operation)

    def perform_operations(self):
        for operation in self.queue:
            if len(operation) > 1:
                func, val = operation
                m = methodcaller(func.lower(), int(val))
                m(self)
            else:
                func = operation[0]
                m = methodcaller(func.lower())
                self.output.append(str(m(self)))

    def get_output(self):
        sys.stdout.write('\n'.join(self.output))

    def insert(self, val):
        self.vals.append(val)

    def extractmax(self):
        to_return = max(self.vals)
        self.vals.remove(to_return)
        return to_return

queue = PriorityQueue()
