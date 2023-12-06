l = open("apa06input.txt").readlines()
t = map(int, l[0].split()[1:])
d = map(int, l[1].split()[1:])
w = 1
for a, b in zip(t, d):
    s = 0
    for x in range(a):
        if x*(a-x) > b:
            s += 1
    w *= s
print(w)
