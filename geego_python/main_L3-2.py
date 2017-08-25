# for 迴圈 + list
name_list = ["Steve", "Bob", "Amy"]     # list 會按照順序

for single_name in name_list :      # 每次擷取 list 內的值, 給予 single_name 的值且更新每次的值
    print("***", single_name)

# for 迴圈 + set
name_set = {"Amy", "Amy", "Bob", "Dior"}     # set 不會有順序

for single_name in name_set :
    print("---", single_name)

# dictionary 必須要有 key 和 value 為一組
alphabat_dict = {'a':5, 'b':10, 'c':15}

for key in alphabat_dict:
    print("key", key)
    # print("value", value)                 # 還未定義 value, 不能直接擷取 value 的值
    print("value", alphabat_dict[key])      # 在 dic 內擷取對應 key 的 value

# python 的 range() 會產生 list
# 可加入 for 迴圈
for index in range(0, 10):
    print(index)

# for 迴圈 + tuple
people_list = [("Steve", 175, 70), ("Amy",160, 45)]
# 使用 list, 用索引值擷取值
for people_tuple in people_list:
    print("name", people_tuple[0])

# list 內的元素可以是一個 tuple
# 使用 tuple, 擷取裡面的元素
for (name, height, weight) in people_list:
    print(name, height, weight)

