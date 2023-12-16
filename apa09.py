print(sum(map(
x:=lambda h:[d
:=[h[i+1]-h[i]
for i in range
(len(h)-1)],h[
-1]+x(d)if any
(h)else 0][-1]
,map(lambda x:
list(map(int,x
.split())),map
(str,open("ap"
"\141\0609inp"
"ut.txt","r").
read().split(\
"\n")[:][:][:]
[:][:][:])))))