import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect, KEYUP
import random

class Block:
    def __init__(self):
        self.position = {
            'x':5,
            'y':2
        }
        self.blocks = []

    def init_position(self):
        self.position = {
            'x':5, # 게임판 가로 넓이가 10이기 떄문에 가운데 출력하기 위함
            'y':2 # 길이가 3인 블록 제일 아래쪽이 기준이 됨. 위에서부터 0, 1, 2임 
        }
    
    def move_left(self):
        self.position['x'] -= 1
    def move_right(self):
        self.position['x'] += 1
    def move_down(self):
        self.position['y'] += 1
    def change(self):
        temp = self.blocks[0]
        self.blocks[0] = self.blocks[1]
        self.blocks[1] = self.blocks[2]
        self.blocks[2] = temp
    
def get_initialized_board():
    board = []
    
    for i in range(0, 20):
        board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) # blocks의 인덱스 값 
    
    return board

def canmove_left(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if x <= 0 :
        return False
    elif board[y][x-1] != 0:
        return False

    return True

def canmove_right(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if x>=9:
        return False
    elif board[y][x+1]!=0:
        return False
    
    return True

def can_move_down(now_block):
    x = now_block.position['x']
    y = now_block.position['y']
    if x>=19:
        return False
    elif board[y+1][x]!=0:
        return False
    
    return True

def set_value_on_board(x, y, value):
    global board
    board[y][x] = value
    
def update_game(board, now_block, next_block, score):

def check_around_vertical(x, y, color, candidates): # 수직으로 같은 색이 있는지 확인 
    if y >= 20:
        return candidates
    if color == 0:
        return candidates
    if board[y][x] != color:
        return candidates
    if board[y][x] == color:
        candidates.append({'x':x, 'y':y})
        check_around_vertical(x, y+1, color, candidates)
    
    return candidates

def check_around_horizontal(x, y, color, candidates):
    if x >= 10:
        return candidates
    if color == 0:
        return candidates
    if board[y][x] != color:
        return candidates
    if board[y][x] == color:
        candidates.append({'x':x, 'y':y})
        check_around_vertical(x+1, y, color, candidates)
    
    return candidates

def check_board(board):
    queue = []
    score = 0
    for y, line in enumerate(board):
        for x, color in enumerate(line):
            candidates = check_

block_color = [
    (64,64, 64), # gray 색상으로, 게임판(배경)임 
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (128, 0, 0),
    (0, 128, 0),
    (0, 0, 128),
    (255, 0, 255),
    (0, 255, 255)
]

screen_size = {
    'width': 240,
    'height': 400
}

pygame.init()
screen = pygame.display.set_mode(
    (screen_size['width'], screen_size['height'])
)
pygame.display.set_caption("HEXA")

now_block = Block() # 현재 내려오고 있는 블록 
next_block = Block() # 옆에 다음 블록이 뭔지 보여주는 블록 
board = get_initialized_board() # 게임판

now_block.blocks = [
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1)
]

next_block.init_position()
next_block.blocks = [
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1),
    random.randint(1, len(block_color) - 1)
]

delay = 1000
level = 0
score = 0

while True:
    update_game(board, now_block, next_block, score) # 판 세팅
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
                break
            elif event.key == pygame.K_UP:
                now_block.change()
                break
            elif event.key == pygame.K_LEFT:
                if canmove_left(now_block): # board 밖으로 나가는지 안나가는지 판단하기 위해 정의한 함수 
                    now_block.move_left()
                break
            elif event.key == pygame.K_RIGHT:
                if canmove_right(now_block):
                    now_block.move_down()
                break
            elif event.key == pygame.K_DOWN:
                if can_move_down(now_block):
                    now_block.move_down()
                break
            elif event.key == pygame.K_SPACE:
                for y in range(now_block.position['y'], 20): # 어디까지 내려갈 수 있는지 확인 및 내리기. 최대 높이가 20칸 
                    b = Block()
                    b.position['x'] = now_block.position['x']
                    b.position['y'] = y
                    if can_move_down(b) == False:
                        now_block.position['y'] = y
                        break
                break
    
    if can_move_down(now_block):
        level += 1 # 한 칸씩 이동하는 거 -- 딜레이를 이용해 속도 조절
        if level > delay:
            level = 0
            now_block.move_down()
        continue
    else:
        for i, block in enumerate(now_block.blocks):
            x = now_block.position['x']
            y = (now_block.position['y']-i)
            set_value_on_board(x, y, block)
        
        while True: # 3개 이상 연결된 곳이 있는지 확인
            point = check_board(board)
            if point <= 0: break
            score += point
            
        now_block.init_position()
        now_block.blocks = next_block.blocks
        
        next_block.blocks = [
            random.randint(1, len(block_color) - 1),
            random.randint(1, len(block_color) - 1),
            random.randint(1, len(block_color) - 1)
        ]
        
        delay = -1 # 게임 난이도 조절
        
    if gameover(board):
        sys.exit()