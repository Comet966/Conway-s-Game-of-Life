### 康威生命游戏(元胞自动机)
---
*实现* 
*伪代码*
```python
#使用surfarray
screen = pygame.display.set_mode((WIDTH,HEIGHT))
arr_state = np.zeros((WIDTH,HEIGHT,3),dtype=np.uint8)



#define kernal1~kernal3 对应三个颜色空间的迭代
kernal1
kernal2
kernal3

#define arr_state_r,g,b 三个颜色空间的初始状态
arr_state_r
arr_state_g
arr_state_b

#define 迭代函数,kernal和arr_state作为参数
def arr_update(arr,kernal):
    arr[1:arr.shape[0],1:arr.shape[1]] = signal.convolve2d(arr,kernal,mode="same")
    return arr
#工作循环
while(running):
    #更新状态
    #分别更新arr_state[0,1,2]
    
    arr_state = arr_update(arr_state,kernal1)
    #将arr_state中数据传到screen
    surfarray.blit_array(screen,arr_state)
    pygame.display.flip()





