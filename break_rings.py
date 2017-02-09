def break_rings(rings):
    d = {}
    rings = list(rings)
    destroyed = 0
    for pair in rings:
        for ring in pair:
            if ring in d:
                d[ring] += 1
            else:
                d[ring] = 1
    s = sorted(d.items(), key=lambda (k, v): v, reverse=True)

        
    for i in s:
        flag = False
        for pair in rings:
            if i[0] in pair:
                rings.remove(pair)
                flag = True
            else:
                flag = False
        if flag:
            destroyed += 1


    return destroyed





rings = ({1,2},{1,3},{1,4},{2,3},{2,4},{3,4},)
print break_rings(rings)    