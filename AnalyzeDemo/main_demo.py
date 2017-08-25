from selenium import webdriver
import jieba
import jieba.analyse
import re


# 將Selenium和Webdriver連結在一起
driver = webdriver.PhantomJS(executable_path='./phantomjs/bin/phantomjs')
# Step1. 取得網頁
driver.get('https://www.ptt.cc/bbs/Boy-Girl/M.1495546810.A.7B0.html')

# Step2. 得到內容
content = driver.find_element_by_id("main-content").text

# Step3. 將文章的內容分析, 並且將推文和內容分開
content = content.split("\n")
revised_content = []
push_content = []
words = []
words_dict = {}
score = 0

pat = re.compile(" [0-9]+/[0-9]+.*")
for line in content:

    if not line.startswith('作者')\
        and not line.startswith('標題')\
        and not line.startswith('時間')\
        and not line.startswith('※')\
        and not line.startswith(':')\
        and not line == ''\
        and not line == '--'\
        and not line.startswith('Sent from')\
        and not pat.match(line):
            if line.startswith('推'):
                score = score + 1
                push_content = push_content + [line]
            elif line.startswith('噓'):
                score = score - 1
                push_content = push_content + [line]
            elif line.startswith('→'):
                push_content = push_content + [line]
            else:
                # 切斷字詞
                for w in jieba.cut(line):
                    words  = words + [w]
                    if w in words_dict:
                        words_dict[w] = words_dict[w] + 1
                    else:
                        words_dict[w] = 1

                revised_content = revised_content + [line]

print("推噓文:", push_content)
print("扣除推噓文的內容:", revised_content)
print("切斷後字詞:", words)
print("字詞出現次數:", words_dict)
print("推噓文分數:", score)

revised_article = "\n".join(revised_content)
# 透過jieba內建的idf頻率庫, 我們可以計算什麼字詞可以代表這文章
tags = jieba.analyse.extract_tags(revised_article, 3)
print("最重要字詞", tags)

# 記得關閉
driver.close()


