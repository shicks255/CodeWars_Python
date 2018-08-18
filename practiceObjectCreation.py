# !python 3


class Person():
    age = ""
    name = ""

    # constructor
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        print("Person - " + self.name)

class Man(Person):
    sex = ""

    # constructor
    def __iter__(self, sex, age, name):
        super(age, name)
        self.sex = sex

    def __str__(self):
        print("Man - " + self.sex + " " + self.age + " " + self.name)

john = Person(25, 'john')
erica = Person(32, 'erica')

# steve = Man("M", 25, 'steve')

# print(john)
# print(erica)
# print(steve)

numbers = [1,2,3,4,5]

numbersSqr = list(map(lambda x: x * 2, numbers))

print(numbersSqr)
# for x in numbersSqr:
#     print(x)