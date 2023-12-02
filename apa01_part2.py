print(sum(map(lambda l:(lambda d:d[0]*10
+d[-1])((lambda g:g(l,g))(lambda l,f:[]
if not l else(lambda p:p+f(l[1:],f))([
int(l[0])]if l[0].isdigit()else[i for i
,n in enumerate(["zero","one","two","t"
"hree","four","five","six","seven","ei"
"ght","nine"])if l[:len(n)]==n]))),open
("apa01input.txt","r").readlines())))
