```sh
path='/home/mi/temp/睡眠数据采集(第2轮)/所有文件/2020_11_05.tar.gz' 
tar -tf $path                   # 遍历压缩文件 path 内的文件
tar -tvf $path                  # 包含文件信息



```

上传方式：
1. 手表app端上传
2. adb 端上传

adb

```sh
cd /usr/lib/android-sdk/platform-tools/
adb root

adb pull /sdcard/sensor-data
adb shell ls /sdcard/sensor-data
adb shell
cd /s
cd /sdcard/

adb shell ls /sdcard/sensor-data
(base) mi@mi:/usr/lib/android-sdk/platform-tools$ sudo adb pull /sdcard/sensor-data

```

# 1 遍历文件夹下的所有文件
```python
for parent, dir_names, file_names in os.walk(person_dir):
    for file_name in file_names:
        print(file_name)

```
```python
import tarfile
import os

def untar(fname, dirs):
    t = tarfile.open(fname)
    t.extractall(path = dirs)

if __name__ == "__main__":
    untar("del.tar.gz", ".")


import tarfile
import os

def tar(fname):
    t = tarfile.open(fname + '.tar.gz", "w:gz")
    for root, dir, files in os.walk(fname):
        print(root, dir, files)
        for file in files:
            fullpath = os.path.join(root, file)
            t.add(fullpath)
    t.close()
if __name__ == "__main__":
    tar("del")
```

# 2 [获取压缩文件内的文件](https://www.liujiangblog.com/course/python/63)
```python
import tarfile
path = '/home/mi/temp/睡眠数据采集(第2轮)/所有文件/2020_11_05.tar.gz'
tar = tarfile.open(name = path, mode = 'r')
files = [i.name.split('/')[-1] for i in tar]
```

```python
import tarfile
import datetime

def getweakupdate(time: str)->str:  
    # 功能：输入入睡时间，获取醒来日期
    # 输入要求： '2020_07_03_23_13_04'
    # 输出：'20200704', 醒来日期
    cur = datetime.datetime.strptime(time, '%Y_%m_%d_%H_%M_%S')    # 将字符串格式转换为时间格式
    delta = datetime.timedelta(hours = 8)                          # 8 小时时间差
    date = cur + delta                                             # 时间相加，得到醒来的时间
    datestr = date.strftime('%Y%m%d')                              # 将时间格式转化为字符串, 形如 '20200704'
    return datestr



path = '/home/mi/temp/睡眠数据采集(第2轮)/所有文件/2020_11_05.tar.gz'

tar = tarfile.open(path)
filesWithsize = [(member.name, member.size) for member in tar.getmembers()]   # 获取文件路径名, 文件大小
names = [file.split('/')[-1] for (file,size) in filesWithsize if size > 0]    # 获取非空文件的文件名

wakeupdateAndtel = [(getweakupdate(name[:19]), name.split('-')[1]) for name in names] # 通过文件名，获取 (电话, 醒来日期)



```


```python
# (1) 通过文件上传时间判断是否为夜间
def judgeNight(time: str)->bool: 
    # 功能：判断文件是否为夜间
    # 输入：'2020_10_03_23_34_51'，上传时间
    hour = int(time[11:13])
    night = hour >= 20 or hour <= 6
    return night

# (2) 通过 time 提取醒来日期
def getweakupdate(time: str)->str:  # 输入要求: ’2020_07_03_23‘
    cur = datetime.datetime.strptime(time[:13], '%Y_%m_%d_%H')     # 将字符串格式转换为时间格式
    delta = datetime.timedelta(hours = 6)                          # 6 小时时间差
    date = cur + delta                                             # 时间相加，得到醒来的时间
    datestr = date.strftime('%Y%m%d')                              # 将时间格式转化为字符串, 形如 '20200704'
    return datestr

# 1 读取 压缩文件(path) 下的所有 zip 文件的 文件名及其大小
def getFileAndSize(path):
    tar = tarfile.open(path)
    fileWithSize = [(member.name, member.size) for member in tar.getmembers()]
    return fileWithSize

# 2 提取有效文件
def getValidFiles(fileWithSize):
    validFiles = [file for (file,size) in fileWithSize if size > 0]
    return validFiles

# 3 提取夜间文件
def getNightFiles(validFiles):
    nightFiles = [file for file in validFiles if judgeNight(file.split('/')[-1][:19])]
    return nightFiles

# 4 提取日间文件
def getDayFiles(validFiles):
    dayFiles = [file for file in validFiles if not judgeNight(file.split('/')[-1][:19])]
    return dayFiles

# 5 提取 (日期, 电话, 文件名) 三元组
def getDateTelName(files, nightOrday = 'day'):
    assert nightOrday in {'day', 'night'}
    
    names = [file.split('/')[-1] for file in files]
    timeTelNames = [(name.split('-')[0][:19], name.split('-')[1], name) for name in names]
    
    if nightOrday == 'day':
        return [(time[:10].replace('_', ''), tel, name) for (time, tel, name) in timeTelNames]
    elif nightOrday == 'night':
        return [(getweakupdate(time[:13]), tel, name) for (time, tel, name) in timeTelNames]





```