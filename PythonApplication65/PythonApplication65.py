#coding:cp1251
import math
from typing import List

def calc():
    x = int(input(" type num 1:"))
    y = int(input(" type num 2:"))
    print(x + y, 
          x - y, 
          x * y, 
          x / y, 
          x // y, 
          x ** y, 
          x % y)
#calc()

def calc_two():
    x = int(input("type f num:"))
    y = int(input("type s num:"))
    x += y
    #x -= y
    #x *= y
    #x /= y
    print(f"x = {x}, y = {y}")
#calc_two()


def bool_task():
   
    print(1 == 2)
    print(1 != 1)
    print(not 1 == 2)
    print(3 > 1)
    print(2 < 1)
    print(1 >= 1)
    print(0 <= 1)
    print(True and False)
    print(False or False)
    print(False and False)
    print(True and True)
    print(5 > 3 and 1 < 0)
    print(not 0)
    print(not 1)
#bool_task()

def wordsf():
    s = input("type words \n")
    print('python' in s)
    print('abc' in s)
    print('777' not in s )
    print('�����' in s)
#wordsf()

def operators_1():
    x = int(input("type num:"))
    if (x > 0 and x <10):
        print("single digit number")
    elif (x > 9 and x < 99):
        print("two-digit number")
    else:
        print("invalid number value")
#operators_1()
'''
class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi *(self.radius**2)
    def perimeter(self):
        return 2 * math.pi * self.radius

r = int(input("type radius circle:"))
if (r > 0):
    obj = circle(r)
    print("ok")
    print("������� �����:", round(obj.area(), 2))
    print("����� ����������:", round(obj.perimeter(), 2))
else:
   print("������ ������������� �����")
#obj = circle(r)
#print("������� �����:", round(obj.area(), 2))
#print("����� ����������:", round(obj.perimeter(), 2))
'''

5
def pon():
    s = input("������� �����:")
    if (s [-1] in [0, 5]):
        print(f"����� {s} ������� �� 5")
    else:
        print(f"����� {s} �� ������� �� 5")
#pon()

def sol1():
    for i in range(0,5,1):
        print(i)
    i = 0
    while i <= 5:
        print(i)
        break
    i += 1    
#sol1()

def sol2():
    for i in range(-5,5,2):
        print(i)
    i = 0
    while i <=5:
        print(i)
        i += 1
        break
#sol2()


def sol3():
    for i in range(5,-5,3):
        print(i)
    i = 0
    while i <=5:
        print(i)
        i += 1
        break
#sol3()

def sol4():
    e_str = input("������� ������:")
    for i in range(len(e_str)):
        if (i % 2 == 0):
            print(e_str[i], end="")
#sol4()

    def solution_list_1():
        numbers = []
        for _ in range(5):
            num = int(input("enter num"))
            numbers.append(num)
            numbers.count(num)
            print(numbers)


    def solution_list2():
        inputi = input("enter str:")
        lststr = list(inputi) 
        print(lststr)

        uinp = input("enter str2:")
        ulst = list(uinp)
        print(ulst)
    
def solution_list3():
        list_x = [-3, -2, -1, 0, 1, 2, 3]
        print("list is:")
        print(list_x)
        sumofelements = 0
        for element in list_x:
            sumofelements = sumofelements + element
        print("����� ���� ��������� ����� : ", sumofelements, "����� ������:",(len(list_x)), "������������ ��������� ������:",())
solution_list3()

