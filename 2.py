


depth = 0
h = 0
aim = 0
with open("2") as f:
    for i in f:
        cmd,n = i.strip().split()
        n = int(n)

        if cmd == "forward":
            h += n
            # depth += aim * n
        elif cmd == "up":
            # aim -= n
            depth += n 
        else:
            # aim += n
            depth -= n 
print(h*depth,h,depth)

# d={};[d[i]:=d[i]+int(v)for i,v in map(str.split,open("2")))]
# d={};[d.__setitem__(i[0],d.get(i[0],0)+int(v))for i,v in map(str.split,open("2"))]
# d={i:0for i in"fud"};[d.__setitem__(i[0],d[i[0]]+int(v))for i,v in map(str.split,open("2"))]
#sum(i[0]!="f"and (ord(i[0])//9-12)*int(v)or 0for i,v in map(str.split,open("2")))
#sum(i[0]!="f"and ((i[0]=="u")*2-1)*int(v)or 0for i,v in map(str.split,open("2")))
#f=0;sum(i[0]!="f"and((i[0]!="u")*2-1)*int(v)or(f:=f+int(v))*0for i,v in map(str.split,open("2")))*f
#f=0;print(sum(i[0]!="f"and int("-"*(i!="up")+v)or(f:=f+int(v))*0for i,v in map(str.split,open("2")))*f)
#f*(u-d)
#fu-fd
#(f+1)u-(f+1)d
#fu-fd+u-d
#f ord=102 int36 15  == 1j
#d ord=100 int36 13 == -1
#u ord=117 int36 30 == 1

#sum(({'f':1j,'d':1,'u':-1}[A.split()[0][0]]*int(A.split()[1])map(str.split, open('2'))));print(A.real*A.imag)
A=sum(({'f':1j,'d':1,'u':-1}[A[0][0]]*int(A.split()[1][0])for A in open('1')))
print(A.real*A.imag)
f=0;print(sum(i[0]!="f"and int("-"*(i=="up")+v)or(f:=f+int(v))*0for i,v in map(str.split,open("2")))*f)
#print((sum(({'f':1j,'d':1,'u':-1}[A[0]]*int(A.split()[1])for A in open('a')))**2).imag/2)
print((sum(({'f':1j,'d':1,'u':-1}[A[0]]*int(A.split()[1])for A in open('a')))**2).imag/2)
print((sum({'f':1j,'d':1,'u':-1}[A[0]]*int(A.split()[1])for A in open('a'))**2).imag/2)
print((sum(dict(f=1j,d=1,u=-1))[A[0]]*int(A.split()[1])for A in open('a'))**2).imag/2)
print((sum((int((ord(A[0])-108)/8)or 1j)*int(A.split()[1])for A in open('a'))**2).imag/2)


#f    u   d
#102 117 100
#1j   1  -1
