N = 6

cost = [
   [0,40,13,11,6,32],
       [20,0,17,6,9,49],
       [19,7,0,14,39,15],
       [15,18,10,0,6,28],
       [5,34,8,21,0,40],
       [26,21,28,9,34,0]
]

A = [row[:] for row in cost]

P = [[-1 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            P[i][j] = i


def print_matrix(M):
    for row in M:
        print(*row)
    print()


def print_precedence(P):
    for row in P:
        print(*[x + 1 if x != -1 else "-" for x in row])
    print()


def print_path(P, i, j):
    if i == j:
        print(i + 1, end="")
        return

    if P[i][j] == -1:
        print("No Path", end="")
        return

    print_path(P, i, P[i][j])
    print(" ->", j + 1, end="")


print("A0")
print_matrix(A)

print("P0")
print_precedence(P)


for k in range(N):

    for i in range(N):
        for j in range(N):

            if A[i][j] > A[i][k] + A[k][j]:
                A[i][j] = A[i][k] + A[k][j]
                P[i][j] = P[k][j]

    print("A" + str(k + 1))
    print_matrix(A)

    print("P" + str(k + 1))
    print_precedence(P)


print("FINAL COST MATRIX")
print_matrix(A)

print("FINAL PRECEDENCE MATRIX")
print_precedence(P)


print("FINAL PATH TABLE")
print()
print(f"{'FROM':<8}{'TO':<8}{'COST':<8}PATH")

for i in range(N):
    for j in range(N):

        if i != j:
            print(f"{i + 1:<8}{j + 1:<8}{A[i][j]:<8}", end="")
            print_path(P, i, j)
            print()