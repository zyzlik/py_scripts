import sys


s = sys.stdin.readline().strip()
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

count = 0

if a not in s:
    sys.stdout.write(str(count))
    sys.exit()

new_s = s.replace(a, b)
if s == new_s or a in b:
    sys.stdout.write('Impossible')
    sys.exit()

while s != new_s:
    old_s = s
    s = new_s
    new_s = new_s.replace(a, b)
    print new_s + '\n'
    print old_s
    if old_s == new_s:
        sys.stdout.write('Impossible')
        sys.exit()
    count += 1

sys.stdout.write(str(count))
