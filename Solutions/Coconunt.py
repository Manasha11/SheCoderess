inp = raw_input().split(' ');
l = []
connected = []
trees = int(inp[0])
cables = int(inp[1])
#print cables
for i in range(0,trees):
    l.append(i+1)
for j in range(0,cables):
    cab = raw_input().split(' ')
    #print cab[0]
    #print cab[1]
    #print(cab[1] in connected)
    if (connected==[] or int(cab[0]) in connected or int(cab[1]) in connected):
        #print cab[0]
        #print cab[1]
        connected.append(int(cab[0]))
        connected.append(int(cab[1]))
        #print connected

q = int(raw_input())
for k in range(0,q):
    chk = raw_input().split(' ')
    if(int(chk[0]) in connected and int(chk[1]) in connected):
        print("YES")
    else:
        print("NO")
                
