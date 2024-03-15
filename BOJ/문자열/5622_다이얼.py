a = input()
tot_time = 0

for i in a:
    if i in "ABC": tot_time += 3
    elif i in "DEF" : tot_time += 4
    elif i in "GHI" : tot_time += 5
    elif i in "JKL" : tot_time += 6
    elif i in "MNO" : tot_time += 7
    elif i in "PQRS" : tot_time += 8
    elif i in "TUV" : tot_time += 9
    elif i in "WXYZ" : tot_time += 10
print(tot_time)