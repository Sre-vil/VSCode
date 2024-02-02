# 각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 리스트) 

from D_2_2_max import max_of

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'    
a = ['DTS', 'AAC', 'FLAC']

print(f'{t}의 최댓값은 {max_of(t)}')
print(f'{s}의 최댓값은 {max_of(s)}')
print(f'{a}의 최댓값은 {max_of(a)}')