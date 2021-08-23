a = 79
'''
if a >= 60 :
    print("Pass!")
else : 
    print("GG!")
'''

print("Pass!" if a >= 60 else "GG!") ##三目运算符 a >= 60 ? "Pass!" : "GG!"

##--------------------------------------------

print("GPA:", end = '')
if a >= 85 :
    print("4.0")
elif a >= 60 : 
    print(4.0-(85-a)*0.1)
else: 
    print(0)

##--------------------------------------------

a = -1

if a >= 0 :
    pass   ##占位语句无实际意义
else :
    print("No kidding!")