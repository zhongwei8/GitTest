# 1 函数说明
## 1.1 说明
```python
os.walk(top, towdown = True, onerror = None, followlinks = False)
```
以递归的方式，自顶向下或自底向上的方式遍历目录树，对每一个目录都返回一个三元元祖(`dirpath, dirnames, filenames`)
+ `dirpath`：遍历所在目录树的位置，是一个字符串对象
+ `dirnames`：目录树中的子目录组成的列表
+ `filenames`：目录书中的文件组成的列表
## 1.2 例子
1. 将 `c:\pyhon36` 目录中的所有文件和子目录打印出来
```python
import os

try:
    for root, dirs, files in os.walk(r'c:\python36'):
        print("\033[1;31m-"*8, "directory", "<%s>\033[0m" % root, "-"*10)
        for directory in dirs:
            print("\033[1;34m<DIR>    %s\033[0m" % directory)
        for file in files:
            print("\t\t%s" % file)
except OSError as ex:
    print(ex)
```
2. 统计`c:\python36\Lib\email` 目录下所有子目录的大小，`CSV`目录除外
```python
import os
from os.path import join, getsize

for root, dirs, files in os.walk('c:/python36/Lib/email'):
    print(root, 'consumes', end = ' ')
    print(sum(getsize(join(root, name)) for name in files), end = ' ')
    print('bytes in', len(files), 'non-directory files')
    if 'CSV' in dirs:
        dirs.remove('CSV')      # 不遍历 CVS 目录

```
3. 递归删除目录的所有内容，**危险**
```python
import os
for root, dirs, files in os.walk(top, topdown = False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

```