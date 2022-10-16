# import tkinter
# from tkinter import *
#
# def test(argument):
#     print(argument)
#
# test("test")
#
# list = []
# list.append("hello")
# print(list)
# mnoj = {}
# print(f"My list {list}")

# class Student:
#     print("Hello")
#     def __init__(self):
#         self.height = 160
#         print("I'm alive")
#
# peremenna = Student()
# print(peremenna.height)

# class Student:
#     kolichestvo = 0
#     def __init__(self, h):
#         self.h = h
#         Student.kolichestvo += 1
#
# nick = Student(h = "test2")
# kate = Student(h = "test")
# print(nick.h)
# print(kate.h)
# print(nick.kolichestvo)
# print(Student.kolichestvo)

# class Student:
#     height = 160
#     def __init__(self):
#         print(self.height)
#         self.height += 10
# nick = Student()
# kate = Student()


# class Student:
#     def __init__(self, name = None):
#         self.name = name
#     def test(self):
#         return f"My name is {self.name}"
# nick = Student(name = "Bob")
# print(nick.test())

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 300
    def to_study(self):
        print("Time to Study")
        self.progress += 0.12
        self.gladness-= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 54
    def to_work(self):
        print("Opat na rabotu")
        self.money += 40
        self.gladness -= 10
        self.progress += 0.05
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money <= -100:
            print("Bomzh")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_work()
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4:
            self.to_work()

nick = Student(name ="Alex")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
