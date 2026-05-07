# fruits = ['Apple', 'Banana', 'Coconut', 'Durian']
# for i in range(len(fruits)):
#     print(f"{i+1}. {fruits[i]}")
# #
# # # def find():
# # #     user_input = input("Enter fruits name:").strip()
# # #     print(fruits.index(user_input))
# # # find()
# #
# # def abc():
# #     exxtend = ['Elderberry','Fig']
# #     fruits.extend(exxtend)
# #     print(fruits)
# #     print(f'Total Items:{len(fruits)}')
# #
# # abc()
#
# # def replace():
# #     previous = input("Enter fruits that you wanna change:").strip()
# #     new      = input("Enter fruits that is new:").strip()
# #     if previous in fruits:
# #         a   = fruits.index(previous)
# #         fruits[a] = new
# #         print(fruits)
# # replace()
#
# # def delete(fruits_list,fruits_name):
# #     if fruits_name in fruits:
# #         index_ = fruits.index(fruits_name)
# #         del fruits[index_]
# #     print(fruits_list)
# #
# # name = input("Enter fruits:").strip().capitalize()
# # delete(fruits,name)
#
# def sortDes():
#     print(fruits[::-1])
# # sortDes()
# tuple_store = ('TP0123','Dalwin','APD1F2403IT','3.1')
# print(tuple_store)
# print(tuple_store[0])
# print(tuple_store.index("Dalwin"))
from idlelib.replace import replace

# dict_store =\
# {
# 'TP Number ': 'TP0123',
# 'Name': 'Dalwin',
# 'Intake': 'APD1F2403IT',
# 'CGPA': '3.1'
# }
# for key , value in dict_store.items():
#     print(key,value)
#
# dict_store["Society"] = 'Student Union, Programming Club, Debate Club'
#
# print(dict_store["Society"])
# dict_store["Name"] = 'Devinder'
# print(dict_store['Name'])
#
# set_store = {
#     "TP0123",
#     "Dalwin",
#     "APD1F2403IT",
#     "3.1"
# }
#
# print(set_store)
# if "TP0123" in set_store:
#     print("TP0123")
#
# set_store.add("APD1F2403IT")
#
# set_store.add(3.5)
# set_store.remove("3.1")
# print(set_store)
fruits = ['apple','orange','banana','grape']
for i in fruits:
    if 'apple' in fruits:
        index_fruits = fruits.index('apple')
        del fruits[index_fruits]
print(fruits)

print(replace(fruits[2],'kiwi'))
# password = 'william'
# def login():
#     count = 0
#     try:
#         while count < 3:
#             user_password = input("Enter your password: ").strip()
#             if user_password.strip() == password.strip():
#                 print("Login Successful")
#                 break
#             else:
#                 print("Try Again")
#                 count += 1
#         if count == 3:
#             print("you have attempt 3 times")
#     except Exception as Error:
#         print(Error)
# login()

