total = int(input())
total_count = int(input())

sum = 0
for i in range(total_count):
    a, b = list(map(int, input().split()))
    sum += a*b

if sum == total:
    print("Yes")
else: print("No")