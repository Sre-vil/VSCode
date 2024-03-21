num = int(input())
count = 0

for i in range(num):
    word = input()
    tmp = []
    for j in word:
        if j in tmp and j!=tmp[-1]: 
            count += 1
            break
        else: tmp.append(j)
print(num-count)