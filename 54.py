import easygui
import urllib.request,urllib.parse
import http.cookiejar
import re
import chardet

def get_cat_picture():
    while True:
        data = easygui.multenterbox('请填写图片的尺寸','请下载一个图片',fields=['宽','高'])
        if data == None:
            easygui.msgbox('请输入图片的宽和高')
        else:
            break
    dirname = easygui.diropenbox('请选择存放图片的文件夹',default='.')
    url = 'http://placekitten.com/g/{}/{}'.format(data[0],data[1])
    file_name = dirname + '/cat_{}_{}.jpeg'.format(data[0],data[1])
    img = urllib.request.urlopen(url).read()
    with open(file_name,'wb') as f:
        f.write(img)


def login_douban():
    loginurl = 'https://www.douban.com/accounts/login'
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    data = {
        "form_email":"1872314654@qq.com",
        "form_password":"douban11012",
        "source":"index_nav",
    }
    #从首页提交登录
    response = opener.open(loginurl,urllib.parse.urlencode(data).encode('utf-8'))
    
    #判断地址是否正确
    if response.geturl() == 'https://www.douban.com/accounts/login':
        html = response.read()
        html = html.decode(chardet.detect(html)['encoding'])
        
    #查找验证码图片
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>',html)
    
    # <_sre.SRE_Match object; span=(11267, 11412), match='<img id="captcha_image" src="https://www.douban.c>

    if imgurl:
        #取出验证码地址
        url = imgurl.group(1)
        #将图片保存至同目录下
        filename,headers = urllib.request.urlretrieve(url,filename='v.jpg')
        #获取captcha参数
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>',html)

        if captcha:
            vcode = input('请输入图片上的验证码：')
            data['captcha-solution'] = vcode
            data['captcha-id'] = captcha.group(1)
            data['user-login'] = '登录'

            response = opener.open(loginurl,urllib.parse.urlencode(data).encode('utf-8'))
            if response.geturl() == 'https://www.douban.com/':
                print('login success!')
            else:
                print('登录失败')
        

    
if __name__ == '__main__':
    # get_cat_picture()
    login_douban()