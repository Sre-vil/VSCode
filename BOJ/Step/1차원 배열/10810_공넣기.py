# N : 바구니 개수 
# M : 공을 넣는 횟수 

n, m = list(map(int, input().split()))
l = [0 for i in range(n)]

for z in range(m):
    i, j, k = list(map(int, input().split()))
    for x in range(i-1, j):
        l[x] = k

for i in l: print(i, end=' ')