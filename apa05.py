l=open("apa05input.txt","r").readlines()
pts = list(map(int, l[0].split(":")[1].split()))
print(pts)
newpts = []
for m in l[1:]:
    if ":" in m or " " not in m:
        print("-"*20)
        pts=newpts+pts
        newpts=[]
        print(pts)
        continue
    b, a, r = map(int, m.split())
    oldpts=[]
    for p in pts:
        if p in range(a,a+r):
            newpts.append(p+b-a)
        else:
            oldpts.append(p)
    pts=oldpts
print(min(pts))
