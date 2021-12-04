from collections import defaultdict
le = len("110000100111")
le = 12
hl = len([*open("3")])//2

# 12 or 5
counts =  [0]*le
with open("3") as f:
    for l in f:
        l = int(l.strip(),2)
        for i in range(le):
            counts[i] += (l >> i) & 1 
print(counts)
c= int("".join(reversed(list(map(lambda x: "01"[x>5], counts)))),2)
print(c)
print(bin(2**le -1 - c))
print((2**le -1 - c)*c)
with open("3") as f:
    keep = [*map(str.strip, f)]
    keep2 = []
    
    
    for i in range(le):
        co = 0
        tot = 0
        for l in keep:
            co += int(l[i])
            tot += 1
        keep2 = list()
        print(co, co >= tot/2, tot)
        for l in keep:
            if int(l[i])  == (co < tot/2):
                keep2.append(l)
        print(keep, i)


        keep = keep2

print(keep)
#13min 20s
ans = list(keep)

# with open("3") as f:
#     keep = [*map(str.strip, f)]
#     keep2 = []
    
    
#     for i in range(le):
#         co = 0
#         tot = 0
#         for l in keep:
#             co += int(l[i])
#             tot += 1
#         keep2 = list()
#         # print(co)
        
#         for l in keep:
#             if int(l[i])  == (co < tot//2):
#                 keep2.append(l)
#         print(keep, i)
#         if len(keep2) == 1:
#             ans2 = keep2[0]
#         keep = keep2
# print(keep,ans, ans)

# #@4652538