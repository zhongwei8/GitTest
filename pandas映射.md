# 1 apply
## 1.1 列映射

## 1.2 表映射
```python
data['d'] = data[['a', 'b']].apply(lambda x: x['a'] + x['b'], axis = 1)
```
关键的参数是 `axis = 1`, 指定计算的方向，是列而不是行，默认为 0，即按列计算。
# 2 map

# 3 transform