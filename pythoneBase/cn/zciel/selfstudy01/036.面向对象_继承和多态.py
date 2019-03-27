# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('Animal is running...')


# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 当然，也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):

    def run(self):
        print('Dog is running ...')

    def eat(self):
        print('Eating meat ...')


# 继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
# 判断一个变量是否是某个类型可以用isinstance()判断：
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型
print(isinstance(a, list))

print(isinstance(b, Animal))

print(isinstance(c, Dog))

# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
b = Animal()
print(isinstance(b, Dog))


# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


# 再定义一个Tortoise类型
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())
# 新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
