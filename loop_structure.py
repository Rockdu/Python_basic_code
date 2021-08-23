a = 1
while a <= 10 :
    print(a)
    a+=1

for i in 'Python' :
    print(i+" ", end='')
print()

for i in range(0, 10, 2) :
    if i == 6 :
        break
    else :
        print(i, end='')
print()

for i in range(0, 10, 2) :
    if i == 6 :
        continue
    else :
        print(i, end='')
print()

for i in range(3) : 
    txt = input()
    if bool(txt) == True :
        print("有效输入")
        break
    else : pass
else : print("三次输入均为空") ## else : 循环完整执行完后执行的内容
