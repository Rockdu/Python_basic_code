d2 = {"c" : 1, "a" : 1, "b" : 2}
print(type(d2.keys()), d2.keys())
print(type(d2.values()), d2.values()) ## 不去重
print(type(d2.items()), d2.items())
for i in d2 :
    print(i)