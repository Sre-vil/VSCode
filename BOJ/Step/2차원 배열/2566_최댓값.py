matr = []
max_value = 0
col = 0
row = 0

for i in range(9):
    tmp = list(map(int, input().split()))
    matr.append(tmp)
    if max_value <= max(tmp):
        max_value = max(tmp)
        row = i+1
        col = tmp.index(max_value) + 1

print(max_value)
print(row, col)