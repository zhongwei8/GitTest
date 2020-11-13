# 1 [tarfile](https://www.liujiangblog.com/course/python/63)
&emsp;&emsp;`tarfile` 是一个归档模块，与压缩模块 `zipfile` 对应。`tarfile` 模块用于解包和打包文件，包括被 `gzip`, `bz2` 或 `lzma` 压缩后的打包文件。如果是 `zip` 类型的文件，建议使用 `zipfile` 模块，更高级的功能请使用 `shutil` 模块。
# 2 定义的类
```python
tarfile.open(name = None, mode = 'r', fileobj = None, bufsize = 10240, **kwargs)
```
+ 返回：一个 `TarFile` 类型的对象(本质为打开一个文件对象)
+ `name`：文件名或路径
+ `mode`：打开模式，默认为 `'r'`，即自动解压并打开文件
# 3 Tarfile 对象
该对象提供了访问文件的接口。打包文件本质是数据块的序列。包中的每个文件成员都是由头部块和数据块组成。**包里的每个文件都是一个TarInfo 对象，所以遍历一个 TarFile 对象，就是遍历一个TarFile 对象的集合**。
```python
TarFile.getmember(name)     # 获取某个成员
TarFile.getmembers()                # 获取包内所有成员
TarFile.list(verbose = True, *, members = None) # 列表显示包内成员信息

```
# 4 例子
1. 解包到当前目录
```python
import tarfile

tar = tarfile.open('sample.tar.gz')
tar.extractall()
tar.close()
```
2. 指定包内某一类型文件被解包
```python
import os
import tarfile

def py_files(members):
    for tarinfo in members:
        if os.path.splitext(tarinfo.name)[1] == '.py':
            yield tarfile

tar = tarfile.open('sample.tar.gz')
tar.extractall(members = py_files(tar))
tar.close()

```
3. 根据文件名列表，创建不压缩的包
```python
import tarfile

tar = tarfile.open('sample.tar', 'w')
for name in ['for', 'bar', 'quux']:
    tar.add(name)
tar.close()
```
3. 使用 with 语句的写法
```python
import tarfile

with tarfile.open('sample', 'w') as tar:
    for name in ['foo', 'bar', 'quux']:
        tar.add(name)

```
4. 压缩并打包文件夹下的所有文件及目录
```python
import os
import tarfile

tar = tarfile.open('text.tar', 'w:gz')
for root, dir, files in os.walk(os.getcwd()):
    for file in files:
        fullpath = os.path.join(root, file)
        tar.add(fullpath)

```