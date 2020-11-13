# 1 merge：基于列的横向合并
## 1.1 函数
```python
merge(left, right, how = 'inner',
      on = None, left_on = None, right_on = None, 
      left_index = False, right_index = False, sort = True,
      suffixes = ('_x', '_y', copy = True, indicator = False))
```
+ `how` : 合并的方式，有内连接、左外连接、右外连接、全外连接; 默认为内连接
+ `on` : 用于连接的列索引名称。如果不指定，默认以两个表的列名交集作为连接键
+ `left_on`:  左表中用作连接键的列名。这个参数中左右列名不相同，但代表的含义相同时非常有用。
+ `right_on`: 同上
+ `left_index`: 用左表的行索引作为连接键，退化为 JOIN 函数
+ `right_index`: 同上
+ `sort`: 将合并的数据排序，默认为 `True` 
## 1.2 说明
1. 默认以重叠列名为连接键
2. 默认是内连接 `INNER JOIN`
3. 可以多键连接，`on` 参数后传入多键列表即可
4. 如果两个表的列表不同， 可以用 `left_on`, `right_on` 指定
5. 也可以用行索引当作连接键，`left_index = True, right_index = True`，但还不如直接用 JOIN


# 2 join：基于行索引的横向合并
## 2.1 函数
```python
left.join(right, lsuffix = '_l', rsuffix = '_r')
```
## 2.2 说明
1. 基于行索引的横向合并
2. 如果两个表的列名没有重复，直接用 `left.join(right)`
3. 如果两个表的列名有重复，设置 `lsuffix, rsuffix` 参数
# 3 concat：基于轴的堆叠
## 3.1 函数
```python
pd.concat([df1, df2])     # 默认为纵向堆叠
```
## 3.2 说明：(纵向)堆叠
