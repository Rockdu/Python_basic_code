a = 1
b = True
print(a is b) #比较id
print(a is not b)
print(a == b) #比较值
a = 1
b = 1
print('####################')
print(a is b) #比较id
print(a is not b)
print(a == b) #比较值
a = [1,2,3,4]
b = [1,2,3,4]
print('####################')
print(a is b) #比较id
print(a is not b)
print(a == b) #比较值
print('####################')

## --------------------------------------------------
s = 'hello world!'
print('world' in s)
print('World' in s)