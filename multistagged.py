INF = float("inf")

matrix = [
    [0, 13, 2, 11, 1, INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [INF, 0, INF, INF, INF, 5, 4, 13, 10, INF, INF, INF, INF, INF],
    [INF, INF, 0, INF, INF, 14, 13, 15, 5, INF, INF, INF, INF, INF],
    [INF, INF, INF, 0, INF, INF, 3, 13, 11, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, 0, INF, 6, 4, 1, INF, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, 0, INF, INF, INF, 1, 7, 12, 6, INF],
    [INF, INF, INF, INF, INF, INF, 0, INF, INF, 9, 8, 10, 13, INF],
    [INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, 5, 1, 8, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, 0, 7, 8, 6, 2, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, INF, 3],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, INF, 5],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, INF, 10],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0, 6],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 0],
]

n = 14
k = 5

stage_vertices = {1: [1], 2: [2, 3, 4, 5], 3: [6, 7, 8, 9], 4: [10, 11, 12, 13], 5: [14]}
stage_of = {v: s for s, vs in stage_vertices.items() for v in vs}


def c(i, j):
    return matrix[i - 1][j - 1]


def heading(s):
    vs = ", ".join(map(str, stage_vertices[s]))
    word = "Vertex" if len(stage_vertices[s]) == 1 else "Vertices"
    print(f"\nStage {s}: {word} {vs}")


def FGraph(k, n, p):
    cost = [INF] * (n + 1)
    d = [0] * (n + 1)

    cost[n] = 0.0
    heading(k)
    print(f"cost[{n}] = 0")

    stage = k
    for j in range(n - 1, 0, -1):
        if stage_of[j] != stage:
            stage = stage_of[j]
            heading(stage)

        best, r = INF, 0
        for x in range(j + 1, n + 1):
            if c(j, x) != INF:
                value = c(j, x) + cost[x]
                print(f"c[{j},{x}] + cost[{x}] = {c(j, x)} + {cost[x]:g} = {value:g}")
                if value < best:
                    best, r = value, x

        cost[j] = best
        d[j] = r
        print(f"cost[{j}] = {cost[j]:g}, d[{j}] = {d[j]}")

    p[1] = 1
    p[k] = n
    for j in range(2, k):
        p[j] = d[p[j - 1]]

    print("\ncost array:", [f"{x:g}" for x in cost[1:]])
    print("d array:", d[1:])
    print("Minimum Cost:", f"{cost[1]:g}")


def BGraph(k, n, p):
    bcost = [INF] * (n + 1)
    d = [0] * (n + 1)

    bcost[1] = 0.0
    heading(1)
    print("bcost[1] = 0")

    stage = 1
    for j in range(2, n + 1):
        if stage_of[j] != stage:
            stage = stage_of[j]
            heading(stage)

        best, r = INF, 0
        for x in range(1, j):
            if c(x, j) != INF:
                value = bcost[x] + c(x, j)
                print(f"bcost[{x}] + c[{x},{j}] = {bcost[x]:g} + {c(x, j)} = {value:g}")
                if value < best:
                    best, r = value, x

        bcost[j] = best
        d[j] = r
        print(f"bcost[{j}] = {bcost[j]:g}, d[{j}] = {d[j]}")

    p[1] = 1
    p[k] = n
    for j in range(k - 1, 1, -1):
        p[j] = d[p[j + 1]]

    print("\nbcost array:", [f"{x:g}" for x in bcost[1:]])
    print("d array:", d[1:])
    print("Minimum Cost:", f"{bcost[n]:g}")


print("FORWARD APPROACH (FGraph)")
p = [0] * (k + 1)
FGraph(k, n, p)
print("Minimum Cost Path p[1:k]:", " -> ".join(map(str, p[1:])))

print("\n\nBACKWARD APPROACH (BGraph)")
p = [0] * (k + 1)
BGraph(k, n, p)
print("Minimum Cost Path p[1:k]:", " -> ".join(map(str, p[1:])))