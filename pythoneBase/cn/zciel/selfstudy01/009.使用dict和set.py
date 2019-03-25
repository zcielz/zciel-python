# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
# 第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
# dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam'] = 67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# 如果key不存在，dict就会报错
# print(d['Thomas'])  KeyError: 'Thomas'

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Thomas' in d)
print('Jack' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d)
print(d.pop('Bob'))
print(d)

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# 牢记的第一条就是dict的key必须是不可变对象。
# 因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# list是可变的，就不能作为key
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3, 1])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果,通过remove(key)方法可以删除元素
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
