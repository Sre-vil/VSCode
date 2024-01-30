import random 

n = int(input('난수 개수 : '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end='')
    if r==13:
        print('\n프로그램을 중단')
        break

else: print('\n난수 생성 종료')