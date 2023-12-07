print(sum((i+1)*x[1]for i,x in enumerate(
sorted(([sum(sum(x==c for x in s)for c in
s),*map(lambda c:36*"TJQKA".find(c)+int(c
,36),s)],int(t))for s,t in map(str.split,
open("apa07input.txt","r").readlines())))))
