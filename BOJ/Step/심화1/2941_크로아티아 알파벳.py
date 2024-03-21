import string
a = input()

alpha = string.ascii_letters
given = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in given:
    count += a.count(i)
    a = a.replace(i, '.')

a = a.replace('.', '')
print(count + len(a))