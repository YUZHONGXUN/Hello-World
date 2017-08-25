# 群集
personal_data = ('Steve', 175, 70)

# Tuple 把這三個元素合併成一個元素
print(personal_data[0])     # 印出第0個索引值的元素

personal_data = personal_data + ('Male', 30)     # 增加新元素進 Tuple
print(personal_data)

# del personal_data[0]     # del 可刪除第0個索引值的元素

print('abc' + str(3))      # 用 str 字串加入
print('Personal:' , 3, personal_data)     # 印出字串, 數字, Tuple內元素

# List 當作"相同型態"的排隊
name_list = ["Steve", "Bob", "Emily"]
print("List:", name_list)
name_list = name_list + ["David"]      # 加入元素進 list
print(name_list)
del name_list[1]        # del 完不會回傳答案
print(name_list)

# 專屬技能
name_list.append("Amy")       # append 呼叫回傳
print(name_list)
name_list.insert(0, "Athena")      # index 座號的位置, insert 加入索引值的位置
print(name_list)
name_list.remove("David")          # 在 list中 remove 值
print(name_list)

people_list = [('Steve', 175, 70),
               ("Bob", 180, 80),
               ("Amy", 160, 45)]
print(people_list[2])            # 擷取 list 第2個索引值的元素
print(people_list[2][1])         # 擷取 list 第2個索引值內的第1個索引值元素
print(len(people_list))

# Set 內的元素不會重複印出, 無順序性, 無法用索引值
lottery = {3, 23, 17, 3}
print(lottery)                   # 不會重複印出相同的元素

lottery.add(25)
lottery.add(17)
print(lottery)

# lottery.remove(31)         # 在 Set 內就刪除, 不在裡面會發生 Error
lottery.discard(31)        # 在 Set 內就刪除

lottery = lottery.union({12, 8})      # 聯集 union 需要指定回傳
print(lottery)

