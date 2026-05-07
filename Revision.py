# #1
# mylist = []
# for cnt in range(10):
#     value = input('Enter you num :')
#     mylist.append(value)
# print(mylist)
from gc import collect
from idlelib.replace import replace
from pdb import find_function
from tokenize import Exponent


# #2
# mylist = []
# mysum = 0
# size = int(input('Enter the size of list:'))
# for cnt in range(size):
#     num = int(input('Enter your nm :'))
#     mysum += num
#     mylist.append(num)
# for cnt in range(size):
#     print(mylist[cnt])
#
# #3
# mylist = [65,75,85,95,105]
# num = int(input('enter your nm :'))
# ind = -1
# for cnt in range(len(mylist)):
#     if(num == mylist[cnt]):
#         ind= cnt
#         break
# if (ind != -1):
#     print('Search successful and valus found at index:', ind)
# else:
#     print('Search Unsuccessful')

#------------------------------------

# 1
# book = {"english ": 1, "science": 2, "commerce" : 3}
# for books, numbers in book.items():
#     print(books, numbers)
#
# # 2
# student = {
#     "Student 1":{"Student_name": "Jack","Student_age" : 10,"Student_ID"  : "Tp009090"},
#     "Student 2":{"Student_name": "mammmo","Student_age" : 11, "Student_ID"  : "Tp009090"},
#     "Student 3":{"Student_name": "william","Student_age" : 12,"Student_ID"  : "Tp009090"}
# }
#
# b = list(student)
# print(b)
# i = 0
# a = list(student)
# b = len(a)
# while i > b:
#     print(student)
#     i += 1
#     break

# i = 7
# while i < 0:
#     print("")
#

# ./ current ../ go back
# delete dict
# abd.clear()

#------------------------------
#
# base = int(input("Enter base in cm: "))
# height = int(input("Enter height in cm: "))
# print(f"Area of the triangle is : {(1/2)*base*height}")
#
#
# # type 1 (easy) no parameter , no return result
# # input , process , display result
# def area_of_triangle():
#     base = int(input("Enter base in cm: "))
#     height = int(input("Enter height in cm: "))
#     area   = (1 / 2) * base * height
#     print(f"area {area}")
#
# #main program
# print("start")
# area_of_triangle()
# print("end")
#
# # RCV parameter ,  no return value
# # no input , have process , display result
# def area_of_triangle2(base,height):
#     area = (1/2)*base*height
#     print(f"is {area}")
#
# # main
# print("start")
# base = int(input("Enter base in cm: "))
# height = int(input("Enter height in cm: "))
# area_of_triangle2(base,height)
# print("end")
#
# def area_of_triangle2(x,y):     # 但是x,y 不一定需要跟着main program 的写法
#     area = (1/2)*base*height
#     x = 90                       # 也就是说 x 可以是另一个数字
#     print(f"is {area}")
#
# # main
# print("start")
# base = int(input("Enter base in cm: "))
# height = int(input("Enter height in cm: "))
# area_of_triangle2(base,height)
# print("end")
#
#
# #type3 没有parameter 但有 return value
# # user input, process, display result
# def area_of_triangle3():
#     base = int(input("Enter base in cm: "))
#     height = int(input("Enter height in cm: "))
#     area = (1/2)*base*height
#     return area
#
# # main
# print(f"{area_of_triangle3()}")
#
#
# #type 4 (有parameter , return result)
# # process, return result
# def area_of_triangle3(x,y):
#     area = (1/2)*base*height
#     return area
#
# # main
# base = int(input("Enter base in cm: "))
# height = int(input("Enter height in cm: "))
# print(f"{area_of_triangle3(base,height)}") # ()里的base,height 一定要跟着main program 的input

#-------------------------------------

