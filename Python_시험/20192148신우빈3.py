# 1부터 100까지 3의 배수에는 *, 그 외는 &를 출력
for i in range(1,101):
    if i%3==0: print("*", end='')
    else: print("&", end='')