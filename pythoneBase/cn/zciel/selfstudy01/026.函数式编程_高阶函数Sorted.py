# Python内置的sorted()函数就可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# list = [36, 5, -12, 9, -21]
# keys = [36, 5,  12, 9,  21]
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：
#
# keys排序结果 => [5, 9,  12,  21, 36]
#                 |  |    |    |   |
# 最终结果     => [5, 9, -12, -21, 36]

# 字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# 对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# sorted传入key函数，即可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# 小结
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
