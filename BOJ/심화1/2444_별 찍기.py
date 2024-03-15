a = int(input())
b = a
c= []

for i in range(1, a*2):
    if i%2==1:
        c.append(i)
        for j in range(b-1): print(" ", end='')
        for k in range(i): print('*', end='')
        b-=1
    else: continue
    print()

c.reverse()
# print(c) => 9 7 5 3 1
for i in c:
    if b==0:
        b+=1
    else:
        for j in range(b): print(' ', end='')
        for k in range(i): print('*', end='')
        b+=1
        print()