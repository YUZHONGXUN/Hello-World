# *args, **kwargs
# 原先寫法
def add(num_list):
    result = 0
    for number in num_list:
        result = result + number
    return result

result = add([1, 2, 3.14, 5, 6])
print(result)

# 簡潔寫法: *args
def add(*args):        # * 表示轉成 tuple
    # print(args)
    result = 0
    for number in args:
        result = result + number
    return result

result = add(1, 2, 3.14, 5, 6)
print(result)

# 原先寫法
def add(*args, dict):
    result = 0
    for number in args:
        result = result + number
    return dict['prefix'] + result + dict['postfix']

result = add(1, 2, 3.14, 5, 6, dict = {'prefix':6, 'postfix':10})
print(result)

# 簡潔寫法: **kwargs
def add(*args, **kwargs):        # ** 表示轉成字典 dict
    result = 0
    for number in args:
        result = result + number
    return kwargs['prefix'] + result + kwargs['postfix']

result = add(1, 2, 3.14, 5, 6, prefix = 6, postfix = 10)
print(result)

# 編排順序
def printWithDecoration(content, prefix, postfix):
    print(prefix, content, postfix)

printWithDecoration(prefix = "***", content = "Hello Python", postfix = "$$$")  # 標記可告訴對應的順序