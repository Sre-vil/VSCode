from D_2_7_A_card_conv import card_conv

if __name__ == '__main__':
    print('10진수를 n진수로 변환')

    while True:
        while True: # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력 :'))
            if no > 0:
                break

        while True: # 2~36진수의 정숫값을 입력받음
            cd = int(input('어떤 진수로 변환? : '))
            if 2<= cd <= 36:
                break
        
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input('한 번 더 변환할까요?(Y ... 예 / N ... 아니요) : ')
        if retry in {'N', 'n'}:
            break