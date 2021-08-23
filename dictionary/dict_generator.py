item = ['A', 'B', 'C']
value = [10, 20, 30, 1000, 1000]  ## zip打包新列表长度为所有的min
print(list(zip(item, value))) ## 对应打包成元组 返回zip类型，转为列表

## 字典生成式
d = {i : j for i,j in zip(item, value)}
print(d)
print({i : 1 for i in range(10)})