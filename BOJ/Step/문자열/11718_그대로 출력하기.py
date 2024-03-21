while True:
    try:
        print(input())
    except EOFError:
        break

# 입력값이 몇 번 주어지는지 정보가 없음
# 이런 경우 try,except 구문을 통해 입력값이 계속 들어오면 print
# 입력값이 안들어온다면 EOF(End Of File)로 판단하고, break