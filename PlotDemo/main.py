from matplotlib import pyplot as plt
import numpy as np

# 分成數個畫布
plt.subplot(1, 2, 1)    # row = 1, col = 2, 編號1號畫布

# 在 0~2pi之間線性取50個點
# print(np.linspace(0, 2 * np.pi, 100))    # 試著 print 出來
x_dots = np.linspace(0, 2 * np.pi, 100)
y_dots = np.sin(x_dots)
plt.plot(x_dots, y_dots, 'b--', label="y = sin(x)")    # 將函數作圖, 帶入顏色(左) + 款式(右)
plt.legend()

plt.subplot(1, 2, 2)
y_dots_2 = []         # 先給定一個空的 list, 每次迴圈做完就放進去
for single_x_dot in x_dots:
    y_dots_2.append(single_x_dot * 2)    # 每次作圖就 append
plt.plot(x_dots, y_dots_2, 'k-.', label="y = 2 * x")   # 沒有名字會自動變成 list, 有名字自動會變成 dic
# 把標籤放入的位置
plt.legend()     # loc="lower-right" 把標籤在右下角, 空白就是在左上角

plt.plot()     # 作圖
plt.show()       # 把圖顯示出來
