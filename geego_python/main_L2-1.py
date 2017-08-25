# 布林值
a = True
b = False

c = a and b     # T and F , 結果為 False
print(c)

c = a or b      # T or F , 結果為 True
print(c)

print(5 > 2 and 3 == 3)      # and 的左右都是 True , 結果為 True

# 字串
slogan = 'Hello Python'

print(slogan[1])            # 印出第1個字元
length = len(slogan)        # 查看元素的數量
print(length)
print(slogan[length- 1])    # 從最後1個字元擷取出來

print(slogan[2:5])          # 擷取第2個字元到第5個字元

slogan = slogan + " Ver.2"    # 加上字串後回傳到左邊
print(slogan)

print('Pyto' in slogan)       # 字串中沒有符合 Pyto的元素

print(slogan == 'Hello Python Ver')    # 在 print 中字串是否符合, 印出布林值

print('Hello Python\naaa')     # \n 是換行符號
print('Hello Python\\aaa')     # \\ 是字元符號, 跳脫字元的符號
print('Hello Python\"aaa')     # '' 內的 \", 可印出 "

slogan = slogan.replace('o', 'z', 1)      # . 是取用下方的子屬性資料, 回傳後再執行 replace
print(slogan)

print(slogan.startswith('el'))      # 若開頭 el, 則回傳 True

price = '10000'
print(price.isdigit())              # 若是字串內都是數字則回傳 True

slogan = slogan.upper()             # 字串內全改為大寫
print(slogan)

