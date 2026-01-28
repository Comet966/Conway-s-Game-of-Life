import numpy as np
import pygame
from pygame import surfarray
from scipy import signal

pygame.init()
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

arr_state = np.zeros((WIDTH,HEIGHT,3),dtype=np.uint8)

#define kernal
kernal_1=np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]
],dtype=np.uint8)
kernal_2=np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]
],dtype=np.uint8)
kernal_3=np.array([
    [1,0,1],
    [0,0,0],
    [1,0,1]
],dtype=np.uint8)
#modify initial state
#arr_state = np.random.randint(0,2,size=arr_state.shape)
arr_state[:,:,0] = np.ones((WIDTH,HEIGHT),dtype=np.uint8)
arr_state[:,:,1] = np.ones((WIDTH,HEIGHT),dtype=np.uint8)
arr_state[:,:,2] = np.ones((WIDTH,HEIGHT),dtype=np.uint8)
#arr_state[150:250,150:250,:] = np.ones((100,100,3),dtype=np.uint8)*255

#center_x, center_y = WIDTH // 2, HEIGHT // 2
#
# 简单圆形（可以用更精确的距离判断）
#y, x = np.ogrid[0:400, 0:400]
#for r in range(0,100):
#    mask = (x - center_x) ** 2 + (y - center_y) ** 2 == r ** 2
#    arr_state[mask,:] = 255



running = True
dt = 0
#define updater
def arr_update(arr,kernal1,kernal2,kernal3):
    arr[:,:,0] = signal.convolve2d(arr[:,:,0],kernal1,mode="same")
    arr[:,:,1] = signal.convolve2d(arr[:,:,1],kernal2,mode="same")
    arr[:,:,2] = signal.convolve2d(arr[:,:,2],kernal3,mode="same")
    return arr

#工作循环
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    arr_state = arr_update(arr_state,kernal_1,kernal_2,kernal_3)
    surfarray.blit_array(screen,arr_state)

    pygame.display.flip()
    dt = clock.tick(30)/1000


