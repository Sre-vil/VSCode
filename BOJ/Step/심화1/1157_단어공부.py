a = input().lower()
b = set(a)

res = ''
max_count = 0
for i in b:
    if max_count < a.count(i):
        max_count = a.count(i)
        res = i
    elif max_count == a.count(i):
        res='?'
print(res.upper())