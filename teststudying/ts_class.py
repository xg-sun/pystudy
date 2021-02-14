class Person:
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    def __init__(self,name,age,gender,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def eat(self):
        print(f"{self.name} eating")
        print("xxxxx")

    def play(self):
        print(f"{self.name} playing")

    def jump(self):
        print(f"{self.name} jump")


zs = Person('zhangsan', 20, 'male', 60)
print(f"张三的姓名是{zs.name},张三的年龄是{zs.age},张三的性别是{zs.gender},张三的体重是{zs.weight}.")
zs.jump()
zs.eat()
zs.play()

# print(zs.name)
# print(zs.age)
# print(zs.weight)



