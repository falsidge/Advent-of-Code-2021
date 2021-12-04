le = len("110000100111")
counts =  [0]*le
with open("3") as f:
    for l in f:
        l = int(l.strip(),2)
        for i in range(le):
            counts[i] += (l >> i) & 1 
print(counts)
c= int("".join(reversed(list(map(lambda x: "01"[x>500], counts)))),2)
print(c,bin(c))
print(bin(2**le -1 - c))
print((2**le -1 - c)*c)

#13min 20s

(a:=int(b:="".join(map("01".__getitem__,map((len([*open("3")])/2).__lt__,[sum(i)for i in zip(*map(lambda x:[*map("1".__eq__,x)],open("3")))]))),2))*(2**len(b)-1-a)
map((len([*open("3")])/2).__lt__,[sum(i)for i in zip(*map(lambda x:[*map("1".__eq__,x)],open("3")))])



print((a:=int(b:="".join(map(lambda x:"01"[x.count("1")>len(x)/2],zip(*open("3")))),2))*(2**len(b)-1-a))
