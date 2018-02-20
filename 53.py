
import urllib.request
import chardet

def get_charset():
    url = input('请输入URL：')
    data = urllib.request.urlopen(url)
    html = data.readline()
    print('该网页使用的编码是：{}'.format(chardet.detect(html)['encoding']))

def get_content():
    url_list = []
    with open('urls.txt','r') as f:
        for each in f:
            url_list.append(each.rstrip("\n"))
    for i in range(len(url_list)):
        data = urllib.request.urlopen(url_list[i]).read()
        encoding = chardet.detect(data)['encoding']
        html = data.decode(encoding)
        file_name = 'url_'+str(i)
        with open(file_name,'w',encoding=encoding) as f:
            f.write(html)

if __name__ == '__main__':
    get_content()