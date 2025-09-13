def print_hi(name, age, gender):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    str1 = ['a', 'b', 'c', 'd']
    print(str1)
    str2 = (1, 2, 3, 4)
    print(type(str1), type(str2))
    print(str1, str2)
    a = {"yuxiang":1, "xujiacheng":2}
    b = {"name": 'xujiacheng'}
    print(type(a.keys()))
    print(min(a.values()))
    print(a.__len__())

    char = str1[1]
    num = str2[2]

    match char, num:
        case 'a', 1:
            print(f"char is {char}, num is {num}")
        case 'b', 3:
            print(f"char is {char}, num is {num}")
        case 'c', 2:
            print(f"char is {char}, num is {num}")
        case 'd', 4:
            print(f"char is {char}, num is {num}")
        case _:
            print("not matched")

    match a:
        case {}:
            print(a|b)
        case _:
            print("not matched")

    num1 = 10
    num2 = num1
    num1 += 10
    print(num1, num2)

    print(b['name'].upper())

    string = '伟大的中国梦'
    print('as@slfj@fls@ lfsjf'.split('@'))
    print(f'{num1:%}')

    s_encode = string.encode('utf-8','strict')
    print(string, s_encode)
    print(''.join([string, 'test']))
    print(''.join(str1))

    print(name, age, gender)
    print(t)

    print((lambda x, y:x + y)(3, 4))

    print(sum((1, 2, 3)))

    print('{0:2d} | {1}'.format(5, '你好'))

class Student(object):
    attribute = 'person'
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def func1(self):
        print(self.__name, self.age, self.gender)

    @staticmethod
    def get_attribute():
        print(Student.attribute)

    @classmethod
    def test(cls):
        print('test')


if __name__ == '__main__':
    t = 10
    print_hi('mytest', 18, gender='m')

    stu = Student('xujiacheng', 18, 'male')
    print(Student.attribute)
    print(stu.name)
    print(stu.age)
    stu.test()
    Student.test()
    Student.get_attribute()
    stu.get_attribute()

    Student.func1(stu)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
