case_count = int(input())
l = []

for i in range(case_count):
    tmp = input()
    l.append(tmp[0]+tmp[-1])

for i in l: print(i)