"""
    我的飞机
"""
import pygame

#继承pygame.sprite.Sprite
class Myplane(pygame.sprite.Sprite):
    #初始化pygame
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        #导入图片
        self.image1 = pygame.image.load("images/hero1.png").convert_alpha()
        self.image2 = pygame.image.load("images/hero2.png").convert_alpha()

        #导入被打的图片存入列表
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/hero_blowup_n1.png").convert_alpha(),\
            pygame.image.load("images/hero_blowup_n2.png").convert_alpha(),\
            pygame.image.load("images/hero_blowup_n3.png").convert_alpha(),\
            pygame.image.load("images/hero_blowup_n4.png").convert_alpha(),\
            ])
        #获得飞机大小
        self.rect = self.image1.rect()
        #bg_size[0] 屏幕宽度,bg_size[1] 屏幕高度
        self.width, self.height = bg_size[0],bg_size[1]
        #飞机的左和顶
        # 屏幕的宽-飞机的宽取得整数
        self.rect.left,self.rect.top = \
            (self.width - self.rect.width)//2,\
            self.height - self.rect.height - 60

        self.speed = 10
        #设置存在
        self.active = True
        #飞机不会死设置为否
        self.invincible = False
        #更加精准的碰撞检测
        self.mask = self.mask.from_surface(self.image1)
    #向上移动
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.down < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.down = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.active = True
        self.invincible = True