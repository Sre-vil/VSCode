# 세 정수의 최댓값 구하기 

def max3(a, b, c):
    """a, b, c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum # 최댓값 반환 

print(f'max(3, 2, 1) = {max3(3, 2, 1)}') # a > b > c
print(f'max(3, 2, 2) = {max3(3, 2, 2)}') # a > b = c
print(f'max(3, 1, 2) = {max3(3, 1, 2)}') # a > c > b
print(f'max(3, 2, 3) = {max3(3, 2, 3)}') # a = c > b
print(f'max(3, 1, 3) = {max3(3, 1, 3)}') # c > a > b
print(f'max(3, 3, 2) = {max3(3, 3, 2)}') # a = b > c
print(f'max(3, 3, 3) = {max3(3, 3, 3)}') # a = b = c
print(f'max(3, 2, 3) = {max3(3, 2, 3)}') # c > a = b
print(f'max(3, 3, 1) = {max3(3, 3, 1)}') # b > a > c
print(f'max(3, 3, 2) = {max3(3, 3, 2)}') # b > a = c
print(f'max(3, 3, 2) = {max3(3, 3, 2)}') # b > c > a
print(f'max(3, 3, 3) = {max3(3, 3, 3)}') # b = c > a
print(f'max(3, 2, 3) = {max3(3, 2, 3)}') # c > b > a