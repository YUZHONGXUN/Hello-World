# 迴圈
import random
lottery_ticket = set()            # 設定一個空的 Set
# while 條件:
#    條件是對的(True), 我就執行這些程式碼
# while 罰寫次數 < 10:
#    罰寫
#    罰寫次數+1
while len(lottery_ticket) < 7:     # 反覆抽7次, 產生樂透彩劵
    num = random.randint(1, 20)       # random.randint 隨機抽整數
    print(num)
    lottery_ticket.add(num)

print(lottery_ticket)

# Dictionary 字典, 有 key 和 value
alphabat_dict = {'a':5, 'b':(), 'c':15}          # 可在 dictionary 內做 tuple
print(alphabat_dict)
alphabat_dict['d'] = 20    # 新增
print(alphabat_dict)
alphabat_dict['c'] = 5     # 修改
print(alphabat_dict)
alphabat_dict['c'] = alphabat_dict['c'] + 10      # 做數學運算
print(alphabat_dict)
del alphabat_dict['c']     # 刪除
print(alphabat_dict)

