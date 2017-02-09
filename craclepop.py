pop = "Pop"
cracle = "Cracle"
for i in range(1, 101):
    if i % 15 == 0:
        print(cracle + pop)
    elif i % 3 == 0:
        print(cracle)
    elif i % 5 == 0:
        print(pop)
    else:
        print(i)
