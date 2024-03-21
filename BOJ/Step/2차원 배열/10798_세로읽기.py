matr = []

for _ in range(5):
    tmp = input()
    matr.append(tmp)

for i in range(15):
    for j in range(5):
        try:
            print(matr[j][i], end='')
        except:
            continue