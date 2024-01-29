# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요 : '))
b = int(input('정수 b를 입력하세요 : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b: print(f'{i} + ', end='')  # i가 b보다 작으면 합을 구하는 과정을 출력 
    else: print(f'{i} = ', end='')      # i가 b보다 크거나 같으면 최종값 출력을 위해 i = 출력 
    sum+=i                              # sum에 i를 더함 

print(sum)