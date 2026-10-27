INF = float('inf')
parent = []

def Find(i):
    while parent[i] >= 0: i = parent[i]
    return i

def Union(j, k): parent[j] = k

def Adjust(a, i, n):
    j, item = 2 * i, a[i]
    while j <= n:
        if j < n and a[j][2] > a[j + 1][2]: j += 1
        if item[2] <= a[j][2]: break
        a[j // 2] = a[j]; j *= 2
    a[j // 2] = item

def Heapify(a, n):
    for i in range(n // 2, 0, -1): Adjust(a, i, n)

def DeleteMin(a, n):
    if n == 0:
        print("Heap empty"); return None, n
    x, a[1] = a[1], a[n]
    n -= 1
    if n > 0: Adjust(a, 1, n)
    return x, n

def PrintStep(step, u, v, j, k, parent, t, i, mincost, selected):
    print(f"\nSTEP {step}\nu = {u}\nv = {v}\nj = Find(u) = {j}\nk = Find(v) = {k}\ni = {i}")
    print("Decision :", "SELECT" if selected else "REJECT (cycle)")

    print("\nParent Array:")
    print("Vertex : " + "".join(f"{p:4}" for p in range(1, len(parent))))
    print("Parent : " + "".join(f"{parent[p]:4}" for p in range(1, len(parent))))

    print("\nT Table:\ni        u        v")
    for p in range(1, len(t)):
        if t[p] is not None: print(f"{p:<8}{t[p][0]:<9}{t[p][1]:<9}")

    print("\nmincost =", mincost)

def Kruskals(cost, n):
    global parent
    a = [None] + [[u, v, cost[u][v]] for u in range(1, n + 1) for v in range(u + 1, n + 1) if cost[u][v] != INF]

    m = len(a) - 1
    Heapify(a, m)
    parent = [0] + [-1] * n

    i, mincost, t, step = 0, 0, [None] * n, 0
    while i < n - 1 and m > 0:
        edge, m = DeleteMin(a, m)
        u, v = edge[0], edge[1]
        j, k = Find(u), Find(v)
        step += 1
        selected = j != k
        if selected:
            i += 1; t[i] = [u, v]; mincost += cost[u][v]; Union(j, k)
        PrintStep(step, u, v, j, k, parent, t, i, mincost, selected)

    if i != n - 1:
        print("\nNo spanning tree")
    else:
        print("\nFINAL RESULT\nMinimum Cost =", mincost)
        print("\nFinal T Table:\ni        u        v")
        for p in range(1, len(t)):
            if t[p] is not None: print(f"{p:<8}{t[p][0]:<9}{t[p][1]:<9}")

        print("\nFinal Parent Array:")
        print("Vertex : " + "".join(f"{p:4}" for p in range(1, n + 1)))
        print("Parent : " + "".join(f"{parent[p]:4}" for p in range(1, n + 1)))

    return mincost

cost = [
    [INF, 33, 19, 36, 68, 53, 20, 62, INF, 44],
    [33, INF, 17, 46, INF, 43, 43, INF, 21, 59],
    [19, 17, INF, 27, 41, 87, 25, 38, 48, 40],
    [36, 46, 27, INF, 50, 59, 39, 87, 72, 72],
    [68, INF, 41, 50, INF, 74, INF, 67, 47, 77],
    [53, 43, 87, 59, 74, INF, 87, 66, 21, INF],
    [20, 43, 25, 39, INF, 87, INF, 73, 57, 90],
    [62, INF, 38, 87, 67, 66, 73, INF, 71, 86],
    [INF, 21, 48, 72, 47, 21, 57, 71, INF, 20],
    [44, 59, 40, 72, 77, INF, 90, 86, 20, INF]
]

cost = [[INF] + row for row in cost]
cost.insert(0, [INF] * 11)
n = 10
Kruskals(cost, n)