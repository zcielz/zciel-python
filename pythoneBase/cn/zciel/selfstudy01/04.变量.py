a = 123
print(a)

a = 'abc'
print(a)

b = 'abc'
c = b
b = 'def'
print(c)  # abc c指向b指向的结果，b指向改变了，但是c指向还是原来的值
