import numpy
def check(board):
    vert = [True] * len(board)
    for y in range(len(board)):
        hor = True
        for x in range(len(board)):
            if board[y][x] != 0:
                hor = False
                vert[x] = False
        if hor:
            return True
    if any(vert):
        return True

    return False
    any(all(map(0.__eq__,i))for i in board)

mint = 0
mini = 0
t= []
won = 0
with open("4") as f:
    called = map(str, f.readline().strip().split(","))
    called =[*called]
    print(called)
    t = f.read().split("\n\n")[1:]
    time = [0]*len(t)
    for ind, i in enumerate(t):
        board = []
        for j in i.split("\n"):
            board.append(list(filter(lambda x: x!=" ", j.split())))
        print(board)
        t[ind] = board
        for times, i in enumerate(called):
            for y in range(len(board)):
                for x in range(len(board)):
                    if board[y][x] == i:
                        board[y][x] = 0
            if check(board):
                time[ind] = times
                if times > mint:
                    mini = ind
                    mint = times
                    won = i
                break
tot = 0
board = t[mini]
print(board)
for i in range(len(t[0])):
    tot += sum(map(int, board[i]))
print(time, mini, mint, won, tot, int(won)*tot)
print(int(won)*tot)

any(all(map(isinstance,i,[int]*2*len(board)))for i in[*zip(*board)]+board)
any(all(map(isinstance,i,[int]*2*len(board)))for i in[*zip(*board)]+board)
any(all(map(lambda x:x==0,i))for i in[*zip(*board)]+board) # check_board

#f=open("4").read().split("\n\n");[*map(lambda t:[*map(lambda b:[*map(lambda c:c,map(int,f[0].split(",")))],map(str.split, t.split("\n")))],f)]
# f=open("4").read().split("\n\n");[*map(lambda t:[*map(lambda b:[*map(lambda c:(b:=[0 if x==c else x for x in b]),f[0].split(","))],map(str.split, t.split("\n")))],f)]
f=open("4").read().split("\n\n");[*map(lambda t:
[*map(lambda b:([0 if x==c else x for x in b]
) for c in f[0].split(","))],map(str.split, t.split("\n")))],f)]

#board map(str.split, t.split("\n")f
#f=open("4").read().split("\n\n");[*map(lambda t:[*map(lambda c:print(t:=t.replace()),map(int,f[0].split(",")))],f)]

map(b.split())
int.__class__
print(
check([
[0,1,0],
[1,1,"3"],
[0,"2","3"]
]
)
)


any(all(map(lambda x:x==0,i))for i in[*zip(*board)]+board)
