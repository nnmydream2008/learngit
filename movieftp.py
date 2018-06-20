#!/usr/bin/env python3.6
#_*_ coding:utf-8 _*_
import requests
import os
import time
from bs4 import BeautifulSoup
allurllist=[]
def all_page():
    url='http://www.ygdy8.net/html/gndy/oumei/list_7_1.html'
    headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    resp=requests.get(url,headers=headers)
    s=requests.session()
    s.headers.update(headers)
    s.keep_alive=False
    html=resp.text
    soup=BeautifulSoup(html,'html.parser')
    pages=soup.find_all('option')
    pagenumber=int(str(pages[-1]).split('">')[-1].split('<')[0])
    baseurl='http://www.ygdy8.net/html/gndy/oumei/list_7_'
    for i in range(1,pagenumber+1):
        allurl=baseurl+str(i)+'.html'
        allurllist.append(allurl)
pageurllist=[]
def page_url():
    for url in allurllist:
        print('正在解析第',allurllist.index(url)+1,'页......')
        headers={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        resp=requests.get(url,headers=headers)
        s=requests.session()
        s.keep_alive=False
        s.headers.update(headers)
        resp.encoding='gbk'
        html=resp.text
        soup=BeautifulSoup(html,'html.parser')
        ulinks=soup.find_all('a',class_='ulink')
        urls=[]
        for i in ulinks:
            urls.append(i['href'])
        for i in urls:
            l1=i.split('/')
            if l1[-1]=="index.html":
                urls.remove(i)
        print(urls)
        for i in urls:
            allurl='http://www.dytt8.net'+i
            pageurllist.append(allurl)
    print('总抓取到',len(pageurllist),'页电影详情页面')
synopsislist=[]
ftplinklist=[]
def catch_highscoremovie(list):
    for pageurl in list:
        print('正在分析第',list.index(pageurl)+1,'个电影详情网页，总',len(list),'页......')
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
        print(pageurl)
        resp=requests.get(pageurl)
        requests.adapters.DEFAULT_RETRIES=5
        s=requests.session()
        s.keep_alive=False
        s.headers.update(headers)
        resp.encoding='gbk'
        html=resp.text
        soup=BeautifulSoup(html,'html.parser')
        score=soup.find_all('span',style='FONT-SIZE: 12px')
        if score!=[]:
            try:
                s=float(str(score[0]).split('IMDB评分')[1].split(' ')[0].split('/')[0])
                if s>5:
                    synopsis=str(score[0]).split('◎简')[-1].split('<img')[0]
                    synopsislist.append(synopsis)
                    link=soup.find_all('td',style="WORD-WRAP: break-word",bgcolor="#fdfddf")
                    ftplink=str(link[0]).split('"')[5]
                    ftplinklist.append(ftplink)
                    print('ftplink保存完成!')
                else:
                    print('分数低于预估值!')
            except:
                try:
                    s=float(str(score[0]).split('IMDB评分')[1].split(' ')[1].split('/')[0])
                    if s>5:
                        synopsis=str(score[0]).split('◎简')[-1].split('<img')[0]
                        synopsislist.append(synopsis)
                        link=soup.find_all('td',style="WORD-WRAP: break-word",bgcolor="#fdfddf")
                        ftplink=str(link[0]).split('"')[5]
                        if ftplink=="#ff0000":
                            ftplink=str(link[0]).split('"')[7]
                            ftplinklist.append(ftplink)
                            print('ftplink保存完成!')
                        else:
                            ftplinklist.append(ftplink)
                            print('ftplink保存完成!')
                    else:
                        print('分数低于预估值!')
                except:
                    print('IMDB评分获取失败!')
        else:
            print('网页访问失败!')
def filewriteintolist():
    urllist=[]
    with open('/data/shell/tmp/movie/pageurl.txt') as f:
        line=f.read().splitlines()
        print(line)
        for i in line:
            print(i)
            urllist.append(i)
    return urllist
def movieintofile():
    filename='HighScoreMovieftplinks.txt'
    if os.path.exists('/data/shell/tmp/movie/HighScoreMovieftplinks.txt'):
        os.remove('/data/shell/tmp/movie/HighScoreMovieftplinks.txt')
    os.chdir(os.path.join('/data/shell/tmp','movie'))
    with open(filename,'w') as f:
        for i in ftplinklist:
            print('正在保存第',ftplinklist.index(i)+1,'个电影到文件中......')
            f.write('\n'+'电影下载地址：'+i+'\n')
            f.write('电影简介：'+'\n')
            f.write(synopsislist[ftplinklist.index(i)])
    print('文件已保存成功！')
def pagewriteintofile(list):
    filename='pageurl.txt'
    os.chdir(os.path.join('/data/shell/tmp','movie'))
    with open(filename,'w') as f:
        for i in list:
            print('正在写入第',pageurllist.index(i)+1,'页')
            f.write(i+'\n')
#all_page()
#page_url()

#pagewriteintofile(pageurllist)
catch_highscoremovie(filewriteintolist())
print(len(ftplinklist))
movieintofile()




