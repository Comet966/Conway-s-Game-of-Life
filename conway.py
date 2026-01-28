import numpy as np
import pygame
from scipy.signal import convolve2d

# 参数设置
WIDTH, HEIGHT = 800, 800  # 窗口大小
CELL_SIZE = 10  # 每个细胞的像素大小
COLS = WIDTH // CELL_SIZE  # 网格列数
ROWS = HEIGHT // CELL_SIZE  # 网格行数

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# 卷积核（计算8个邻居）
# 修改卷积核可以改变规则
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]], dtype=np.uint8)

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# 初始化网格（初始为随机状态，约20%活细胞）
grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2])

# 控制变量
simulation_running = True  # 是否自动演化
run = True  # 主循环控制

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 空格：暂停/继续
                simulation_running = not simulation_running
            if event.key == pygame.K_r:  # R：重新随机生成
                grid = np.random.choice([0, 1], size=(ROWS, COLS), p=[0.8, 0.2])
            if event.key == pygame.K_c:  # C：清空网格
                grid = np.zeros((ROWS, COLS), dtype=int)

    # 如果模拟正在运行，计算下一代
    if simulation_running:
        # 使用卷积计算每个细胞的活邻居数（环形边界）
        neighbors = convolve2d(grid, kernel, mode='same', boundary='wrap')
        # 应用生命游戏规则
        grid = (neighbors == 3) | (grid & (neighbors == 2))

    # 暂停时允许手动编辑（自定义初始状态）
    if not simulation_running:
        buttons = pygame.mouse.get_pressed()
        if buttons[0] or buttons[2]:  # 左键绘制活细胞，右键擦除
            mx, my = pygame.mouse.get_pos()
            col = mx // CELL_SIZE
            row = my // CELL_SIZE
            if 0 <= row < ROWS and 0 <= col < COLS:
                grid[row, col] = 1 if buttons[0] else 0

    # 绘制背景
    screen.fill(WHITE)

    # 绘制活细胞
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row, col]:
                pygame.draw.rect(screen, BLACK,
                                 (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # 绘制网格线
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    # 绘制操作提示
    tip = "Space: Stop  |  R:Random  |  C:Clear  |  Mouse Left/Right:Paint/Delete"
    text = font.render(tip, True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(12)  # 控制演化速度（约12代/秒）

pygame.quit()