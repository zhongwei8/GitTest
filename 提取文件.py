import tarfile
import datetime
import os

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
# 6 构建字典：'日期-电话' -> 文件名
def dateTel2FileName(datetelnames):
    datetel2file_name = {date + '-' + tel: name for (date, tel, name) in datetelnames}
    return datetel2file_name

# 7 在源文件基础上补充文件名
def updateSummary(summaryPath,datetel2file_name):
    summary = pd.read_csv(summaryPath)
    cols = summary.columns
    phones = summary['user_phone'].apply(lambda x: x.split('-')[1])
    dates = summary['date']
    summary['date-tel'] = [str(date) + '-' + phone for date, phone in zip(dates, phones)]
    for i in summary.index:
        if summary.loc[i, 'date-tel'] in datetel2file_name:
            summary.loc[i, 'file_name'] = datetel2file_name[data.loc[i, 'date-tel']]
    summary[cols].to_csv(summaryPath, index = False, mode = 'w')
    return summary[cols]




tabpath = '/home/mi/temp/睡眠数据采集(第2轮)/日间记录/汇总/日间汇总.csv'
insertFileName(tabpath, datetel2file_name)