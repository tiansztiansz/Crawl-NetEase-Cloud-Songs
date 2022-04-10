import re
import requests
import os
import time

# 构造请求头
headers = {
    'User-Agent': 'Chrome/10'
}

def main():
    print('例如：罗大佑的网址是：https://music.163.com/#/artist?id=3686','  ','ID就是：3686')
    ID=input("请输入歌手ID：")
    url='https://music.163.com/artist?id='+ID
    html=requests.get(url,headers).text
    get_id(html)

def get_id(html):
    findlink=re.compile(r'<a href="/song\?id=(\d*)">(.*?)</a></li><li>')
    findname=re.compile(r'<h2 id="artist-name" data-rid=\d* class="sname f-thide sname-max" title=".*?">(.*?)</h2>')
    singername=re.findall(findname,html)[0]
    creat(singername)
    ll=re.findall(findlink,html)
    for i in ll:
        savemusic(i[1],i[0])
        time.sleep(0.5)

def creat(singername):          #创建文件夹
    if not os.path.exists(singername):
        os.mkdir(singername)  # 如果该目录不存在就创建它
    os.chdir(singername)

def savemusic(name,id):     #保存文件
    url='http://music.163.com/song/media/outer/url?id='+id+'.mp3'
    with open(name+'.m4a','wb') as f:
        print('歌曲《',name,'》 下载中***************')
        f.write(requests.get(url=url,headers=headers).content)
        f.close()
        print("《",name,"》下载完成")
        print('')

if __name__ == '__main__':
    main()
