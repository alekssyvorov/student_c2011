import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 50
    def to_work(self):
        self.money += 50
        self.gladness -= 10
        self.progress += 5

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep!")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < 5:
            print("Bankrout")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 1)}")
        print(f"Money = {round(self.money, 1)}")

    def live(self, day):
        d = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()


name = input("Input name ")
nick = Student(name=name)
for i in range(1, 366):
    if nick.alive == False:
        break
    nick.live(i)
