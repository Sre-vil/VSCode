# seq_search() 함수를 사용하여 실수 검색하기 
from D_3_1_ssearch_while import seq_search

number = 0
x = [] # 빈 리스트 x 생성 

while True:
    s = input(f'x[{number}]: ')
    if s == 'End': break
    x.append(float(s)) # 배열 맨 끝에 원소를 추가 
    number += 1

ky = float(input('검색할 값 입력 : ')) # 검색할 키 ky를 입력받기 

idx = seq_search(x, ky) # ky와 값이 같은 원소를 x에서 검색 
if idx==-1:
    print('검색값을 갖는 원소가 존재하지 않음') 
else:
    print(f'검색값은 x[{idx}]에 있음')