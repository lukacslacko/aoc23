def d(s):
    d={x[1]:int(x[0]) for x in map(lambda t:t.strip().split(), s.split(","))}
    return d

def b(ds,k):
    return max(d[k] for d in ds if k in d)

def pow(line):
    head, body = line.split(":")
    ds = list(map(d,body.split(";")))
    return b(ds,"red")*b(ds,"green")*b(ds,"blue")
    
print(sum(map(pow, open("apa02input.txt", "r").readlines())))
