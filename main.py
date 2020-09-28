import random, sys
import pygame
import config

def renderScore(screen, score):
    font = pygame.font.SysFont(None, 26)
    textSurface = font.render(f"score: {score}", True, config.colorDarkGreen)
    screen.blit(textSurface, (0, 0))

# renderBackground 渲染背景
def renderBackground(screen, color):
    return pygame.draw.rect(screen, config.colorBlack, (0, 0, config.winWidth, config.winHeight))

# renderFood 渲染食物
def renderFood(screen, foodCoord):
    return pygame.draw.rect(screen, config.colorRed, (foodCoord['x'] * 20, foodCoord['y'] * 20, 20, 20))

# renderSworm 渲染蠕虫
def renderSworm(screen, snakeCoords):
    for coor in snakeCoords:
        x = coor['x'] * config.cellSize
        y = coor['y'] * config.cellSize
        wormSegmentRect = (x, y, config.cellSize, config.cellSize)
        pygame.draw.rect(screen, config.colorBlue, wormSegmentRect)

# selectDirection 根据键盘按键，选择新方向
def selectDirection(key, oldDirection):
    if key == pygame.K_d and oldDirection != 'left':
        return 'right'
    if key == pygame.K_a and oldDirection != 'right':
        return 'left'
    if key == pygame.K_w and oldDirection != 'down':
        return 'up'
    if key == pygame.K_s and oldDirection != 'up':
        return 'down'
    return oldDirection

# moveSnake 自然移动
def moveSnake(disrection, snakeCoords):
    nextCoord = nextSnakeCoord(disrection, snakeCoords)
    snakeCoords.insert(0, nextCoord)
    snakeCoords.pop()

# nextSnakeCoord 贪吃蛇的头部下一个坐标
def nextSnakeCoord(disrection, snakeCoords):  
    snakeHeaderCoord = snakeCoords[0]
    if disrection == 'right':
        return {'x': snakeHeaderCoord['x'] + 1, 'y': snakeHeaderCoord['y']}
    if disrection == 'left':
        return {'x': snakeHeaderCoord['x'] - 1, 'y': snakeHeaderCoord['y']}
    if disrection == 'up':
        return {'x': snakeHeaderCoord['x'], 'y': snakeHeaderCoord['y']-1}
    if disrection == 'down':
        return {'x': snakeHeaderCoord['x'], 'y': snakeHeaderCoord['y']+1}

# randomFoodCoord 随机生成一个食物的坐标
def randomFoodCoord():
    return {'x': random.randint(0, config.mapHeight - 10), 'y': random.randint(0, config.mapWith - 10)}

# initSwormCoord 初始化蛇的坐标
def initSwormCoord():
    startx = 10
    starty = 10
    return [
        {'x': startx,     'y': starty}, 
        {'x': startx - 1, 'y': starty},
        {'x': startx - 2, 'y': starty},
    ]

# appendSworm 蛇的长度追加
def appendSworm(snakeCoords):
    snakeCoords.append({'x': snakeCoords[-1]['x'], 'y': snakeCoords[-1]['y']})
    return snakeCoords

# isEatFood 判断是否吃到了食物
def isEatFood(foodCoord, snakeCoords):
    snakeHeaderCoord = snakeCoords[0]
    if foodCoord['x'] == snakeHeaderCoord['x'] and foodCoord['y'] == snakeHeaderCoord['y']:
        return True
    return False

# isGameover 判断是否游戏结束
def isGameover(snakeCoords):
    snakeHeaderCoord = snakeCoords[0]
    # 超越边界
    if snakeHeaderCoord['x'] <= -1 or snakeHeaderCoord['x'] >= config.mapWith:
        return True
    if snakeHeaderCoord['y'] <= -1 or snakeHeaderCoord['y'] >= config.mapHeight:
        return True
    # 身体相撞
    for snakeBodyCoord in snakeCoords[1:]:
        if snakeBodyCoord['x'] == snakeHeaderCoord['x'] and snakeBodyCoord['y'] == snakeHeaderCoord['y']:
            return True
    return False

# gameExit 退出游戏
def gameExit():
    return pygame.quit()

def main():
    pygame.init()
    pygame.font.init()

    snake_speed_clock = pygame.time.Clock()
    pygame.display.set_caption(config.winTitle)

    screen = pygame.display.set_mode((config.winWidth, config.winHeight))

    score = 0
    direction = 'right'
    foodCoord = randomFoodCoord()
    snakeCoords = initSwormCoord()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return gameExit()
            if event.type == pygame.KEYDOWN:
                direction = selectDirection(event.key, direction)


        # 移动蛇
        moveSnake(direction, snakeCoords)
        if isGameover(snakeCoords):
            gameExit()

        # 如果吃到了食物，长度增加，创建新食物，分数增加
        if isEatFood(foodCoord, snakeCoords):
            snakeCoords = appendSworm(snakeCoords)
            foodCoord = randomFoodCoord()
            score += 1

        # 渲染图像
        renderBackground(screen, config.colorBlack)
        renderSworm(screen, snakeCoords)
        renderFood(screen, foodCoord)
        renderScore(screen, score)

        # 更新图像到显示设备
        snake_speed_clock.tick(config.snakeSpeed)
        pygame.display.update()

if __name__ == '__main__':
    main()

