# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)

from D_2_2_max import max_of

number = 0
x = [] # 빈 리스트 

while True:
    s = input(f'x[{number}]값을 입력 : ')
    if s == 'End':
        break
    x.append(int(s)) # 배열의 맨 끝에 추가 
    number+=1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')