st = input()
to_find = input()
s = set()


for i in range(len(st)):
    index = st.find(to_find, i)
    if index != -1:
        s.add(index)

print(len(s))
