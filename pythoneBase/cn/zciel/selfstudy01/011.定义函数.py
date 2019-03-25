# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-11))


# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

# 空函数 如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass


age = 18
if age >= 15:
    pass


# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs('adf')
print(my_abs(1.2))

# 返回多个值
import math


def mov(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = mov(100, 100, 60, math.pi / 6)
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值
r = mov(100, 100, 60, math.pi / 6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
