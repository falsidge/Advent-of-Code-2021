l=[]

counts = [
0,
]*9
with open("6") as f:
    l = [*map(int,f.read().split(","))]
    for i in range(7):
        counts[i] = l.count(i)
    for k in range(256):
        nc = list(counts)
        for j in range(1,9):
            nc[j-1] = counts[j]
        nc[8] = counts[0]
        nc[6] = counts[0] + nc[6]
        counts = nc 
    print(counts, sum(nc))
    # for i in range(256):
    #     k = []
    #     l = [*map(lambda x: x-1 if x > 0 else (k.append(8)or 6),l)] + k
    #     print(len(l))
