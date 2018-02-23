# coding=utf-8
from bs4 import BeautifulSoup
import urllib.request,urllib.parse
import re

def first():
    url = 'https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'
    response = urllib.request.urlopen(url).read().decode('utf-8')
    html = BeautifulSoup(response,'html.parser')
    viewurl = re.findall("[https://|http://]baike\.baidu\.com/view+/.*",response)
    herf = html.find_all(href=re.compile('view'))
    for each in herf:
        print(each.text,'->',''.join(['https:baike.baidu.com',each['href']]))

def second():
    word = input('请输入关键词：')
    data = {
        "word":word
    }
    word = urllib.parse.urlencode(data)
    url = 'https://baike.baidu.com/search/word?{}'.format(word)
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    html = BeautifulSoup(data,'html.parser')
    #查找是否有义项
    title = html.find('div','polysemantList-header-title')
    #查找人物简介
    if html.find(class_='lemma-summary'):
        print(html.find(class_='lemma-summary').text)
    #查找标题
    h1 = html.find('h1')
    #查找副标题
    h2 = html.find('h2')
    #查找义项里的所有列表
    li = html.find_all('li','item')
    #用做统计输出了多少个
    count = 0
    while True:
        if title != None:
            href = title.find_all('a')
            for each in href:
                yield each.string,'->',''.join(['https://baike.baidu.com',each['href']])
        if li != None:
            if h2 != None:
                yield h1.string,h2.string,'->',''.join(['https://baike.baidu.com',response.geturl()])
            else:
                yield h1.string,'->',''.join(['https://baike.baidu.com',response.geturl()])
            for each in html.find_all(href=re.compile('\/item\/.+\/\d{5,8}#viewPageContent')):
                yield each.string,'->',''.join(['https://baike.baidu.com',each['href']]) 
        quitword = input('输入任意字符将继续打印，q退出程序：')
        if quitword == 'q':
            break
# for i in second():
#     print(i)

#----------------------上面的是自己写的--------------------------------

def test_url(soup):
    result = soup.find(text=re.compile("百度百科尚未收录词条"))
    if result:
        print(result[0:-1]) # 百度这个碧池在最后加了个“符号，给它去掉
        return False
    else:
        return True

def summary(soup):
    word = soup.h1.text
    # 如果存在副标题，一起打印
    if soup.h2:
        word += soup.h2.text
    # 打印标题
    print(word)
    # 打印简介
    if soup.find(class_="lemma-summary"):
        print(soup.find(class_="lemma-summary").text)   

def get_urls(soup):
    for each in soup.find_all(href=re.compile("view")):
        content = ''.join([each.text])
        url2 = ''.join(["http://baike.baidu.com", each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "html.parser")
        if soup2.h2:
            content = ''.join([content, soup2.h2.text])
        content = ''.join([content, " -> ", url2])
        yield content
        

def main():
    word = input("请输入关键词：")
    keyword = urllib.parse.urlencode({"word":word})
    response = urllib.request.urlopen("http://baike.baidu.com/search/word?%s" % keyword)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    if test_url(soup):
        summary(soup)
        
        print("下边打印相关链接：")
        each = get_urls(soup)
        while True:
            try:
                for i in range(10):
                    print(next(each))
            except StopIteration:
                break
            
            command = input("输入任意字符将继续打印，q退出程序：")
            if command == 'q':
                break
            else:
                continue
    
if __name__ == "__main__":
    main()