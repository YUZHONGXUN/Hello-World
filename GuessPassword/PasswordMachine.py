import random

class PasswordMachine():
    def __init__(self, min_num = 1, max_num = 100):       # 創造下限和上限
        self.min_number = min_num
        self.max_number = max_num
        self.answer = random.randint(min_num, max_num)
        # print(self.min_number, self.answer, self.max_number)
        self.guess_times = 0

    def guess(self,number):
        try:                       # 防呆機制: 防呆處理非數字
            int(number)
        except:
            print("請不要亂輸入")
            return False
        number = int(number)       # 輸入數字, 但是超過最大值, 或小於最小值
        if number > self.max_number or number < self.min_number:
            print("請不要亂輸入")
            return False

        self.guess_times = self.guess_times + 1     # 猜完進入下一次
        if number == self.answer:
            return True
        elif number < self.answer:
            self.min_number = number
            return False
        else:
            self.max_number = number
            return False

    def returnInterval(self):
        return (self.min_number, self.max_number)