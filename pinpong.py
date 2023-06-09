import pygame as pg
pg.init()
win_width, win_height = 900, 700
win = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('ПінПонг')
x2 = 5
y2 = 5
class Game_sprite():
    def __init__(self,image,x,y,width,height,speed):
        self.image = pg.transform.scale(pg.image.load(image),(width,height))
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))
class Player(Game_sprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pg.K_d] and self.rect.x < 750:
            self.rect.x += self.speed
    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.x < 750:
            self.rect.x += self.speed
class Ball(Game_sprite):
    def move(self):
        global x2, y2, player, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(self, player) or pg.sprite.collide_rect(self, player2):
            y2 = y2 * -1
        if self.rect.x > 850:
            x2 = -5
        if self.rect.x < 0:
            x2 = 5


bg = Game_sprite('Image/BG.jpg',0,0,900,700,0)
player = Player('Image/Platform2.png',350,0,200,30,10)
player2 = Player('Image/Platform.png',350,670,200,30,10)
ball = Ball('Image/Ball.png',350,350,50,50,15)
while True:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    bg.reset()
    player.reset()
    player.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    pg.display.flip()