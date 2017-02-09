inp = 'ACGT'
out = ['00', '01', '10', '11']
print(input().translate(dict(zip(map(ord, inp), out))))
