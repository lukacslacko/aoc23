print(
    sum(
        [
            c := [
                len(v[0].intersection(v[1]))
                for v in [
                    list(
                        map(
                            lambda s: set(int(x) for x in s.split()),
                            l.split(":")[1].split("|"),
                        )
                    )
                    for l in open("apa04input.txt", "r").readlines()
                ]
            ],
            n := len(c),
            f := lambda v, i: [
                print(v, i),
                [v[k] + (v[i] if i < k <= i + c[i] else 0) for k in range(n)],
            ][-1],
            g := lambda i: [print(i), f([1] * n, 0) if i == 0 else f(g(i - 1), i)][-1],
            g(n - 1),
        ][-1]
    )
)
