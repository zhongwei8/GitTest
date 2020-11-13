# 1 重命名

```python
DataFrame.rename(self, mapper = None, 
    index = None,
    columns = None,
    axis = None,
    copy = True,
    inplace = False,
    level = None, errors = 'ignore')[source]
```
1. 映射重命名列
```python
>>>df = pd.DataFrame({'A': [1, 2, 3],'B': [4, 5, 6]})
>>>df.rename(columns = {'A': 'a', 'B': 'c'})
    a   c
0   1   4
1   2   5
2   3   6
```
2. 使用映射重命名索引
```python
>>> df.rename(index = {0: 'x', 1: 'y', 2: 'z'})
    A   B
x   1   4
y   2   5
z   3   6
```

# 2 [替换](https://www.cjavapy.com/article/738/)
```python
DataFrame.replace(self, 
    to_replace = None, 
    value = None, 
    inplace = False, 
    limit = None, 
    regex = None, 
    method = 'pad')[source]
```
1. 标量替换
```python
>>>s = pd.Series([0, 1, 2, 3, 4])
>>>s.replace(0, 5)
0   5
1   1
2   2
3   3
4   4
>>>df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
    'B': [5, 6, 7, 8, 9],
    'C': ['a', 'b', 'c', 'd', 'e']})
>>>df.replace(0, 5)
    A   B   C
0   5   5   a
1   1   6   b
2   2   7   c
3   3   8   d
4   4   9   e
```
2. 序列替换

```python
>>>df.replace([0, 1, 2, 3], 4)
    A   B   C
0   4   5   a
1   4   6   b
2   4   7   c
3   4   8   d
4   4   9   e
>>>df.replace([0, 1, 2, 3], [4, 3, 2, 1])
    A   B   C
0   4   5   a
1   3   6   b
2   2   7   c
3   1   8   d
4   0   9   e
```
3. 字典替换
```python
>>>df.replace({0: 10, 1: 100})
    A   B   C
0   10  5   a
1   100 6   b
2   4   7   c
3   4   8   d
4   4   9   e
>>> df.replace({'A':0, 'B': 5}, 100)
    A   B   C
0   100  100   a
1   1   6   b
2   2   7   c
3   3   8   d
4   4   9   e
>>> df.replace({'A': {0: 100, 4:400}})
     A  B  C
0  100  5  a
1    1  6  b
2    2  7  c
3    3  8  d
4  400  9  e
```
4. 正则表达式替换
```python
>>> df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],
...                    'B': ['abc', 'bar', 'xyz']})
>>> df.replace(to_replace=r'^ba.$', value='new', regex=True)
      A    B
0   new  abc
1   foo  new
2  bait  xyz
>>> df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)
      A    B
0   new  abc
1   foo  bar
2  bait  xyz
>>> df.replace(regex=r'^ba.$', value='new')
      A    B
0   new  abc
1   foo  new
2  bait  xyz
>>> df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})
      A    B
0   new  abc
1   xyz  new
2  bait  xyz
>>> df.replace(regex=[r'^ba.$', 'foo'], value='new')
      A    B
0   new  abc
1   new  new
2  bait  xyz

```
# 3 条件替换`pd.where()`

```python
DataFrame.where(cond,
    other = nan,
    inplace = False, 
    axis = None, 
    level = None, 
    errors = 'raise', 
    try_cast = False)[source]
"""
cond:   bool Series/DataFrame, array-like, or callable
                当条件为真时，保持原值；
                当条件为非时，从 other 中替换对应的值；
                当条件为可调用对象时，它在序列/表格上进行计算，并返回 boolean 序列/表格。
other:  标量，序列/表，或可调用对象
inplace:    布尔类型，默认为假。是否就地修改原数据
axis:           整型, 默认为空。对齐的轴
"""
```
```python
>>> s = pd.Series(range(5))
>>> s.where(s > 0)
0   NaN
1   1.0
2   2.0
3   3.0
4   4.0
dtype: float64

>>> s.mask(s > 0)
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

>>> s.where(s > 1, 10)
0    10
1    10
2    2
3    3
4    4
dtype: int64

>>> df = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
>>> df
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
>>>  m = df % 3 == 0
>>> df.where(m, -df)
   A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
>>> df.where(m, -df) == np.where(m, df, -df)
      A     B
0  True  True
1  True  True
2  True  True
3  True  True
4  True  True
>>> df.where(m, -df) == df.mask(~m, df)
      A     B
0  True  True
1  True  True
2  True  True
3  True  True
4  True  True
```
# 4 标记 `df.mask()`
