def kind(cs):
    return sum(sum(x==c for x in cs)for c in cs)

def val(c):
    return 36*"TJQKA".find(c)+int(c,36)

def hand(cs):
    return [kind(cs),*map(val,cs)]
    
l = open("apa07input.txt","r").readlines()
v=[(hand(s[0]),int(s[1]))for s in map(str.split,l)]
print(sum((i+1)*x[1] for i,x in enumerate(sorted(v))))
