import sys
import pygame


def check_keydown_event(event,ship):            ##定义一个按下键盘的函数

            if event.key==pygame.K_RIGHT:       ##方向键右键
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:      ##方向键左键
                ship.moving_left=True
            elif event.key == pygame.K_UP:      ##方向键上键
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:    ##方向键下键
                ship.moving_down = True

def check_keyup_event(event,ship):              ##定义一个松开键盘的函数

            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
def check_events(ship):                        ##响应键盘的函数
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ##退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
def update_screen(ai_settings,screen,ship): ##刷新屏幕
    screen.fill(ai_settings.bg_color)       ##背景设置
    ship.blitme()                           ##在指定位置创建飞船
    pygame.display.flip()
