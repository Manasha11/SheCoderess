numOfFruits = int(raw_input());
strings = raw_input();
arr=strings.split();

count=1
for i in range (0,len(arr)):
    n=1
    for j in  range (1,len(arr)):
        for k in range (0,4):
            if arr[j]==arr[i]+k:
                arr.pop(j);
                break;

print(count)

##num = int(raw_input())
##weights = raw_input().split(' ')
##weights.sort()
##l =[]
##units = 1
##
##while(weights!=[]):
##    for i in range(int(weights[0]),int(weights[0])+5):
##        l.append(int(weights[0])+i+1)
##    for j in weights:
##        if int(j) in l:
##            weights.pop(weights.index(j))
##    units=units+1
##print units
