m, n = map(int, input().split())
board = [input() for _ in range(m)]

patterns = [
    ['WBWBWBWB', 'BWBWBWBW']*4,
    ['BWBWBWBW', 'WBWBWBWB']*4
]
res = []

for i in range(m-7):
    for j in range(n-7):
        for pat in patterns:
            changes = 0
            for a in range(8):
                for b in range(8):
                    if board[i+a][j+b] != pat[a][b]:
                        changes += 1
            res.append(changes)

print(min(res))