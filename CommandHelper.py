#命令辅助方式
import os
import re
import configparser
import requests
import bs4

#文件夹是否存在,不存在的话则创建
def procdir(dirname):
    if os.path.exists(dirname) == False:
        os.mkdir(dirname)

def combinesave(var):
    cf = configparser.ConfigParser()
    cf.read("config.conf")
    reportname = cf.get('folder', 'keyfolder')
    str = os.path.join('.','reports', reportname ,var)
    return str

#2月7日添加

def getNewTeacherAPKVersion():
    res = requests.get('http://mobile.17zuoye.net/Android/17Teacher/17Teacher_version.txt')
    version = str(res.text)
    versioncode = re.findall(r"android:versionName=\"(.+?)\"", version)

    if(res.status_code == requests.codes.ok):
        print(versioncode[0])
        return versioncode[0]
    else:
        return "ERROR"

def downloadNewestTeacherAPK():
    #新建文件夹，下载目标页面信息
    url='http://mobile.17zuoye.net/Android/17Teacher/'
    procdir('APK')
    print("Download APK infomation from building server...")
    res=requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'lxml')
    version = getNewTeacherAPKVersion()
    for link in soup.find_all('a'):
        if (version in link.get('href')):
            downloadLink = url + link.get('href')
            print(link.get('href'))
    #使用下载模块，下载指定的apk
    print(downloadLink)
    downloadProcess = requests.get(downloadLink)
    with open(os.path.join('.','APK','Teacher.apk'),"wb") as code:
        code.write(downloadProcess.content)
    print("DownLoad APK Version:"+ getNewTeacherAPKVersion()+" SUCCESS!")

def AutoInstallAPK(filename):
    out = os.popen('adb install -r ' + filename).read()  # os.popen支持读取操作
    print(out[-1])


APK = os.path.join('.','APK','Teacher.apk')
#2月7日添加,TEST用
getNewTeacherAPKVersion()
downloadNewestTeacherAPK()
AutoInstallAPK(APK)



