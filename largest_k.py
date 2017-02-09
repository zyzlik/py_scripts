# This is Python 2
import sys

line = sys.stdin.readline()
index = int(line.split(' ')[-1])

line = sys.stdin.readline()
lst = line.replace('\n', '').split(' ')
lst = map(int, lst)
lst.sort()
result = lst[index - 1]
sys.stdout.write(str(result))
