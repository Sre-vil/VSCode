score_list = []
lev_to_score = {
    'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
    'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0,
    'F':0.0    
    }
score_sum=0
for _ in range(20):
    name, score, level = input().split()
    if level=="P": continue
    else:
        score_list.append(float(score)*lev_to_score[level])
        score_sum += float(score)  

print('%.6f'%(sum(score_list)/score_sum))