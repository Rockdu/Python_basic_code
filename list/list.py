lst = ["hello", 'w', 98, 233.33, 'w']
lst2 = list(["hello", 'w', 98, 233.33, 'w'])
print(lst == lst2)

## -----------------获取索引--------------------
print(lst.index('w'))
print(lst.index('w', 4, 5)) ## [start, end)中查找
if 'w' in lst[2 : 4] :
    print(lst.index('w', 2, 4)) ## 不在[2,4)的列表中 报错
else :
    print("\'w\' not in lst[2 : 4]")
print(("abaababbaba").index("bab"))

##------------------逆向索引--------------------
print(lst[-1])

##------------------列表切片--------------------
lst2 = lst[0 : 4 : 2]
print(lst2)
lst2 = lst[0 : 5 : 2]  ##[start, end) step
print(lst2)
lst2 = lst[1 : 4]  ##[start, end)默认步长1
print(lst2)
lst2 = lst[ : 3]  ##默认前缀
print(lst2)
lst2 = lst[3 : ] ##默认后缀
print(lst2)
lst2 = lst[ : 2 : -1]  ##默认反后缀
print(lst2)
lst2 = lst[2 :  : -1]  ##默认反前缀
print(lst2)

##------------------push_back-----------------------

lst2 = lst
lst.extend(["=w="])
print(lst[-1])
'''
    lst.append(["qwq", "awa"]) ## 将["qwq", "awa"]作为一个元素添加
    print(lst)
'''
lst.extend(["qwq", "awa"]) ## 将新list中的元素添加
print(lst)

lst = lst2
lst[2::2] = ["is", "is", "end"] ## 将[start, stop) 步长为step的替换为 赋值的list 位置个数一定要大于list大小
## lst[4::2] = ["this", "is", "end"] 报错
print(lst)

## ---------------------remove-------------------------
lst.remove("is")  ##移除 第一个找到的元素 不存在报错
print(lst)
lst.pop() ##移除最后一个元素
print(lst)
lst.pop(1) ##移除第二个元素
print(lst)
lst[1:2] = [] ##移除一段
print(lst)
##lst.clear() ##清空
print(lst)
del lst  ## 删除