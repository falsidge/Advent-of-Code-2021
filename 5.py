sz = 1000
graph = [[0]*sz for i in range(sz)]
with open("5") as f:
    for i in f:
        cords = [*map(lambda x:tuple(map(int,x.strip().split(","))),i.split(" -> "))]
        cords = sorted(cords)
        if cords[0][0] == cords[1][0] or cords[0][1] == cords[1][1]:
            # print(cords)
            # if cords[0][0] == cords[1][0]:
            #     x = cords[0][0]
            for x in range(cords[0][0], cords[1][0] + (1 if cords[1][0] >= cords[0][0] else -1), 1 if cords[1][0] >= cords[0][0] else -1):
                # print(x)
                # print(cords[0][1], cords[1][1] + (1 if cords[1][1] >= cords[0][1] else -1), 1 if cords[1][1] > cords[0][1] else -1)
                for y in range(cords[0][1], cords[1][1] + (1 if cords[1][1] >= cords[0][1] else -1), 1 if cords[1][1] >= cords[0][1] else -1):
                    # print(x,y)
                    graph[y][x] += 1
        # print("sub",cords[0][0] - cords[0][1] ,   -cords[1][0] + cords[1][1])
        if (cords[1][1]-cords[0][1]  ==   cords[1][0] - cords[0][0]):
            for x in range(0, cords[1][0] - cords[0][0]+ 1, 1):
                # print(cords, x, 't')
                graph[cords[0][1] + x][cords[0][0] + x] += 1
        elif (-cords[1][1]+cords[0][1]  ==   cords[1][0] - cords[0][0]):
            for x in range(0, cords[1][0]-cords[0][0] + 1, 1):
                # print(x)
                # print(cords, x, 'b')
                graph[cords[0][1] - x][cords[0][0] + x] += 1
mx = 0
tot = 0
for y in graph:
    for x in y:
        if x >= 2:
            tot += 1
            # mx = x
            # print(mx)

    print(y)
print(tot)