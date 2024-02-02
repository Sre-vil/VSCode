# 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

import random
from D_2_2_max import max_of

print('난수의 최댓값 구하기')
num = int(input('난수 갯수 입력 : '))
lo = int(input('난수 최솟값 입력 : '))
hi = int(input('난수 최댓값 입력 : '))
x = [None]*num # 원소 수가 num인 리스트 생성 

for i in range(num): x[i] = random.randint(lo, hi) # lo 이상 hi 이하인 정수 난수를 반환 

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')