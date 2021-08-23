t1 = (1, 2, 3)
print(t1)
## t1[0] = 1 报错 元组不可更改
t2 = 1, 2, 3
print(t1 == t2)
t3 = ('X',)
print(t3) ## 一元元组
print(()) ## 空元组

## 元组是不可变的指针数组，指向的可变元素可变，指向的不可变元素不可变
t = (10, [20, 30], 9)
print(t)
print(t[0], type(t[0]))
print(t[1], type(t[1]))
print(t[2], type(t[2]))
## t[0] = 100 报错
t[1].append(10)
print(t)
t[1][1] = 20
print(t)

## for 循环遍历
for i in t :
    print(i, end = " ")
print()