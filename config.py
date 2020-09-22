
# 颜色定义
colorWhite = (255, 255, 255)
colorBlack = (0, 0, 0)
colorGray = (230, 230, 230)
colorDarkGray = (40, 40, 40)
colorDarkGreen = (0, 155, 0)
colorGreen = (0, 255, 0)
colorRed = (255, 0, 0)
colorBlue = (0, 0, 255)
colorDarkBlue = (0, 0, 139)

# 定义方向
EVENT_UP = 1
EVENT_DOWN = 2
EVENT_LEFT = 3
EVENT_RIGHT = 4

# 窗口大小
winWidth = 800
winHeight = 600
winTitle = "贪吃蛇"

# 方块的大小
cellSize = 20

# 贪吃蛇的速度
snakeSpeed = 6  

# 因此地图实际尺寸是相对于贪吃蛇大小而言的
mapWith = int(winWidth / cellSize)
mapHeight = int(winHeight / cellSize)
