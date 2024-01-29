# 세 정수의 최댓값 구하기
    # 3개의 정숫값 비교하여 최댓값 구하기   
    # a,b,c에 정숫값을 입력받아 maximum으로 최댓값을 찾을 수 있음.
print("세 정수의 최댓값을 구합니다.")
a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))

maximum = a
if b > maximum: maximum=b
if c > maximum: maximum=c

print(f'최댓값은 {maximum}입니다.')