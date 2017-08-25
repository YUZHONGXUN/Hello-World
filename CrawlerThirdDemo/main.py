from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.PhantomJS('./driver/phantomjs/bin/phantomjs')
driver.get('https://trends.google.com.tw/trends/hottrends#pn=p12')      # 開啟網頁
# print(driver.page_source)     # 印出網頁的 code 內容

for index in range(0, 3):    # 取名 '_' 表示隨便取名, 總共做3次
    time.sleep(3)     # 等待3秒, 等待載入
    day_search = driver.find_elements_by_class_name('hottrends-trends-list-date-container')    # element's' 是找"全部"的元素
    # print(day_search)

    # 找完現在的頁面
    for single_day_search in day_search:
        single_date = single_day_search.find_element_by_class_name('hottrends-trends-list-date-header-text').text
        if single_date != '':     # 如果不等於空白, 就執行以下程式
            print("-----", single_date, "-----")
            items = single_day_search.find_elements_by_class_name('hottrends-trends-list-trend-container')  # 還未確定頁面, 不用加.text
            for single_search_item in items:
                title = single_search_item.find_element_by_class_name('hottrends-single-trend-title').text
                search_times = single_search_item.find_element_by_class_name('hottrends-single-trend-info-line-number').text
                print(title, search_times)
    # 確定 button 的出現
    # 等待10秒產生計時器, presence_of_element_located 等待元素出現(不用選all), 裡面是一個 tuple(),
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'more-link')))   # 載入更多
    # 等待確定出現就點擊, for 迴圈做3次, 總共點擊2次的載入更多, 最後1次點擊完 button 就結束
    button.click()

driver.close()

