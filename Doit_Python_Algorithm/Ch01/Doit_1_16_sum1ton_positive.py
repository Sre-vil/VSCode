while True:
    n = int(input('n 값 입력 : '))
    if n > 0:
        break # n이 0보다 커질 때까지 반복 

sum = 0
i = 1

for i in range(1, n+1):
    sum += i # sum에 i를 더함 
    i += 1 # i에 1을 더함 

print(f'1부터 {n}까지정수의 합은 {sum}입니다.')