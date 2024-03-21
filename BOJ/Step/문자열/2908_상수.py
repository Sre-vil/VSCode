a, b = input().split()

a_rev = a[::-1]
b_rev = b[::-1]

if a_rev < b_rev:
    print(b_rev)
else: print(a_rev)

# reversed(c) -> <reversed object at 0x0000019E33E399F0>
# reversed(c)를 이용하고 싶다면, list(reversed(c)) 혹은 ''.join(reversed(c)) 방법 사용 

# reversed 는 내장함수이며, reverse는 list 자료형에서 제공하는 함수임 
# reverse는 값을 반환하지 않고 단순히 뒤섞음
    # 따라서, print(l.reverse())은 None을 출력 
