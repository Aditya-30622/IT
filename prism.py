INF = float('inf')

cost = [
    [INF, 11, 88, INF, 28,43, 38, 32, 38, 20],
    [11, INF, 70, 67, 57, 48, 89, 58, 81, 35],
    [88, 70, INF, INF, 71, 23, 16,77,25, 43],
    [INF, 67, INF, INF, 38, 78, 84, 80,69, 70],
    [28, 57, 71, 38, INF, 40, 65, 96, 56, 52],
    [43, 48, 23, 78, 40, INF, 78, INF,INF, 36],
    [38, 89, 16, 84, 65, 78, INF, 83, 74, 42],
    [32, 58, 77, 80, 96, INF, 83, INF, 89,51],
    [38, 81, 25, 69, 56, INF, 74, 89, INF, INF],
    [20, 35, 43, 70, 52, 36, 42, 51, INF, INF]
]

n = len(cost)

for i in range(n):
    for j in range(n):
        if cost[i][j] != cost[j][i]:
            raise ValueError(f"Matrix not symmetric at ({i+1},{j+1})")


def show(near):
    print("near array with cost array:")
    print("  near:", [0 if x == -1 else x + 1 for x in near])
    print("  cost:", ["-" if near[i] == -1 else cost[i][near[i]] for i in range(n)])


def prim():
    near = [0] * n
    t = []

    min_cost = INF
    k = l = -1
    for i in range(n):
        for j in range(i + 1, n):
            if cost[i][j] < min_cost:
                min_cost, k, l = cost[i][j], i, j

    if k == -1:
        raise ValueError("Graph has no edges")

    t.append((k, l, min_cost))
    total = min_cost

    for i in range(n):
        if i == k or i == l:
            near[i] = -1
        else:
            near[i] = l if cost[i][l] < cost[i][k] else k

    print("Step 1")
    print(f"  Selected edge: ({k + 1}, {l + 1})  cost = {min_cost}")
    show(near)
    print("  total min cost =", total)

    for step in range(2, n):
        j, min_cost = -1, INF
        for x in range(n):
            if near[x] != -1 and cost[x][near[x]] < min_cost:
                min_cost, j = cost[x][near[x]], x

        if j == -1:
            raise ValueError("Graph is disconnected; no spanning tree exists")

        t.append((j, near[j], min_cost))
        total += min_cost
        near[j] = -1

        for x in range(n):
            if near[x] != -1 and cost[x][j] < cost[x][near[x]]:
                near[x] = j

        print(f"\nStep {step}")
        print(f"  Selected edge: ({j + 1}, {t[-1][1] + 1})  cost = {min_cost}")
        show(near)
        print("  total min cost =", total)

    return t, total


tree, total = prim()

print("\nFinal MST edges:")
for u, v, w in tree:
    print(f"  {u + 1} - {v + 1}  (cost {w})")
print("Minimum Cost =", total)