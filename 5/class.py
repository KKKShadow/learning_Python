class People:
    def __init__(self, name, age,gender,ktc,zwjs):
        self.name = name
        self.age = age
        self.gender = gender
        self.ktc = ktc
        self.zwjs = zwjs
    def print_info(self):
        print("姓名:", self.name)
        print("年龄:", self.age)
        print("性别:", self.gender)


    def print_ktc(self):
        print('口头禅：',self.ktc)

    def print_zwjs(self):
        print('自我介绍：',self.zwjs)
caixukun = People(name="蔡徐坤", age=20,gender= "男", ktc='唱跳rap篮球' ,zwjs='练习时长两年半')
caixukun.print_info()
caixukun.print_ktc()

zhangxinyu = People(name="张馨予", age=43,gender= "女", ktc='演戏' ,zwjs='演员')
zhangxinyu.print_info()
zhangxinyu.print_zwjs()
