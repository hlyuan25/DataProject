class Person:
    def __init__(self, name, gender, age, combat):
        self.name = name
        self.gender = gender
        self.age = age
        self.combat = combat

    def bush_fighting(self):
        self.combat = self.combat - 200

    def self_learning(self):
        self.combat = self.combat + 100

    def multi_play(self):
        self.combat = self.combat - 500

    def to_string(self):
        return '姓名:' + self.name+';性别:'+self.gender+';年龄：'+self.age+';战斗力：'+self.combat


if __name__ == '__main__':
    print('——————游戏初始——————')
    bb = Person('冰冰', '女', 18, 1000)
    mm = Person('木木', '男', 20, 1800)
    mimi = Person('幂幂', '女', 19, 2500)
    print(bb.to_string())
    print(mm.to_string())
    print(mimi.to_string())
    print('——————开始游戏——————')




