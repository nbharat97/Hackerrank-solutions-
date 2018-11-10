import math
a=[]
s = input()
s = s.replace(" ","")
print(s)
l = len(s)

r = math.floor(math.sqrt(l))
c = math.ceil(math.sqrt(l))
k = 0
for i in range(0,r):
    for j in range(0,c):
        if (k <= l):
            print(s[k], end = "")
            k = k + 1
    print(" ")
        
