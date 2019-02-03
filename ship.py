import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        self.ai_settings=ai_settings
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp') ##导入图片
        self.rect=self.image.get_rect()                 ##得到矩形属性
        self.screen_rect=screen.get_rect()              ##得到屏幕属性

        self.rect.centerx=self.screen_rect.centerx      ##飞船的x坐标为居中
        self.rect.centery=self.screen_rect.centery      ##飞船的y坐标为居中
        ##self.rect.bottom=self.screen_rect.bottom      ##飞船的y坐标为底部
        self.center=float(self.rect.centerx)
        self.center2=float(self.rect.top)
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_left and self.rect.left > 0:                             ##定义游戏边界为可显示界面的边缘
            self.center -= self.ai_settings.ship_speed_factor                   ##在界内时沿x轴向左移动
        elif self.moving_right and self.rect.right < self.screen_rect.right:    ##定义游戏边界为可显示界面的边缘
            self.center += self.ai_settings.ship_speed_factor                   ##在界内时沿x轴向右移动
        elif self.moving_up and self.rect.top>0:                                ##定义游戏边界为可显示界面的边缘
            self.center2 -= self.ai_settings.ship_speed_factor                  ##在界内时沿y轴向下移动
        elif self.moving_down and self.rect.bottom <self.screen_rect.bottom:    ##定义游戏边界为可显示界面的边缘
            self.center2 += self.ai_settings.ship_speed_factor                  ##在界内时沿y轴向上移动
        self.rect.centerx=self.center
        self.rect.top=self.center2
    def blitme(self):
        self.screen.blit(self.image,self.rect)      ##获取图像，导入位置