l = open("apa03input.txt", "r").readlines()
h = len(l) + 2
w = len(l[0]) + 2
l = ["." * w] + ["." + s.strip() + "." for s in l] + ["." * w]
gears = {}
for x in range(1, w - 1):
    for y in range(1, h - 1):
        if not l[y][x].isdigit() or l[y][x - 1].isdigit():
            continue
        z = max(i for i in range(w - x) if all(l[y][x + j].isdigit() for j in range(i)))
        n = int(l[y][x : x + z])
        for p in [y - 1, y, y + 1]:
            for q in range(x - 1, x + z + 1):
                if l[p][q] == "*":
                    k = (p, q)
                    if k not in gears:
                        gears[k] = [n]
                    else:
                        gears[k].append(n)
print(sum(v[0] * v[1] for v in gears.values() if len(v) == 2))
