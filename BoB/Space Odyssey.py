import pygame
import random # 별의 크기 조정에 사용
import math # 별을 분포시키기 위한 각도(cos, sin을 이용해 원 궤적 구할 때 사용)
from pygame.locals import QUIT # pygame 종류를 위해 작성

class Star:
    # 생성자 
    def __init__(self, screen, screenSize, index): # screen : 그림 그릴 캔버스, index : 각 별 식별용
        self.size = 1
        self.color = (255, 255, 255)
        
        self.center = {
            'x' : screen.get_width() / 2,
            'y' : screen.get_height() / 2
        }
        
        self.radius = 0 # 반지름. 중심점으로부터 얼마나 멀리 떨어져있는가?
        self.theta = 0 # 별의 원 궤적을 구할 때 사용 
        
        self.screen = screen
        self.screenSize = screenSize
        
        self.init(index)
        
    # 별의 마지막 좌표 설정 - 중심점 기준 최대거리(모서리) 넘어가면 처음 위치로 되돌아가게 할 것.
    def getLimitDistance(self):
        return int(math.sqrt(math.pow(self.center['x'], 2) + math.pow(self.center['y'], 2)))


    def init(self, index):
        self.radius = float(random.randint(0, self.getLimitDistance()))
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        self.degree = (360/50) * index
        self.theta = float(self.degree) * math.pi/180
        
    def draw(self, color):
        x = self.center['x'] + self.radius * math.cos(self.theta)
        y = self.center['y'] + self.radius * math.sin(self.theta)
        
        pygame.draw.circle(self.screen, color, [x, y], self.size)
    
    # 원이 커지는데 균등하게 커지는게 아니라 점점 더 큰 갭으로 커지게하기 위함     
    def move(self):
        self.radius += 1 + (float(self.radius)/10)
        self.size = 1 + (self.radius/100)
        
        self.draw(self.color)
        
        if self.radius > self.getLimitDistance():
            self.radius = float(random.randint(0, self.getLimitDistance()))
    
screenSize = {
    'widht' : 1024,
    'height' : 768
}

pygame.init()
screen = pygame.display.set_mode(
    (screenSize['widht'], screenSize['height'])
)
pygame.display.set_caption("Space Odyssey")

stars = []
for i in range(0, 50):
    star = Star(screen, screenSize, i)
    stars.append(star)

count = 0
delay = 10000
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    clock.tick(30)
    
    screen.fill((0, 0, 0))
    
    for star in stars:
        star.move()
        
    pygame.display.update()