"""
On the input, the algorithm has a string containing the characters
of the Latin alphabet. This string is split into the so-called "series",
which are encoded by a number-symbol pair or just a symbol (in this case,
the number is considered equal to one). The result must contain the
series in the same order, in which they occur in the original string,
and each series is disclosed into the sequence of characters of a
corresponding length.
"""

from re import sub


lst = []
res = []
s = input()
for char in s:
    if char.isdigit():
        lst.append(char)
    else:
        if lst:
            repeat = int(''.join(lst))
        else:
            repeat = 1
        lst = []
        res.append(char * repeat)
print(''.join(res))

# another solution

print(sub(r'(\d+)(\D)', lambda x: x.group(2) * int(x.group(1)), input()))

# another solution

s, ans, n = input(), '', ''
for i in s:
    if i.isnumeric():
        n += i
    else:
        ans += i * int(n) if len(n) else i
        n = ''
print(ans)
