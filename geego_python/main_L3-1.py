# if, else 迴圈
score = 91

if score > 90 :      # python 的迴圈的 : 和 {} 相同效果
    print("Excellent")      # 在 if 所屬的動作要做縮排
elif score > 80 :           # elif, else 和 if 相同排的位置
    print("Good")
else:
    print("SOSO")

# python 內的迴圈通常是使用 while
# while 應用於未知迴圈執行幾次後會停止的情況
# 練習: 1 + 2 + ... + 10 的結果
result = 0                   # 初始條件
end = 10
# 判斷條件 -> true -> 執行 -> 判斷條件 -> false
pivot = 0
while pivot < end :          # 判斷條件, pivot < end 不斷做迴圈重複執行, 直到滿足條件後停止
    result = result + (pivot + 1)
    pivot = pivot + 1        # 步進條件
print(result)                # 若是縮排, 則表示在 while 內執行的動作

# while 迴圈 加上 break
result = 0
pivot = 0
end = 5000
while result < end:
    result = result + (pivot + 1)
    pivot = pivot + 1
    if result >= end:            # 1 + 2 + ... + 100 = 5050 > end = 5000, 所以 break 跳出執行停止
        break
print(pivot)

