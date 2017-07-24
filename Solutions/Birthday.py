candles = int(raw_input())
h = raw_input().split(' ')
h.sort(reverse=True)
#print h
count = 1
for i in range (0,candles):
    if int(h[i]) == int(h[i+1]):
        count=count+1
    else:
        break
print count
