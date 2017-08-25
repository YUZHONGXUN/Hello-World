def add(num1, num2 = 4, num3 = 4):    # 其中一個有設預設值, 後續的值都必須要設定預設值
    print(num1)
    print(num2)
    print(num3)
    return num1 + num2 + num3

result = add(3, 5)         # 未代入值, 則使用預設值當作資料
print(result)