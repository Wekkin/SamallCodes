## 获取一条直线上的灰度值

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 定义鼠标回调函数
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global A
        A = (x, y)

# 加载图像
img = cv2.imread('image.bmp', cv2.IMREAD_GRAYSCALE)

# 创建窗口并绑定鼠标回调函数
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse)

# 显示图像并等待鼠标点击
cv2.imshow('image', img)
cv2.waitKey(0)

# 根据A点坐标计算B点坐标
B = (A[0], A[1] + 50)

# 获取A到B的灰度值并输出
gray_values = []
for y in range(A[1], B[1]+1):
    gray_values.append(img[y, A[0]])
print("A到B的灰度值是：" , gray_values)

# 画出直线AB
cv2.line(img, A, B, color=255, thickness=1)
cv2.imshow('image', img)
# 设置X轴和Y轴的坐标和范围
x = np.arange(A[1], B[1]+1, 1)
y = gray_values
plt.xlim(A[1], B[1])
plt.ylim(0, 255)
plt.xlabel('line AB y axis')
plt.ylabel('Gray value')

# 绘制图像
plt.plot(x, y)
plt.show()

# 销毁窗口
cv2.destroyAllWindows()
