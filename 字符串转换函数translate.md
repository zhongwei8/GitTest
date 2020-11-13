# 1 `translate`：基于映射表，转换字符串
```python
s = 'abcxyz123'                     # 原始字符串
m = {'a': 'A', 'b': 'B'}              # 转换字典表
t = str.maketrans(m)            # 构造成 trans
s.translate(t)                          # 对原始字符串进行转换
# 'ABcxyz123'
```