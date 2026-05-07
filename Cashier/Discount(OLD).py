import os
def discount():
    new_file_1 =[]
    while True:  # 确保输入者不会乱输入
        try:
            #main
            with open("../data/Discount.txt", "r", encoding="UTF-8") as file:
                file_1 = file.readlines()
                print("Item\t\tDiscount")
                for file1 in file_1:
                    Discount = file1.strip().split("=")
                    if len(Discount) == 2:
                        item     = Discount[0]
                        discount = Discount[1]
                        print(f"{item:<12}{discount}(%)")
                    else:
                        print(repr(file1))

            print(f"\n\n1. ADD\n2. DELETE\n3. MODIFY\n4. EXIT")
            choose = input("PLEASE Enter the number (only number):").strip()
            # start first
            if choose == "1":
                choices = input("File or Type: ").strip().upper()
                if choices == "FILE":
                    try:
                        while True:
                    # try:
                            a = input("Which file you want to import (DON'T SPACE): ")
                            if not a.endswith(".txt"):
                                a = a + ".txt"
                                which_file = os.path.join("/Users/williamchew/Downloads/", a)
                            else:
                                which_file = os.path.join("/Users/williamchew/Downloads/", a)

                            with open(which_file, "r", encoding="UTF-8") as import_file:
                                IMPORT = import_file.readlines()
                                print(f"Item\t\tDiscount")
                                for show_import in IMPORT:
                                    show = show_import.strip().split("=")
                                    if len(show) == 2:
                                        import_item = show[0]
                                        import_discount =  show[1]
                                        print(f"{import_item:<12}{import_discount}(%)")
                                    else:
                                        print(repr(IMPORT))
                            comfirm = input("YES/NO/EXIT: ").strip().upper()
                            if comfirm == "YES" :
                                with open("../data/Discount.txt", "a", encoding="UTF-8") as files:
                                    files.writelines(IMPORT)
                                print("SAVED")
                                break
                            elif comfirm == "NO" :
                                print(f"1. Type again \n2. Exit")
                                comfirm_2 = int(input("PLEASE Enter the num: "))
                                if comfirm_2 == 1:
                                    continue
                                elif comfirm_2 == 2:
                                    break
                                else:
                                    print("Invalid") # test
                            elif comfirm == "EXIT":
                                break
                            else:
                                print("Sorry Invalid")
                                break

                    except:
                        print("File Error")
                        print("SORRY\n\n")
                        pass

                elif choices == "TYPE":
                    while True:
                        new_item = input("Enter new items (if done type' done'): ")
                        if new_item.upper() == "DONE":
                            break
                        else:
                            new_discount = float(input("Pls enter the discount ( like: 10 is 10%) if no discount enter '0' "))
                            new_file_1.append(f"{new_item}={new_discount}\n")
                    with open("../data/Discount.txt", "a", encoding="UTF-8") as file:
                        file.writelines(new_file_1)
                    print("Item\t\tDiscount")
                    for display in new_file_1:
                        display_clear = display.strip().split("=")
                        if len(display_clear) == 2:
                            display_item = display_clear[0]
                            display_discount = display_clear[1]
                            print(f"{display_item:<11} {display_discount}(%)")
                    print(f"\nHAVE BEEN SAVED")
                    break
            # second
            elif choose == "2":
                while True: # if user had completed deleted the item , it will automatically jump to the main page
                    delete = input("Enter the item you want to DELETE: ").strip().upper()
                    new_item_1 = []  # for修改的部分，之后会把剩下的保存进去，要删掉的就不会写进去 #我要把数据存在这里是因为可以一句直接 存进去，不必一个一个填
                    found  = False
                    for delete_item in file_1:
                        Name = delete_item.strip().split("=")  # ["burger " , " 100"]
                        if Name[0].upper().strip() != delete:  # 确保file 的item 跟 我之前要改的东西匹配 ##记录“找到了”，用于后面是否新增## 加strip 是防止burger后面有个空格
                            new_item_1.append(delete_item) #写name 可以吗？？
                        else:
                            found = True # 然后找到了 然后？ # 只是确保之后的程序而已，电脑不会那么聪明 自动停止
                    with open("../data/Discount.txt", "w", encoding="UTF-8") as file:
                        file.writelines(new_item_1)
                    if found: # only use to judge is it "True" or "False" #Found True 告诉程序：“我找到用户要删的那一行了”。
#然后你就可以决定：是否要重新写入文件、是否要显示提示语句等。
                        print(f"{delete} has been Deleted !")
                        break
                    else:
                        print(f"{delete} Not found in the file")
                        break
                #删除其实是「保留不是目标的数据」在 Python 里，我们不能直接删除文件中的某一行，所以：删除的原理其实是：把不需要删除的内容“重新写入”文件，这样就“间接地”删掉了我们不想要的那一行！

        except :
            print("Pls try again: ")

discount()