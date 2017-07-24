import math
t = int(raw_input())
for j in range(0,t):
    inp = raw_input()
    n = 0
    for char in inp:
        if char in "aeiouAEIOU":
            n = n+1
    #print n
    if n%2 == 0 and n <= math.sqrt(len(inp)):
        print "YES"
    else:
        print "NO"
    

