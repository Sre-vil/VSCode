n, m = list(map(int, input().split()))
l = [i for i in range(1, n+1)]
for i in range(m):
    i, j = list(map(int, input().split()))
    # tmp = l[i-1:j]
    # tmp = tmp[::-1]
    # l[i-1:j] = tmp
    l[i-1:j] = l[i-1:j][::-1]  # 직접적으로 슬라이스의 역순을 할당
for i in l : print(i, end=' ')