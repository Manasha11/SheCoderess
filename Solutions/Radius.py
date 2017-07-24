n = int(raw_input())
l = [[]]
for i in range (0,n/2+1):
    rows = raw_input()
m=1
for j in rows:
    if "#" == j:
        break
    else:
        m=m+1
print(n/2-m+1)
