def Discount():
    new_file_1 =[]
    try:
        while True: # Ensure the user doesn't input incorrectly
            #main
            with open("Discount/Discount.txt", "r", encoding="UTF-8") as file:
                file_1 = file.readlines()
                print(("-"*40).center(150))
                print("Item\t\tDiscount".center(145))
                for file1 in file_1:
                    Discount = file1.strip().split("=")
                    if len(Discount) == 2:
                        item     = Discount[0].strip()
                        discount = Discount[1].strip()
                        Adjust = f"{item:<14}{discount:>4}{"(%)":>2}"
                        print(Adjust.center(148))
                    else:
                        print(repr(file1))
            print(("-"*40).center(150))
            print("SELECT:".center(117))
            print(f"\n{"1. ADD":^{128}}\n{"2. DELETE":^{132}}\n{"3. MODIFY":^{132}}\n{"4. EXIT":^{130}}\n")
            choose = input("PLEASE Enter the number (only number):").strip()
            # start first
            if choose == "1":
                choices = input("File or Type: ").strip().upper()
                if choices == "FILE":
                    try:
                        while True:
                    # try:
                            choose_file = input("Which file you want to import (DON'T SPACE): ").strip()
                            if not choose_file.endswith(".txt"):
                                choose_file = choose_file + ".txt" # if users didn't add .txt , we add for them
                                which_file = os.path.join("./IMPORT_FILE/",choose_file)# Combine the full file path so that can be reading data from the file later
                            else:
                                which_file = os.path.join("./IMPORT_FILE/",choose_file) # if user have added '.txt' ,then we combine full file directly

                            with open(which_file, "r", encoding="UTF-8") as import_file: # read the data from the file that user given
                                IMPORT = import_file.readlines()
                                print("\n",("-" * 40).center(150))
                                print("Item\t\t\tDiscount".center(145))
                                for show_import in IMPORT:
                                    show = show_import.strip().split("=")
                                    if len(show) == 2:
                                        import_item = show[0]
                                        import_discount =  show[1]
                                        Adjust_1 = f"{import_item:<17}{import_discount:>4}{"(%)":>3}"
                                        print(Adjust_1.center(152))

                                    else:
                                        print(repr(IMPORT))
                            print("\n", ("-" * 40).center(150))
                            comfirm = input("YES/NO/EXIT: ").strip().upper()
                            if comfirm == "YES" :
                                with open("Discount/Discount.txt", "a", encoding="UTF-8") as files:
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
                    with open("Discount/Discount.txt", "a", encoding="UTF-8") as file:
                        file.writelines(new_file_1)
                    print("\n","Item\t\tDiscount")
                    for display in new_file_1:
                        display_clear = display.strip().split("=")
                        if len(display_clear) == 2:
                            display_item = display_clear[0]
                            display_discount = display_clear[1]
                            print(f"{display_item:<11} {display_discount}(%)")
                    print(f"\nHAVE BEEN SAVED!")
                    break
            # second
            elif choose == "2":
                while True: # if user had completed deleted the item , it will automatically jump to the main page
                    delete = input("Enter the item you want to DELETE: ").strip().upper()
                    new_item_1 = []  # For modified parts, the remaining 剩下的 data will be saved later; deleted parts simply won't be written back
                                     # Data is stored here for convenience — allows storing everything in one go instead of line by line
                    found  = False
                    for delete_item in file_1:
                        Name = delete_item.strip().split("=")  # ["burger " , " 100"]
                        if Name[0].upper().strip() != delete:  # Skip unrelated data and continue when a match is found
                                                               # Add `.strip()` to prevent trailing spaces (e.g., after 'burger ')
                            new_item_1.append(delete_item) #写name 可以吗？？
                        else:
                            found = True
                    with open("Discount/Discount.txt", "w", encoding="UTF-8") as file:
                        file.writelines(new_item_1)
                    if found: # only use to judge is it "True" or "False"
                        print(f"{delete} has been Deleted !")
                        break # If found, show a message that the item has been deleted
                    else:
                        print(f"{delete} Not found in the file")
                        break # If not found, show a message that the item doesn't exist
                              # Deletion is actually "keeping only the data you don’t want to delete"
                              # In Python, we can’t directly delete a specific line from a file, so:
                              # The idea of deletion is: rewrite only the lines we want to keep into the file,
                              # which indirectly removes the line we don’t want
            # Third
            elif choose == "3":
                while True:
                    new_file_modify = []
                    found = False
                    item_modify = input("Which item's discount you want to edit: ").strip().upper()
                    print("Item\t\tDiscount")

                    for modify_file in file_1:
                        modify_Edit = modify_file.strip().split("=")
                        if len(modify_Edit) == 2:
                            item_Original = modify_Edit[0].strip()
                            discount_Original = modify_Edit[1].strip()
                            # print(f"{item_Original:<12}{discount_Original}(%)")  #

                            if item_modify == item_Original.upper():
                                found = True
                                print(f"{item_Original:<12}{discount_Original}(%)")
                                print(f"Your Original item is: {item_Original}")
                                item_discount = float(input( "Pls enter your discount (like: 10 is 10%) if no discount enter '0' ): "))

                                print(f"{item_Original:<12}{item_discount}(%)")
                                new_file_modify.append(f"{item_Original}={item_discount}\n")
                            else:
                                new_file_modify.append(modify_file)  # Without this line, the entire contents of the file will be lost
                                                                     # Why not use `modify_Edit`? Because we want to write back the original unedited line
                                                                     # like "Popo=122\n", including the newline character and other formatting
                    # end for
                    # main
                    if found:  # （为什么不是for循环里面）显示全部你要更改的东西，一次过问你是不是你要更改的数据# 把 for 想象成一个检查文件的“筛子”——它把每行读一读、筛一筛，放进新篮子（new_file_modify）里。而 if found: 是你“检查完所有文件”之后，才来决定：
                        comfirm_modify = input("YES/NO: ").upper().strip()
                        if comfirm_modify == "YES":
                            with open("Discount/Discount.txt", "w", encoding="UTF-8") as NEW_DISCOUNT:
                                NEW_DISCOUNT.writelines(new_file_modify)
                            print("SEVED")
                            break
                        elif comfirm_modify == "NO":
                            print("TRY AGAIN")
                            continue
                    else:  # NOT found
                        print("This Item Not Found In File, Try Again")
                        break
                    # Just like deletion, we can't directly modify a specific line in a file, so instead:
                    # We rewrite the entire file content, but replace the "line to be modified" 要修改的那一行with the new value
            elif choose == '4':
                print('Exit to the home page...')
                break

    except Exception as Error :
        print("Pls try again: ",Error)

Discount()