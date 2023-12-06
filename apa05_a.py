print([l:=open("apa05input.txt","r").
readlines(),q:=lambda k,h,m:[v:=list(
map(int,m.split())),r:=range(v[1],v[1
]+v[2]),([p for p in k if p not in r]
,h+[p+v[0]-v[1]for p in k if p in r])
][-1],e:=lambda k,h:(k+h,[]),u:=lambda
k,h,m:e(k,h)if":"in m or" "not in m 
else q(k,h,m),y:=lambda k,h,c:(k,h)if
not c else y(*u(k,h,c[0]),c[1:]),min(
y(list(map(int,l[0].split(":")[1]
.split())),[],l[1:])[0])][-1])
