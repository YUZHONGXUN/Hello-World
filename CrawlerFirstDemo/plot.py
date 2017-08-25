import  matplotlib.pyplot as plt
import csv
from datetime import datetime     # from datetime 模組中 import datetime

# x_cors = [1, 2, 3, 4]
# y_cors = [2, 3, 4, 5]

# plt.plot(x_cors, y_cors)
# plt.show()       # 一定用要呼叫函式, show 在新的視窗上

def showPlot(csv_file):     # 把 csv_file 檔案內的圖 show 出來
    f = open(csv_file, "r")
    r = csv.DictReader(f)    # 第一行當成標籤作為字典
    x = []    # 空的 list
    y = []
    for single_row in r:
        print(single_row)
        y.append(single_row['匯率'])   # 取出 "匯率" 的值後, 再回傳到 y 的 list
        x.append(datetime.strptime(single_row['時間'], "%Y-%m-%d %H:%M:%S"))   # 取出 "時間" 內的值回傳到 x 的 list
    # print(x)    # 確認 append 的結果是否為 datetime 的 strptime
    # print(y)
    plt.plot(x, y)
    plt.gcf().autofmt_xdate()   # 圖中的 x label 改成傾斜標示
    plt.show()

# showPlot('./result/美金(USD).csv')   # 給定匯入的檔案位址
file_name = input("請輸入欲作圖的CSV: ")    # 給使用者自行輸入檔案
file_name = "./result/" + file_name
showPlot(file_name)
