### 康威生命游戏(元胞自动机)
---
#### 介绍
使用*scipy.signal*中的*convolve2d*方法对一个使用*pygame*建立的画布  
以卷积的方式进行迭代  
可以设置画布RGB三个颜色空间的初始值，以及卷积核的值  




#### 克隆到本地

##### 方式1: 使用*git bash*  
1.选择工作目录打开*git bash*  
2.*git bash*命令行运行  
```GitBash
$ git clone https://github.com/Comet966/Conway-s-Game-of-Life.git

```
使用自己的IDE打开main即可  

##### 方式2:  本地配置环境
*使用AnacondaPrompt*  
```AnacondaPrompt
> conda create env --name conway python=3.11
> conda activate conway
> pip pygame
> install numpy scipy ffmpeg pillow

```

###### 使用IDE打开虚拟环境粘贴main.py代码即可  
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





