import urllib.request
import re,os
from bs4 import BeautifulSoup
import chardet

def open_url(url,referer=None):
    # iplist = ['119.28.50.37:82','221.231.109.40:3128','120.77.201.46:8080','218.202.219.82:81','39.108.67.33:80']
    # proxy_handler = urllib.request.ProxyHandler({'http':random.choice(iplist)})
    # opener = urllib.request.build_opener(proxy_handler)
    request = urllib.request.Request(url)
    # opener.addheaders = [('User-Agent','User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
    if referer != None:
        # opener.addheaders = [('Referer',referer)]
        request.add_header('Referer',referer)
    # urllib.request.install_opener(opener)
    # try:
    #     response = urllib.request.urlopen(url)
    # except HTTPError as e:
    #     if hasattr(e,'code'):
    #         print(e.code)
    #     elif hasattr(e,'reason'):
    #         print(e.reason)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html


def soup(response):
    encoding = chardet.detect(response)['encoding']
    if encoding == 'GB2312':
        encoding = 'GBK'
    html = BeautifulSoup(response.decode(encoding),'html.parser')
    return html

#获取图片分类
def get_classify(url):
    response = open_url(url)
    html = soup(response)
    #找出导航栏
    nav = html.select('div > ul > li > a',limit=7)
    classify = {}
    for i in range(len(nav)):
        classify[nav[i].string] = nav[i]['href']
    classify.pop('首页')
    return classify


# 获取当前页码
def get_current_page(url):
    response = open_url(url)
    html = soup(response)
    page = html.find(class_='page_now')
    return page.string


def get_all_img(url):
    response = open_url(url)
    html = soup(response)
    all_img_url = html.select('dd > a',limit=20)
    all_img = []
    for each in all_img_url:
        all_img.append(each['href'])
    return all_img

def save_img(all_img):
    for each in all_img:
        response = open_url(each,referer=each)
        html = soup(response)
        # num = re.search(r'\d{4,}',each).group()
        foldername = html.find('h5').string
        os.mkdir(foldername)
        os.chdir(foldername)
        pages = int(re.search(r'\d+',html.find(class_='page-ch').string).group())
        page_now = int(html.find(class_='page_now').string)
        for i in range(pages):
            if page_now == 1:
                pic_url = html.find(src=re.compile(r'http://img1.mm131.me/pic/\d{4,}/\d+.jpg'))
                filename = pic_url['src'].split('/')[-1]
                img = open_url(pic_url['src'],referer=each)
            else:
                url = each[:-5] + '_'+ str(page_now) + '.html' 
                html = soup(open_url(url))
                pic_url = html.find(src=re.compile(r'http://img1.mm131.me/pic/\d{4,}/\d+.jpg'))
                filename = pic_url['src'].split('/')[-1]
                img = open_url(pic_url['src'],referer=url)
            with open(filename,'wb') as f:
                f.write(img)
            page_now += 1
        
        


def download_mm(folder='D://OOXX',pages=1):
    try:
        os.mkdir(folder)
    except FileExistsError:
        os.chdir(folder)
    
    url = 'http://www.mm131.com/'
    
    mm_classify = get_classify(url)
    
    for key in mm_classify.keys():
        print(key)
    
    chioce = input('请输入需要爬取的分类：')
    
    while True:
        if chioce in mm_classify.keys():
            url = mm_classify[chioce]
            break
        else:
            print('输入不正确')
            
    
    page_num = int(get_current_page(url))
    html = soup(open_url(url))
    a = html.find(class_='page-en')
    page_en = re.search(r'list_\d_',html.find(class_='page-en')['href']).group()
    for i in range(pages):
        if page_num == 1:
            img_url = url
            all_img = get_all_img(img_url)
        else:
            img_url = url+page_en+str(page_num)+'.html'
            all_img = get_all_img(img_url)
        
        save_img(all_img)
        page_num += 1

if __name__ == '__main__':
    download_mm()