# 세 정수의 최댓값 구하기
    # 3개의 정숫값 비교하여 최댓값 구하기   
    # a,b,c에 정숫값을 입력받아 maximum으로 최댓값을 찾을 수 있음.
print("세 정수의 최댓값을 구합니다.")
a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))

maximum = a                 # maximum에 a의 값을 대입
if b > maximum: maximum=b   # b의 값이 maximum보다 크면, maximum에 b의 값을 대입 
if c > maximum: maximum=c   # c의 값이 maximum보다 크면, maximum에 c의 값을 대입 

print(f'최댓값은 {maximum}입니다.')