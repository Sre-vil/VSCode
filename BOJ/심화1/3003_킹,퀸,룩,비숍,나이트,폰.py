ans = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))

for i in range(len(ans)):
    print(ans[i]-b[i], end=' ')
