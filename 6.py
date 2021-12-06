l = [*map(int,next(open("6")).split(","))]
for i in range(80):
    k = []
    l = [*map(lambda x: x-1 if x > 0 else (k.append(8)or 6),l)] + k
    print(len(l))
