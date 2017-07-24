l=[]
o=[]
t = int(raw_input())
for i in range(0,t):
    inp = raw_input()
    n = len(inp)
    i=0
    while(n>=8):
        l.append(inp[i:i+8])
        i=i+8
        n=n-8
    for j in l:
        o.append(str(unichr(int(j,2))))
    str1=''.join(str(e) for e in o)
    print(str1)
    o=[]
    l=[]


