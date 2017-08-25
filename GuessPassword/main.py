'''
import PasswordMachine
PasswordMachine.PasswordMachine()         # 安裝在某下面的設計圖
'''
from PasswordMachine import PasswordMachine

machine = PasswordMachine()
while True:
    interval = machine.returnInterval()
    message = "請輸入一個數字[" + str(interval[0]) + "," \
              + str(interval[1]) + "]"
    number = input(message)
    print("輸入的數字是", number)
    if(machine.guess(number) == True ):
        print("猜對了, 總共猜了", machine.guess_times, "次")
        break;


# 剪刀石頭布Tips
'''
if p2 == p1 % 3 +1
elif p2 == p1
'''
