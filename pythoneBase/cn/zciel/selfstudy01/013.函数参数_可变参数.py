# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
#
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3]))

#把函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# print(calc([1,2]))
# print(calc([1,2,3]))
print(calc(1,2))
print(calc(1,2,3))

#list或者tuple，要调用一个可变参数
nums = [1,2,3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

#上面复杂的调用可以用简化的写法
person('Jack', 24, **extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
