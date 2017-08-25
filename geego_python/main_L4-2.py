# OOP 物件導向設計
# 物件: 所以東西皆為資料
# 物件導向的兩大重點
# 1. 全部的資料皆為物件, 一個物件可以擁有更多的物件(資料), 給定名字才能繼續使用
# 2. 有效大量創造同類型物件的方法, 使用設計圖的概念
class Dog():
    def __init__(self, n, a):     # 建構值, 外部連接內部, 創造的起始值
        print("INIT!!!!!!!!")     # 創造出來之後, 可被呼叫
        self.name = n             # 外部連接進來, 先設定名字
        self.age = a
    def walk(self):
        print("Dog", self.name, "walk for 10 km")

dog1 = Dog("black", 10)          # 創造新資料
print(dog1.name, dog1.age)
'''
print(dog1.walk)         # 是一種 method 的資料
dog1.walk()              # 有小括號(), 表示執行 SOP 資料
a = dog1.walk            # 也可以回傳到右邊, 再用 () 印出
a()
print(Dog)               # 是一種 class 的資料
'''
dog2 = Dog("White", 20)
print(dog2.name, dog2.age)
