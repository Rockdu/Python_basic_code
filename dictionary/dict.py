d1 = {"a" : 1, "b" : 2}
d2 = {"b" : 3, "a" : 1, "b" : 2}
d3 = dict(a = 1, b = 2)
print(d1)
print(d2)
print(d3)
print(d1 == d2, d2 == d3)

## get和下标访问
print(d1["a"], d1.get("a"))
## print(d1["c"]) 报错
print(d1.get("c"))  ## 返回None
print(d1.get("c", "没有找到的默认值")) ## 自定义返回值

## in / not in / 新增键 / 删除键
print("c" in d1)
d1["c"] = 3
print("c" in d1)
del d1["c"]
print("c" not in d1)
