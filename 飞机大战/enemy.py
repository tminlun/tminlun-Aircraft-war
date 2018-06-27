"""
    敌方飞机
"""
import pygame
from random import *

#小敌人  Sprite:一个带有图像（Surface）和大小位置（Rect）的对象
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        #导入图形
        self.image = pygame.image.load("images/enemt0.png").convert_alpha()
        self.destroy_images = []#小敌人的图片列表
        self.destroy_images.extend([\
            pygame.image.load("images/enemy0_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy0_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy0_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy0_down4.png").convert_alpha(), \
            ])
        self.rect = self.image.get_rect()#获得image距形大小
        self.width, self.height = bg_size[0], bg_size[1]
        self.seep = 2 #速度为2
        #设置飞机当前的存在属性，True表示飞机正常飞行，False表示飞机已损毁
        self.active = True
        #random.randint(a, b),参数a是下限,参数b是上线:生成随机数n: a <= n <= b
        self.rect.left, self.top = \
            randint(0,self.width - self.rect.width),\
            randint(-5 * self.height,0)
        #更加精准的碰撞检测
        self.mask = pygame.mask.from_surface(self.image)

    #移动
    def move(self):
        #如果界面顶部 小于 自我的高
        if self.rect.top < self.height:
            self.rect.top+=self.speed #界面大小加 1
        else:
            self.reset() #否则敌机向下移动出界面

    def reset(self):
        self.active = True
        #当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)

#中敌人
class MidEnemy(pygame.sprite.Sprite):
    energy = 8

    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        #敌人被打的照片
        self.image_hit = pygame.image.load("images/enemy1_hit.png").convert_alpha()
        self.destroy_images = []
        #extend()用新列表扩展原来的列表
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down4.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down5.png").convert_alpha(), \
            pygame.image.load("images/enemy1_down6.png").convert_alpha(),\
            ])
        #获得矩形大小
        self.rect = self.image.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        self.speed = 1#速度为1
        #设置飞机当前的存在属性
        self.active = True
        #飞机的左和顶部
        self.rect.left,self.rect.top = \
                                randint(0,self.width - self.rect.width),\
                                randint(-10 * self.height, -self.height),
        # 设置飞机图像的掩膜用以更加精确的碰撞检测
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = MidEnemy.energy
        self.hit = False

        def move(self):
            """
            定义飞机的移动函数
            :param self:
            :return:
            """
            if self.rect.top < self.height:
                self.rect.top+=self.speed
            else:
                self.reset()

        def reset(self):
            """
            当战机向下移动出屏幕，且飞机是随机出现的
            :return:
            """
            #飞机的左，屏幕的顶部
            self.rect.left , self.top = \
                randint(0,self.width - self.rect.width),\
                randint(0,-10 * self.height, -self.height)
#大敌方飞机:sprite:大小位置
class BigEnemy(pygame.sprite.Sprite):
    energy = 20

    def __init__(self,bg_size):
        self.sprite.Sprite.__init__(self)
        #导入图片
        self.image1 = self.image.load("images/enemy2.png").convert_alpht()
        self.image2 = self.image.load("images/enemy2_hit.png").convert_alpht()

        self.destroy_images = []
        #用新的列表扩展原来的列表
        self.destroy_images.extend([\
            #加载飞机损坏图片
            pygame.image.load("images/enemy2_down1.png").convert_alpht(), \
            pygame.image.load("images/enemy2_down2.png").convert_alpht(), \
            pygame.image.load("images/enemy2_down3.png").convert_alpht(), \
            pygame.image.load("images/enemy2_down4.png").convert_alpht(), \
            pygame.image.load("images/enemy2_down5.png").convert_alpht(), \
            pygame.image.load("images/enemy2_down6.png").convert_alpht(), \
            ])
        #获得image1图形大小
        self.rect = self.image1.get_rect()
        #屏幕的宽和高
        self.width,self.height = bg_size[0],bg_size[1]
        #速度为1
        self.speed = 1
        #设置战机存在
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-10 * self.height, -self.height),
        #更加精准的碰撞检测
        self.mack = self.mack.from_surface(self,self.image1)
        self.energy = BigEnemy.energy
        self.hit = False #打

    def move(self):
        """
        定义移动函数
        :return:
        """
        if self.rect.top < self.height:
            #如果飞机高比界面小
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        让飞机随机出现
        :return:
        """
       #如果存在
        self.active = True
        self.energy = BigEnemy.energy
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-15 * self.height, -5 * self.height)