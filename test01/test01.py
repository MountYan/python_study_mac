class People:
    country = 'china'  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量

    @classmethod
    def get(cls):
        print(cls.country)
        # print(cls.name)


if __name__ == '__main__':
    people = People('liyanze')
    people.get()
