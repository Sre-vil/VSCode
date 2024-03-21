n, m = list(map(int, input().split()))
a = []
b = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

for _ in range(n):
    tmp = list(map(int, input().split()))
    b.append(tmp)

for i in range(n):
    for j in range(m):
        print(a[i][j]+b[i][j], end=' ')
    print()