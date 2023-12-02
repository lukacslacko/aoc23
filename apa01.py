print(sum(map(lambda l:(lambda d:
d[0]*10+d[-1])([int(c)for c in 
l if c.isdigit()]),open("apa01"
"input.txt","r").readlines())))
