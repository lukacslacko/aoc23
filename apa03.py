l = open("apa03input.txt", "r").readlines()
h = len(l) + 2
w = len(l[0]) + 2
l = ["." * w] + ["." + s.strip() + "." for s in l] + ["." * w]
s = 0
for x in range(1, w - 1):
    for y in range(1, h - 1):
        if not l[y][x].isdigit() or l[y][x - 1].isdigit():
            continue
        z = max(i for i in range(w - x) if all(l[y][x + j].isdigit() for j in range(i)))
        if any(
            c != "." and not c.isdigit()
            for c in [l[y][x - 1], l[y][x + z]]
            + list(l[y - 1][x - 1 : x + z + 1])
            + list(l[y + 1][x - 1 : x + z + 1])
        ):
            s += int(l[y][x : x + z])
            print(
                "--------------\n"
                + "\n".join(l[y + i][x - 1 : x + z + 1] for i in [-1, 0, 1])
            )
print(s)
