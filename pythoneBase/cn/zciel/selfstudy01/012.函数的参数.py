# ython的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
def power(x):
    return x * x


print(power(4))


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 9))


# 默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3))


# 一是必选参数在前，默认参数在后

def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())

#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

