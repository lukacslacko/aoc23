print(
    sum(
        2 ** len(v[0].intersection(v[1])) // 2
        for v in [
            list(
                map(
                    lambda s: set(int(x) for x in s.split()), l.split(":")[1].split("|")
                )
            )
            for l in open("apa04input.txt", "r").readlines()
        ]
    )
)
