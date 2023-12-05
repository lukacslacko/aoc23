print([r:=open("apa03input.txt", "r").
readlines(),h:=len(r)+2,w:=len(r[0])+2
,l:=["."*w]+["."+s.strip()+"."for s in
r]+["."*w],sum([z:=max(i for i in range
(w-x)if all(l[y][x+j].isdigit() for j 
in range(i))),int(l[y][x:x+z]) if not 
all(c=="."for c in l[y][x-1]+l[y][x+z]
+l[y-1][x-1:x+z+1]+l[y+1][x-1:x+z+1])
else 0][-1]for x in range(1,w-1)for y 
in range(1,h-1)if l[y][x].isdigit()
and not l[y][x-1].isdigit())][-1])
