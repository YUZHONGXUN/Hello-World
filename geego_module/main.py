'''
import calculator          # import 安裝進去另一個.py 副檔案

result = calculator.add(3, 4.2)
print(result)
'''

# import cal.calculator
# import cal.advanced_calculator
from cal import calculator                        # 使用 from, 可載入 package 內的套件檔案
from cal.advanced_calculator import mod as mod2       # 使用 import 內的應用函數, as 可取別名
# imported 安裝新增的套件 package, 再執行裡面的 __init__.py 檔案
# 執行套件 package後, 再執行 calculator.py 檔案

result = calculator.add(3, 4.122)        # 依循前面 import 的 cal.calculator 操作
print(result)

# result = cal.advanced_calculator.mod(3, 2)
result = mod2(3, 2)               # 若有 import 過 mod, 可直接使用 mod 函數
print(result)