n = int(input('몇 개 출력? '))
w = int(input('몇 개마다 줄바꿈? '))

for i in range(n):
    print('*', end='')
    if i % w == w-1: print()

if n%w: print()