#
# name = "hello world"
# print(name.upper())
#
# #2Convert the string "HELLO" to lowercase and store in variable named newvalue.
# text = "HELLO"
# newvalues = (text.lower())
# print(newvalues)
#
# #Capitalize the string "good morning" and display it
# print("good morning".capitalize())
# #Count how many times "a" appears in "banana" and display it.
# print('banana'.count("a",))
# #Replace "dog" with "cat" in "The dog barked." and store it in var named newvalue.
# newvalue = "The dog barked".replace("dog", "cat")
# print(newvalue)
# #Check if the string "sun" is in "Sunday".
# print("sun"in"sunday")
#
# def contains_substring(text, word):
#     return word in text
#
# print(contains_substring("Sunday", "sun"))
#
# print("apple".find("a"))
# #Find the index of "o" in "Hello World".
# print("Hello World".find("o"))
# #Slice the first 5 characters of "Programming".
# print("Programming"[:5])
# #Slice the last 4 characters of "Development".
# print("Development"[-4:])
# #reverse
# text = "Development"
# print(text[::-1])
# #Remove leading whitespace from " Hello".
# print(" Hello".lstrip())
# #Remove trailing whitespace from "Hello ".
# print("Hello ".rstrip())
# #Check if the string "abc123" is alphanumeric.
# print("abc123".isalpha())
# #Check if the string "1234" contains only digits.
# print("1234".isdigit())
# #Check if "hello" is lowercase.
# print("hello".islower())
# #Check if "Hello" is title case.''
# print("Hello".istitle())
# #delete
# name = ["apple"]
# name.pop("apple")
# name.remove("apple")
# del name[0]
# # set
# next(iter())
# #dict
# get
# print(name["apple"]) # 跟 list 一样，不一样的地方是 list 是 数字 dict 的话是 写key
# # insert 的话
# studnet["apple"] = 1
# print(student)
# # updated
# stdent["apple"] = orange
# print(stdent)
# # deleted 也是一样
# del student["apple"]
# ## list
# studnet = [{}]
# ##
# student = {{}}


# # 1
# INPUT =
# (
#     'John, Good morning'
#  )
# print(len(INPUT))

#2
# INPUT_1 = input('Enter: ').upper()
# # print(INPUT_1.count("a","e","i","o","u"))
#
# a = "a,e,i,o,u"
# count = 0
# for i in INPUT_1:
#     if i.strip() in a.upper().strip():
#         count += 1
# print(count)
# # 2
# Input_2 = 'John, Good morning'
# print(Input_2.count('o'))
# print(Input_2.count('i'))

#3
# po = []
# qwe = 'hello how are you'
# for i in qwe:
#     po.append(i)
# print(po)
# po.sort(reverse=True)
# print(po)

# print(qwe[::-1])

#4
# rew = "Asia Pacific University ".split()
# a = "".join(rew)
# print(a)
# # 5
# def replace_wili(sentence,original_char,new_char):
#     return question_4.replace("a","_")

# #main
# question_4 = 'Asia Pacific University'.lower()
# or_char = "a"
# nw_char = "_"
# a = replace_wili(question_4,or_char,nw_char)
# print(a)

# 6
# def abc(uni,searc):#3
#     if searc in uni:
#         return True#4
#
# searc = 'pacific' #1
# uni = input("uni").lower()
# a = ''.join(uni)
# po = abc(a,searc)#2
# print(po)#5

#7
# def question_7():
#     a = input("input:").strip()
#     b = input("delimiter:").strip()
#     Tokens = a.split(b)
#     return Tokens
#
# print(question_7())

# # 1
# def length():
#     len = "9"
#     wedth = "4"
#     return int(len) * int(wedth)
#
# a = length()
# print(a)

# # 2a
# def question4():
#     a = int(input("Enter num:"))
#     if a > 0:
#         print("Positive")
#     elif a <0:
#         print("negative")
#     elif a == 0 :
#         print("Zero")
# def question2b():
#     #2b
#     while True:
#         a = int(input("enter a num (must be positive:"))
#         if a < 0:
#             print("number must be positive")
#             continue
#         else:
#             if a % 2 == 0:
#                 print("even")
#                 break
#
#             elif a % 2 != 0:
#                 print("odd")
#                 break
# question2b()
# 5
# def count():
#     a = float(input("Enter a number as length of triangle 1:"))
#     b = float(input("Enter a number as length of triangle 2:"))
#     c = float(input("Enter a number as length of triangle 3:"))
#     if a == b == c:
#         print("Equilateral : all sides have the same length")
#     elif b == c or c == a or a == b:
#         print("Isosceles:  two equal sides and two equal angles")
#     elif a != b != c:
#         print("Scalene: all sides have the different length and angles")
#     else:
#         print("Try Again, Value invalid")
# count()
# 1
# a = "Asia"
# b = "Games"
# print(a+b)
#
# c = ("Asia","Games")
# print("".join(c))
# 2
# y = 5
# x = y * 3 + 2
# # print(x)
# a, b = 2,3;
# x= a**b
# print(x)
# a = 1;b = 2;
#
# if a < b:
#     print("True")
# else:
#     print("No")
# 5
# def question5(res):
#     return 10 * 2 + 5 / 2 - 3
# res = 10 * 2 + 5 / 2 - 3
# print(question5(res))

