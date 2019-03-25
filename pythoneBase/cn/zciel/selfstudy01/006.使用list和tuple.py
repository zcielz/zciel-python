classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(classmates[1])
# print(classmates[3]) #IndexError
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print(L)

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
# 它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 要定义一个只有1个元素的tuple
t = (1)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
