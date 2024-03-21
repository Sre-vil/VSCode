# N : 바구니 개수. 1~N
    # 각 바구니에 바구니 번호와 같은 번호가 적힌 공 
# M : 공 변경 횟수 
# i, j : i번 바구니와 j번 바구니 공 교환 

n, m = list(map(int, input().split()))
l = [i+1 for i in range(n)]

for a in range(m):
    i, j = list(map(int, input().split()))
    # tmp = l[i-1]
    # l[i-1] = l[j-1]
    # l[j-1] = tmp
    l[i-1], l[j-1] = l[j-1], l[i-1]

for i in l: print(i, end=' ')