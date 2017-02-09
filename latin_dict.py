import sys


dct = {}
num_words = int(sys.stdin.readline())

for i in range(num_words):
    line = sys.stdin.readline().strip().split(' - ')
    sp_word = line[0]
    lat_words = line[1].split(', ')
    for word in lat_words:
        if not dct.get(word):
            dct[word] = {sp_word}
        else:
            dct[word].add(sp_word)

sys.stdout.write(str(len(dct)))
sys.stdout.write('\n')
for word in sorted(dct):
    sys.stdout.write(word)
    sys.stdout.write(' - ')
    sys.stdout.write(', '.join(sorted(dct[word])))
    sys.stdout.write('\n')
