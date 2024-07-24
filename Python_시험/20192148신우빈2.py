# 1부터 100까지 홀수 합, 짝수 합 구하기
even = 0 # 짝수 합
odd = 0 # 홀수 합
for i in range(101):
    if i%2==0: even+=i
    else: odd+=i

print("1부터 100까지 홀수의 합 : %d" % odd)
print("1부터 100까지 짝수의 합 : %d" % even)