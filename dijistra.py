INF = float('inf')


def Dijkstra(cost, n, v):
    S = [False] * (n + 1)
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    for i in range(1, n + 1):
        S[i] = False
        dist[i] = cost[v][i]
        if cost[v][i] != INF and i != v:
            parent[i] = v

    dist[v] = 0
    parent[v] = -1

    print("INITIALIZATION")
    print("v =", v)
    print("\nS:")
    for i in range(1, n + 1):
        print("S[" + str(i) + "] =", S[i])

    print("\ndist:")
    for i in range(1, n + 1):
        if dist[i] == INF:
            print("dist[" + str(i) + "] = inf")
        else:
            print("dist[" + str(i) + "] =", dist[i])

    for num in range(2, n + 1):
        u = -1
        min_dist = INF
        for i in range(1, n + 1):
            if S[i] == False and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        S[u] = True

        for w in range(1, n + 1):
            if S[w] == False and cost[u][w] != INF:
                if dist[w] > dist[u] + cost[u][w]:
                    dist[w] = dist[u] + cost[u][w]
                    parent[w] = u

        print("\nSTEP", num - 1)
        print("u =", u)
        for i in range(1, n + 1):
            print("S[" + str(i) + "] =", S[i], end=' ')
        print()

        for i in range(1, n + 1):
            if dist[i] == INF:
                print("dist[" + str(i) + "] = inf")
            else:
                print("dist[" + str(i) + "] =", dist[i], end=' ')
        print()

    print("\nFINAL SHORTEST PATH TABLE")
    print(f"{'src':<10}{'dest':<10}{'length':<10}path")

    for dest in range(1, n + 1):
        if dest == v:
            continue

        path = []
        x = dest
        while x != -1:
            path.append(x)
            if x == v:
                break
            x = parent[x]

        path.reverse()
        path_string = " -> ".join(map(str, path))
        print(f"{v:<10}{dest:<10}{dist[dest]:<10}{path_string}")

    return dist, parent


cost = [
    [0,   10,  11,  18,  INF, 24,  31,  26],
    [24,  0,   24,  INF, 18,  25,  25,  24],
    [15,  INF, 0,   11,  INF, INF, 29,  31],
    [INF, INF, INF, 0,   23,  INF, INF, 11],
    [INF, 26,  INF, INF, 0,   30,  INF, INF],
    [22,  11,  16,  11,  13,  0,   INF, INF],
    [19,  35,  INF, INF, 21,  26,  0,   INF],
    [28,  14,  17,  27,  INF, 33,  15,  0],
]

cost = [[INF] + row for row in cost]
cost.insert(0, [INF] * 9)

n = 8
v = 1
dist, parent = Dijkstra(cost, n, v)