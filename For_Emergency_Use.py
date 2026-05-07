# import os
#
# file_path = os.path.join("Users","williamchew","Downloads")
# file_name1 = ["Menu.txt","Discount.txt","Receipt.txt","sales record.txt"]
# file_1     = os.path.join(file_path,file_name1[0])
# file_2     = os.path.join(file_path,file_name1[1])
# file_3     = os.path.join(file_path,file_name1[2])
# file_4     = os.path.join(file_path,file_name1[3])
#
#
# #1
# def Product_Display():
#     print(f"PWP Restaurant Menu:\n")
#     try:
#         print("ITEM\t\tAmount")
#         print("FOOD")
#         with open("Food/FOOD menu.txt", "r", encoding="UTF-8") as file_FOOD:
#             FOOD_lines = file_FOOD.readlines()
#             for FOOD_line in FOOD_lines:
#                 food = FOOD_line.strip().split("=")
#                 if len(food) == 2:
#                     food_1 = food[0]
#                     price_food = food[1]
#                     print(f"{food_1:<12}RM{price_food}")  # 左对齐
#                 else:
#                     print(repr(FOOD_line))  # 直接给程序员看 file 里面的错误（如空行）
#         print("\n")
#         print("DRINK")
#         with open("Beverage/Beverage menu.txt", "r", encoding="UTF-8") as file_DRINK:
#             DRINK_lines = file_DRINK.readlines()
#             for DRINK_line in DRINK_lines:
#                 drink = DRINK_line.strip().split("=")
#                 if len(drink) == 2:
#                     drink_1 = drink[0]
#                     price_drink = drink[1]
#                     print(f"{food_1:<12}RM{price_drink}")
#                 else:
#                     print(repr(DRINK_line))
#
#         print("\n")
#         print("DESSERT")
#         with open("Dessert/DESSERT menu.txt", "r", encoding="UTF-8") as file_DESSERT:
#             DESSERT_lines = file_DESSERT.readlines()
#             for DESSERT_line in DESSERT_lines:
#                 dessert = DESSERT_line.strip().split("=")
#                 if len(dessert) == 2:
#                     dessert_1 = dessert[0]
#                     price_dessert = dessert[1]
#                     print(f"{dessert_1:<12}RM{price_dessert}")
#                 else:
#                     print(repr(DESSERT_line))
#         print("\n")
#         print("HERE IS THE MENU")
#     except FileNotFoundError:
#         print("No This Menu")
# #2
# def Discount():
#     new_file_1 = []  # 把要添加的东西丢进去 (ADD)
#     new_file_2 = []  # 为了modify的部分
#     while True: # 确保输入者不会乱输入
#         item = input("Which items you wanna edit: ")
#         try:
#             with open("Discount/Discount.txt", "r", encoding="UTF-8") as file:
#                 file_1 = file.readlines()
#                 choose = input("ADD / DELETE / MODIFY : ").upper()
#
#                 if choose == "ADD":
#                     choices = input("File or Type").upper()
#                     if choices == "FILE":
#                         a          = input("Which file you want to import (DON'T SPACE): ")
#                         if not a.endswith(".txt"):
#                             a = a + ".txt"
#                         which_file = os.path.join("c",a)
#
#                         with open(which_file, "r", encoding="UTF-8") as import_file:
#                             IMPORT = import_file.readlines()
#
#
#                         with open("Discount/Discount.txt", "a", encoding="UTF-8") as files:
#                             files.writelines(IMPORT)
#                         print("SAVED")
#                         break
#
#                     elif choices == "TYPE":
#                         new_item = input("Enter new items: ")
#                         new_discount = float(input("Pls enter the discount ( like: 10 is 10%) if no discount enter '0' "))
#                         new_file_1.append(f"{new_item} = {new_discount}\n")
#                         with open("Discount/Discount.txt", "a", encoding="UTF-8") as file:
#                             file.writelines(new_file_1)
#                         print(f"{new_item} had been ADD!")
#                         break
#
#                 elif choose == "DELETE":
#
#                     for delete_item in file_1:
#                         Name = delete_item.strip().split("=")   # ["burger" , "100"]
#                         if Name[0] == item: # 确保file 的item 跟 我之前要改的东西匹配 ##记录“找到了”，用于后面是否新增##
#
#                             new_item_1 = [] #for修改的部分，之后会把剩下的保存进去，要删掉的就不会写进去 #我要把数据存在这里是因为可以一句直接 存进去，不必一个一个填
#                             for n in show_file:
#                                 item_name = n.strip().split() # 只是要设variable
#                                 if item_name[0] != item:
#                                     new_item_1.append(n) #有个问题，如果写 item以外的东西会不会崩溃
#
#                             with open("Discount/Discount.txt", "w", encoding="UTF-8") as file:
#                                     file.writelines(new_item_1)
#                                     print(f"{item} has been Deleted !")
#                                     break
#                         else:
#                             print(f"This {item} Not Found !")
#                 elif choose == "MODIFY" :
#                     with open("Discount/Discount.txt", "r") as file: #我先给输入者读，要改哪一个
#                         modify_file = file.readlines()
#                     for i in modify_file:
#                         print(i.strip())
#                     print(f"你之前的的item是: {item}")
#                     item_modify = input("New modify item: ") # 如果用户不要改呢 # 改了之后久的是否会还在
#                     item_discount = float(input("Pls enter your discount (like: 10 is 10%) if no discount enter '0' )"))
#                     new_file_2.append(f"{item_modify} = {item_discount}\n") # 就把新的资料填进新的file里
#                     break
#                 else:
#                     break
#
#         except ValueError:
#             print("Pls try again: ")
#
#         with open("Discount/Discount.txt", "w") as files: # 把所有new_file里面的东西和新的东西重新丢回进去
#                files.writelines(new_file_2)
#
#
#
# #3
#
#
# def Receipts():
#     item = input("Enter your item: ")
#     try:
#         # 找价格
#         with open("Receipt.txt", "r", encoding="UTF-8") as file:
#             A = file.readlines()
#         for receipts in A:
#             name , price_file = receipts.strip().split(" = ")
#             if item == name:
#                 price = float(price_file)
#                 break
#             else:2
#                 print("item not found")
#         # 找到价格，就折扣
#         try:
#             with open("Discount/Discount.txt", "r" , encoding="UTF-8") as file:
#                 B = file.readlines()
#             for count in B:
#                 discount_item , discount = count.strip().split(" = ")
#                 if item == discount_item:
#                     price *= (1-(float(discount)/100))#Discount 加float 是因为 discount 可能是str ，所以把它转换一下
#                     break
#         except FileNotFoundError:
#             pass
#         print(f"this item {item}: final price is: {price:.2f}")
#
#         #保存这个销售账单 （为日后可以有历史销售账单）
#         with open("sales record.txt", "a", encoding="UTF-8") as sales_file:
#             sales_file.write(f"{item},{price:.2f}/n")
#         print("Saved !")
#     except Exception as type_Error:
#         print("Mistake! Enter again: ", type_Error)
# #4
# def sales():
#     total_price = 0
#     count       = 0
#     count_items = {}
#     try:
#         with open("sales record.txt", "r", encoding="UTF-8") as sales_record_file:
#             sales_record = sales_record_file.readlines()
#             for record in sales_record:
#                 items, price = record.strip().split("=")
#                 price = float(price)
#                 #计算总共卖了多少钱
#                 total_price = total_price + price
#                 #计算总共卖了多少个产品
#                 count       = count + 1
#                 if items in count_items:
#                     count_items[items] += 1
#                 else:
#                     count_items[items] = 1
#     except :
#         print("File Not Found")
#         return
#
#     print(f"SALES REPORT")
#     print("----------------")
#     print(f"TOTAL SALES: {count}")
#     print(f"TOTAL AMOUNT: RM {total_price:.2f}")
#     print(f"\n")
#     print(f"HOT SAlES")
#     print(f"Name\t\tAmount")
#     for item_name, total_count in sorted(count_items.items(), key=lambda x: x[1], reverse=True):
#         print(f"{item_name} \t: {total_count}")
#
#
#
#
# #5
# def Cashier():
#     while True:
#         print("\nCashier Menu:\n1.Product_Display \n2.Discount\n3.Receipts.txt \n4.Sales \n5.Exit")
#         choice = input("Choose: ")
#         if choice == "1":
#             Product_Display()
#         elif choice == "2":
#             Discount()
#         elif choice == "3":
#             Receipts()
#         elif choice == "4":
#             sales()
#         elif choice == "5":
#             print("Exit")
#             break
#         else:
#             print("Invalid input.")
#
# # 开始
# Cashier()