# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력하기 

score1 = int(input('1번 학생의 점수 입력 : '))
score2 = int(input('2번 학생의 점수 입력 : '))
score3 = int(input('3번 학생의 점수 입력 : '))
score4 = int(input('4번 학생의 점수 입력 : '))
score5 = int(input('5번 학생의 점수 입력 : '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}')
print(f'평균 {total/5}')