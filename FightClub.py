isValid = False
l = ["fightclub.uk", "fightclub.com", "fightclub.lk", "fightclub.sa", "fightclub.cc", "fightclub.jp", "fightclub.se", "fightclub.xy", "fightclub.gi", "fightclub.rl", "fightclub.ss"]
t = int(raw_input())

#def hasNumbers(inputString):
#    return bool(re.search(r'\d', inputString))

for i in range(0,t):
    inp = raw_input()
    tokens = inp.split("@")
    if(len(tokens)==2):
        if(tokens[1] in l):
            if(len(tokens[0])>=3 and len(tokens[0])<=6):
                if(tokens[0].islower()):
                   if(tokens[0].isalnum()):
               
                        isValid = True
    if(isValid):
        print("VALID")
    else:
        print("INVALID")
    isValid=False
