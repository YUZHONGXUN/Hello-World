from matplotlib import pyplot as plt

ls = ['dog', 'cat', 'frog', 'elephant']
sizes = [10, 20, 30, 40]
exs = [0, 0, 0.3, 0.1]     # 圓餅圖的區塊往外拉的參數

plt.pie(sizes, explode = exs, labels = ls, autopct='%.1f%%' ,shadow = True)   # 未寫入的函數, 自動帶入預設值的參數
plt.show()
