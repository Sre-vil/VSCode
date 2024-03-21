in_data = list(map(int, input().split()))
compare_data = [1, 2, 3, 4, 5, 6, 7, 8]
revers_compare = list(reversed(compare_data))

if in_data == compare_data: print("ascending")
elif in_data == revers_compare: print("descending")
else: print("mixed")