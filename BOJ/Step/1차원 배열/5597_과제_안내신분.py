l = [i for i in range(1,31)]
l2 = []

for i in range(28):
    tmp = int(input())
    l2.append(tmp)

for i in l:
    if i not in l2:
        print(i)