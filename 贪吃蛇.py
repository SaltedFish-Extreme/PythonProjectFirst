#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 导入必要的模块
import pygame
import sys
import random
from pygame.locals import *

# 定义颜色变量，使用RGB值
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)

def gameOver():
    """结束游戏函数，退出pygame并退出系统"""
    pygame.quit()
    sys.exit()

def main():
    """主函数，用于运行贪吃蛇游戏"""

    pygame.init()  # 初始化pygame所有模块

    fpsClock = pygame.time.Clock()  # 创建一个时钟对象，用于控制游戏速度

    # 创建游戏窗口，设置大小为640x480
    playSurface = pygame.display.set_mode((640, 480))
    # 设置窗口标题为“贪吃蛇”
    pygame.display.set_caption('贪吃蛇')

    # 初始化蛇头的初始位置
    snakePosition = [100, 100]
    # 初始化蛇身的初始位置列表
    snakeBody = [[100, 100], [80, 100], [60, 100]]

    # 初始化目标（食物）的位置
    targetPosition = [300, 300]
    targetflag = 1  # 标记是否需要重新放置目标

    direction = 'right'  # 初始化蛇的移动方向为右
    changeDirection = direction  # 用于存储方向变化

    while True:  # 主游戏循环

        for event in pygame.event.get():  # 事件处理循环
            if event.type == QUIT:  # 如果触发退出事件
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:  # 如果按下键盘按键
                # 根据按键改变方向
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:  # 如果按下ESC键
                    pygame.event.post(pygame.event.Event(QUIT))

        # 防止蛇向相反方向移动
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # 根据方向移动蛇头的坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        # 在蛇头位置插入新的位置
        snakeBody.insert(0, list(snakePosition))

        # 如果蛇吃到目标，目标需要重新放置
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1]:
            targetflag = 0
        else:
            snakeBody.pop()  # 如果没有吃到目标，移除蛇尾

        # 随机生成新的目标位置
        if targetflag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            targetPosition = [int(x * 20), int(y * 20)]
            targetflag = 1

        playSurface.fill(blackColour)  # 填充背景颜色为黑色
        # 画出蛇身
        for position in snakeBody:  # rect(Surface, color, Rect, width=0)
            pygame.draw.rect(playSurface, whiteColour, Rect(position[0], position[1], 20, 20))
        # 画出目标方块
        pygame.draw.rect(playSurface, redColour, Rect(targetPosition[0], targetPosition[1], 20, 20))

        pygame.display.flip()  # 刷新游戏屏幕

        # 判断蛇是否撞到边界，如果是则结束游戏
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver()

        fpsClock.tick(5)  # 控制游戏速度，每秒帧数为5

if __name__ == "__main__":
    main()  # 运行主函数
