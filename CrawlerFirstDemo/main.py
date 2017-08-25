from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv                   # 用來開啟 csv 的檔案
from os.path import exists    # 判斷檔案是否存在
from time import localtime, strftime    # 年月日的時區, 把 time轉成字串形式

page = urlopen("http://rate.bot.com.tw/xrt?Lang=zh-TW")    # 使用 urlopen 匯入原始的網頁文件, 非動態的網頁文件
print(page)    # print "HTTPResponse", 表示是一個 HTTP的物件

bsObj = BeautifulSoup(page, "html.parser")    # 系統告知必須要加上 "html.parser"
# print(bsObj)   # print 網頁的頁面

# print 頁面內的 table資訊
# print(bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr"))
                # 找出物件內 tag 的元素, find 僅會找一個元素 或 找第一個元素(多個元素時)

tr_list = bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr")

for single_tr in tr_list:
#    print(single_tr.find("div", {"class": 'visible-phone'}))
            # div 是通用區塊 <div class="visible-phone print_hide">
            # visible-phone , print_hide 擇一即可
#    print(single_tr.find("td", {"class": "rate-content-cash","data-table": "本行現金賣出" }))
            # find "td"中 class 內的元素, 發現若有重複, 再加上額外條件

# 取出元素, 使用 contents
    rate_name = single_tr.find("div", {"class": 'visible-phone'}).contents[0]
    rate = single_tr.find("td", {"class": "rate-content-cash","data-table": "本行現金賣出" }).contents[0]

    rate_name = rate_name.replace(" ", "")    # 消除空格
    rate_name = rate_name.replace("\n", "")   # 消除換行
    rate_name = rate_name.replace("\r", "")   # 消除斷行
    print(rate_name, ":", rate)

# 使用 csv 套件, import載入 csv的檔案做存檔
# 檔案會自動建立, 但是檔案的資料夾不會自動建立, 使用 open() 函數開啟資料夾
# 資料夾不使用絕對路徑, 僅使用相對路徑 "./ ~ /"
    file_name = "./result/" + rate_name + ".csv"
    if not exists(file_name):     # 反向寫 not exists, 若檔案不存在的時候, 執行的條件
        f = open(file_name, "a", newline='')     # 設定第2個參數, r (read), w (write), a (append) 寫完直接覆蓋
        w = csv.writer(f)
        w.writerow(["時間", "匯率"])             # 寫入檔案內的欄位, 把檔案一次性寫進 row
        f.close()
    f = open(file_name, "a", newline='')         # newline='' 避免多增加空白的換行
    w = csv.writer(f)    # 寫入這個路徑內的檔案, 並且輸出檔案
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())     # 使用 strftime 轉換成日期、時間格式的字串
    w.writerow([now_time , rate])       # 若沒有檔案一次把兩個 row 寫進去, 若有檔案就寫一個 row 即可
    f.close()            # 寫程式結尾時, 一定要做關閉的 function , 會自動結束後存檔
