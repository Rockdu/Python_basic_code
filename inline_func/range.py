# range(start, stop, step) 创建等差数列 [start, stop) 公差step
print(range(10), list(range(10)))
print(range(5, 10), list(range(5, 10)))
print(range(10, 5, -2), list(range(10, 5, -2))) ## 负数是可行的
print(range(10, 5, -1), list(range(10, 5, -1)))
print(range(3, 10, 2), list(range(3, 10, 2)))
##-------------------------------------
print(7 in range(3, 10, 2))
print(6 in range(3, 10, 2))