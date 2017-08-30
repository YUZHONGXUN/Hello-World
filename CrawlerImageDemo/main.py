from selenium import webdriver
import urllib.request
import time

driver = webdriver.PhantomJS('./driver/phantomjs/bin/phantomjs')
driver.get('http://www.tokyodisneyresort.jp/tc/attraction/lists/park:tdl')      # 開啟網頁
# print(driver.page_source)     # 印出網頁的 code 內容

time.sleep(1)

spot_div = driver.find_elements_by_class_name('list-view-col')

for single_spot in spot_div:
    # print(single_spot)
    image = single_spot.find_element_by_tag_name('img')     # 網頁的哪一個 tag 位置
    title = single_spot.find_element_by_tag_name('h2').text
    image_url = image.get_attribute('src')          # 圖片從網頁的哪裡抓下來
    print(image_url)

    req = urllib.request.Request(url=image_url, data=b'None', headers={
        'User-Agent': ' Mozilla/5.0'})
    handler = urllib.request.urlopen(req)       # 把 url 偽裝成是瀏覽器內的 handler
    img = handler.read()                # 設定讀取出來
    # print(img, title)
    file_path = "./result/" + title + ".jpg"        # 檔案的路徑
    f = open(file_path, 'wb')       # write 只有 byte
    f.write(img)       # 要把 img 放進去才能 write
    f.close()          # 存檔的動作
driver.close()

