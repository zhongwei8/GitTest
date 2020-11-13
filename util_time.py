import datetime

"""
1 三种基本类型
    1) 标准的日期时间字符串
    2) 日期时间
    3) 整数时间戳
2 三种基本类型之间的相互转换，共 3! = 6 种转换
    1)  标准的日期时间字符串
    ...
    TODO
3 标准的日期时间字符串运算
    '2020-10-03 12:22:35' - '2020-10-02 14:39:19'
"""



datetime_str = '%Y-%m-%d %H:%M:%S'                                                  # (标准的)日期时间字符串 模式
datetime_pattern = r'[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}'     # '2020-10-11 13:03:45'

# 1 判断一个字符串，是否为(标准的)日期时间字符串，如：‘2020-10-11 13:03:45’
def isStandardDatetimeStr(st: str)-> bool:
    pattern = re.compile(datetime_pattern)
    valid = pattern.match(st)
    if valid:   return True
    return False

# 2 日期时间 to (标准的)日期时间字符串
def datetime_to_String(dt)-> str:
    if not isinstance(dt, datetime.datetime):
        print('Input error! Not a datetime.datetime object')
        return 
    return dt.strftime(datetime_str)

# 3 (标准的)日期时间字符串 to 日期时间 
def string_to_Datetime(st: str)-> datetime.datetime:
    
    if not isinstance(st, str):
        print('Input error! Not a str object')
        return 
    if not isStandardDatetimeStr(st):
        print("Input error! Not a standard datetime str type like '2020-02-14 03:42:39'" )
        
    return datetime.datetime.strptime(st, datetime_str)

# 4 (标准的)日期时间字符串 to 时间戳
def string_to_Timestamp(st: str)-> int:
    if not isinstance(st, str):
        print("Input error! Not a standard datetime str type like '2020-02-14 03:42:39'" )
    if not isStandardDatetimeStr(st):
        print("Input error! Not a standard datetime str type like '2020-02-14 03:42:39'" )
    
    struct_time = time.strptime(st, datetime_str)
    timestamp = time.mktime(struct_time)
    return int(timestamp)

# 5 时间戳 to (标准的)日期时间字符串
def timestamp_to_String(sp: (int, float))-> str:
    if not isinstance(sp, (int, float)):
        print('Input error! Not a int or float object')
        return 

    local_time = time.localtime(sp)
    time_str = time.strftime(datetime_str, local_time)

    return time_str

# 6 日期时间 to 时间戳
def datetime_to_Timestamp(dt: datetime.datetime)-> int:
    
    if not isinstance(dt, datetime.datetime):
        print('Input error! Not a datetime.datetime object')
        return

    timetuple = dt.timetuple()
    timestamp = time.mktime(timetuple)
    timestamp = int(timestamp)

    return timestamp
    
"""
from dateutil.parser import parse
parser('2020-01-03')    # datetime.datetime(2011, 1, 3, 0, 0)

imoprt pandas as pd
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']

pd.to_datetime(datestrs)

# DatetimeIndex(['2011-07-06 12:00:00', '2011-08-06 00:00:00'], dtyep = 'datetime64[ns]', freq = None)



"""