# a = int(input("enter num:"))
# count = a
# while count < 0 :
# print(f"\n{"Cashier Menu:":^{150}}\n{"1.Product_Display":^{150}}\n{"2.Discount":^{143}}\n{"3.Receipts":^{142}}\n{"4.Sales":^{140}}\n{"5.Exit":^{138}}")
# choice = input("Choose: ")
# while True:
#     # user input
#     item = input("Enter your item if 'done' type done: ").upper().strip()
#     if item == 'DONE':
#         break
#     while True:
#         quantity = int(input("enter the quantity: "))
#         if quantity <= 0:
#             print("quantity must be > 0")
#             continue
# try :
#     with open("sbuas.txt", 'r', encoding="UTF-8") as file:
#         for file_1 in file:
#             a = file_1.strip(",\n ")
#             print(a)
# except Exception as b:
# #     print(b)
# i = int(input("enter a number:"))
# while i >= 0:
#     print(i)
#     i -= 1
# for loop
# i = int(input("Enter a num:"))
# for a in range(0,11):
#     b = i * a
#     print(f"{i} x {a} = {b}")
# while loop
# i = int(input("Enter a num:"))
# a = 0
# while a <= 10:
#     b = a * i
#     print(f"{i} x {a} = {b}")
#     a += 1

# def price():
#     car_price = float(input("Enter your car price:"))
#     down_payment = float(input("Enter down payment:"))
#     interest = float(input("Enter loan interest rate:"))
#     year = float(input("Enter years:"))
#
#     interest_total = (car_price - down_payment) * (interest/100) * year
#     monthly_payment = (car_price - down_payment + interest_total) / (year * 12)
#     print(f"Monthly Payment: {monthly_payment}")
#     for num in range(1,6):
#         h = (car_price - down_payment) * (1 + (interest/100) * num)
#         print(f"RM{car_price - down_payment} * ({interest}/100) * {num} = RM{h}")
# price()
# for i in range(1,9):
#     print("*"*i)
# def calculate_area(x,y):
#     return x * y * (1/2)
# length = 7
# width  = 3
# a = calculate_area(length , width)
# print(a)
# def greet():
#     print(f"This is a function! ")
#     return
# greet()
# def power(x,y):
#     return x ** y
#
# base = 5
# exponent = 7
# print(power(base , exponent))
# print(len("John, Good morning"))
# a = "John, Good morning".upper()
# b = "aeiou".upper()
# count = 0
# for i in a:
#     if i in b:
#         count += 1
# print(count)
# def abc(a):
#     return a[::-1]
# a = input("Enter:")
# b = abc(a)
# print(b)
# a = input("Enter:").split()
# b = "".join(a)
# print(b)

# def abc(sentence, orgin_char, new_char):
#     return sentence.replace(orgin_char, new_char)
# a = input("enter:").lower()
# b = input("enter")
# c = "_"
# d = abc(a,b,c)
# e = d.title()
# print(e)
# def abc(a,b):
#     return (b in a)
# a = input("enter:").lower()
# b = input("enter:").lower()
# c = abc(a,b)
# print(c)
# def a():
#     b = input("enter:")
#     c = input("delimiter:")
#     ad = b.split(c)
#
#     print(ad)
# # a()

# fruits = ['Apple', 'Banana', 'Coconut', 'Durian']
# for i in range(len(fruits)):
#     a = f"{i+1}.{fruits[i]}"
#     print(a)
#
# def find():
#     ab = input("Enter:")
#     if ab in fruits:
#         print(fruits.index(ab))
#
# find()
def abc():
    total_distance = float(input("Enter the total distance of the trip(KM):"))
    km_RM = float(2.05)
    b = total_distance / 12
    count = b * km_RM
    print(f"due to 1 litle is 12 km，your {total_distance}is  {b}km")
    print(count)
abc()

# 需要多少升
# 然后总费用

def enter():

   try:
       collect = []
       while True:
            name = input("enter your name:")
            material = float(input("Enter recycling in KG:"))
            if material < 10:
                feedback = "Thanks for recycling"
            elif material < 20:
                feedback = "Good job! Keep recycling"
            elif material > 20:
                feedback = "Excellent work!"

            nima = input("Do you want to enter another resident? (yes/no):").lower().strip()
            if nima == "yes":
                collect.append(f"{name}:{material}kg -- {feedback} ")
                continue
            elif nima == "no":
                collect.append(f"{name}:{material}kg -- {feedback} ")
                for i in collect:
                    print(i)
                break
   except Exception as e:
       print(e)

enter()