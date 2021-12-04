increases = 0
with open("1") as f:
    lines = list(map(int, f.readlines()))
    for i,j in zip(lines[3:],lines):
        if i > j:
            increases += 1
print(increases)

#sum(y>x for x,y in zip(open(i),(lambda k:next(k) and k)((open(i)))))
#from itertools import *;sum(map(max,pairwise(open("1"))))
#from itertools import*;sum(starmap(int.__lt__,pairwise(map(int,open("1")))))
#71 bytes
#from itertools import*;sum(int(x)<int(y)for x,y in pairwise(open("1"))) 
#64 bytes
sum(int(y)>int(x)for x,y in zip(open("1"),[*open("1")])[1:])
#51 bytes
d=[*map(int,open("1"))];sum(i<j for i,j in d,d[1:])
sum(sum(map(int.__lt__,i,i))for i in[map(int,open("1")),d]) 
sum(i>j for j,i in[map(int,open("1"))]*2)

sum(v>d[i+1]for i,v in enumerate([*map(int,open("1"))]))
sum(map(int.__gt__,d:=[*map(int,open("1"))],d[1:]))
from itertools import*;

#part 2

#from collections import*;b=map(int,open("1"));a=deque((next(b),next(b),next(b)),3);p=sum(a);sum(a.append(i)or p<(p:=sum(a))for i in b)
#from collections import*;p=sum(a:=deque((next(b:=map(int,open("1"))),next(b),next(b)),3));sum(a.append(i)or p<(p:=sum(a))for i in b)
#p=next(b:=map(int,open("1")))+next(b)+next(b);sum(a.append(i)or p<(p:=sum(a))for i in b)
#
# 97 bytes
# p=next(b:=map(int,open("1")))+next(b)+next(b);sum((p<(p:=p+i-int(j)))for j,i in zip(open("1"),b))
#p=sum(map(lambda x:int(x[0]),zip(b:=open("1"),range(3))));sum((p<(p:=p+i-int(j)))for j,i in zip(open("1"),b))
#p=sum((b:=list(map(int,open("1"))))[:3]);sum((p<(p:=p+i-int(j)))for j,i in zip(open("1"),b[3:]))
sum(int(j)>int(i)for j,i in zip(open("1"),[*open("1")][3:]))
#p=sum((b:=list(map(int,open("1"))))[:3]);sum((p<(p:=p+i-int(j)))for j,i in zip(open("1"),b[3:]))
#a,b,c,d
#b+c+d>a+b+c => d>a, 
#e+c+d > b+c+d =>e>b
