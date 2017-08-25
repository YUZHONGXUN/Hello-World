import jieba
import jieba.analyse

f = open('a.txt', 'r')     # 僅讀取'r', 僅寫入'w'
# print(f.read())    # 函數加上 .read() 才能讀取
article = f.read()

# print(jieba.cut(article))       # 函數加上 .cut 作為分割
for w in jieba.cut(article):
    print(w)

print("\n---------------------\n")
result = jieba.analyse.extract_tags(article, 5)    # extract 萃取文章, 擷取最重要的字(5個字)
print(result)
