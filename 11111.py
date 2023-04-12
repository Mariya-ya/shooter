#Создай собственный Шутер!

from pygame import *




#нам нужны такие картинки:
img_back = "galaxy.jpg" #фон игры
img_hero = "rocket.png" #герой

GREEN =(80,0,255)
#Создаем окошко
win_width = 700
win_height = 500
display.set_caption("me_game")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class Card(sprite.Sprite):
    def __init__(self,width,height,x,y,color):
        super().__init__()
        self.rect = Rect(x,y,width,height)
        self.fill_color = color
    def draw(self):
        draw.rect(window,self.fill_color,self.rect)

class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y): 
        super().__init__()
        self.image = transform.scale(image.load(img_back), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


player2 = Pic(img_hero,80,80,200,250)
player1 = Card(80,80,100,150,GREEN)




#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

       #обновляем фон
    window.blit(background,(0,0))

       #обновляем их в новом местоположении при каждой итерации цикла
    player2.reset()
    player1.draw()

    display.update()
   #цикл срабатывает каждые 0.05 секунд
    time.delay(50)