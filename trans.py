"""
Input: string message containing only char A, C, G, T
Output: string with these char replaced by codes 00, 01, 10, 11 respectively
"""


inp = 'ACGT'
out = ['00', '01', '10', '11']
print(input().translate(dict(zip(map(ord, inp), out))))
