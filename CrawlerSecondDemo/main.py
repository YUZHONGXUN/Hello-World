from selenium import webdriver
import time      # import 時間的套件

# 物件導向是設計圖, 參數傳入可建立物件
driver = webdriver.Chrome("./driver/chromedriver.exe")      # 必須要下載最新版本的 chromedriver.exe
driver.get("https://www.facebook.com/")     # 取得網頁, driver 出瀏覽器 chrome, 使用 python 開啟 facebook

# 在 chrome 的 開發人員工具中的 html, 尋找對應的 code
# enter email
email = driver.find_element_by_name("email")
email.clear()     # 先清除裡面輸入的字串, 以防萬一
email.send_keys('spark82475@hotmail.com')     # 輸入 email 的欄位

password = driver.find_element_by_name("pass")
password.clear()
password.send_keys('loveyou04551.')     # 輸入 password 的欄位

# submit form
form = driver.find_element_by_id("login_form")
form.submit()

time.sleep(1)      # 先不要有任何動作, 等待1秒鐘後重新整理頁面

# 先找重整過後的頁面, 再從頁面中找貼文的文章 (有兩層)
print(driver.find_element_by_class_name('fbUserPost').find_element_by_class_name('userContent').text)

time.sleep(1)

driver.close()    # 做完動作一定要關閉, 避免佔記憶體和流出資料

