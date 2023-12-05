print(
    [
        r := open("apa03input.txt", "r").readlines(),
        h := len(r) + 2,
        w := len(r[0]) + 2,
        l := ["." * w] + ["." + s.strip() + "." for s in r] + ["." * w],
        dicts := [
            [
                z := max(
                    i
                    for i in range(w - x)
                    if all(l[y][x + j].isdigit() for j in range(i))
                ),
                {
                    (p, q): int(l[y][x : x + z])
                    for p in [y - 1, y, y + 1]
                    for q in range(x - 1, x + z + 1)
                    if l[p][q] == "*"
                },
            ][-1]
            for x in range(1, w - 1)
            for y in range(1, h - 1)
            if l[y][x].isdigit() and not l[y][x - 1].isdigit()
        ],
        keys := set(k for d in dicts for k in d.keys()),
        sum(
            [
                v[0] * v[1]
                for k in keys
                for v in [[d[k] for d in dicts if k in d]]
                if len(v) == 2
            ]
        ),
    ][-1]
)
