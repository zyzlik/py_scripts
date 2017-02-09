import sys

from functools import reduce

line = sys.stdin.readline()
line = line.split()
result = reduce(lambda x, y: x + y, [int(i) if i.isdigit() else 0 for i in line])
sys.stdout.write(str(result))
