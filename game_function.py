import sys
import pygame


def check_keydown_event(event,ship):

            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                ship.moving_left=True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True

def check_keyup_event(event,ship):

            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left=False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  ##退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
def update_screen(ai_settings,screen,ship): ##刷新屏幕
    screen.fill(ai_settings.bg_color)       ##背景设置
    ship.blitme()
    pygame.display.flip()
