import shutil

columns = shutil.get_terminal_size().columns
import os


def Product_Display():
    print(f"{" PWP Restaurant Menu:":^{150}}\n")
    try:
        while True:
            print("ITEM\t\t\tUnit Price".center(146))
            print("FOOD".center(150))
            print(f"{("-"*29).center(150)}")
            with open("data/FOOD menu.txt", "r", encoding="UTF-8") as file_FOOD:
                FOOD_lines = file_FOOD.readlines()
                for FOOD_line in FOOD_lines:
                    food = FOOD_line.strip().split("=")
                    if len(food) == 2:
                        food_1 = food[0]
                        price_food = food[1]
                        Display = f"{food_1:<19}RM{price_food:>8}"
                        print(Display.center(150))
                    else:
                        print(repr(FOOD_line))  # Show file errors (e.g., blank lines) directly to the programmer
            print("\n")
            print("DRINK".center(150))
            print(f"{("-" * 30).center(150)}")
            with open("data/Beverage menu.txt", "r", encoding="UTF-8") as file_DRINK:
                DRINK_lines = file_DRINK.readlines()
                for DRINK_line in DRINK_lines:
                    drink = DRINK_line.strip().split("=")
                    if len(drink) == 2:
                        drink_1 = drink[0]
                        price_drink = drink[1]
                        Display_drink = f"{drink_1:<19}RM{price_drink:>8}"#
                        print(Display_drink.center(150))
                    else:
                        print(repr(DRINK_line))

            print("\n")
            print("DESSERT".center(150))
            print(f"{("-" * 29).center(150)}")
            with open("data/DESSERT menu.txt", "r", encoding="UTF-8") as file_DESSERT:
                DESSERT_lines = file_DESSERT.readlines()
                for DESSERT_line in DESSERT_lines:
                    dessert = DESSERT_line.strip().split("=")
                    if len(dessert) == 2:
                        dessert_1 = dessert[0]
                        price_dessert = dessert[1]
                        Display_dessert = f"{dessert_1:<19}RM{price_dessert:>8}"# 左对齐
                        print(Display_dessert.center(150))
                    else:
                        print(repr(DESSERT_line))
            print("\n")
            print("HERE IS THE MENU")

            break


        while True:
            try:
                click = input("Exit type 1 :").strip()
                if click == "1":
                    Cashier()
                    break
                else:
                    continue
            except Exception as Error:
                    print(Error)
    except FileNotFoundError:
        print("No This Menu")





def Receipts(): # 要跟customer system 做连接
    contain = [] # if using dict, So if the user enters the same product name multiple times (e.g., “BURGER”), the second entry will overwrite the first one.
    Total = 0.0
    # while True:
    try:
        # user input
        with open("data/to_receipt menu.txt", 'r', encoding="UTF-8") as file_from_customerOrder:
            for CustomerOrder in file_from_customerOrder:
                Customer_Order = CustomerOrder.strip().split(",")
                if len(Customer_Order) == 2:
                    item = Customer_Order[0].strip().upper()
                    quantity = int(Customer_Order[1].strip())
                else:
                    continue

            # item = input("Enter your item if 'done' type done: ").upper().strip()
            # if item == 'DONE':
            #     break
            #
            # while True: # if user made any mistake like: type 1+ or alphabet , i will ask users again
            #     quantity_number = input("enter the quantity: ")
            #     try:
            #         quantity = int(quantity_number) # avoid users type the wrong number or alphabet
            #         if quantity <= 0:
            #             print("quantity must be > 0")
            #             continue # avoid users typed '0' still can continue run the program.
            #         else:
            #             break

            # find the price (Food, Beverage, Dessert)
                price = 0.0 #Initialize the price to 0 in case the product hasn’t been found yet
                found_product = False
                product = "" # Create a string variable to temporarily store the name of the found product.
                # Food
                with open("data/FOOD menu.txt", "r", encoding="UTF-8") as file:
                    for receipts in file:
                        name = receipts.strip().split("=")
                        if len(name) == 2:
                            product = name[0].strip()
                            price_file = name[1].strip()
                            if item == product.upper():
                                price = float(price_file)
                                print(f'{product},{price}')
                                found_product = True
                                break
                        else:
                            print(repr(receipts))
                            continue
                # Beverage
                if not found_product: # Avoid unintentional overwriting and value being replaced
                    with open("data/Beverage menu.txt", "r", encoding="UTF-8") as file:
                        for receipts in file:
                            name = receipts.strip().split("=")
                            if len(name) == 2:
                                product = name[0].strip()
                                price_file = name[1].strip()
                                if item == product.upper():
                                    price = float(price_file)
                                    print(f'{product},{price}')
                                    found_product = True
                                    break
                            else:
                                print(repr(receipts))
                                continue
                # Dessert
                if not found_product:# Avoid unintentional overwriting and value being replaced
                    with open("data/DESSERT menu.txt", "r", encoding="UTF-8") as file:
                        for receipts in file:
                            name = receipts.strip().split("=")
                            if len(name) == 2:
                                product = name[0].strip()
                                price_file = name[1].strip()
                                if item == product.upper():
                                    price = float(price_file)
                                    print(f'{product},{price}')
                                    found_product = True
                                    break
                            else:
                                print(repr(receipts))
                                continue
                if not found_product:
                    print("Item not found...")



                # Once the price is found, apply the discount
                # open discount file
                discount = 0.0
                with open("data/Discount.txt", "r", encoding="UTF-8") as file_2:
                    for count in file_2:
                        discount_item = count.strip().split("=")
                        if len(discount_item) == 2:
                            product_1 = discount_item[0].strip().upper()
                            discount_str = discount_item[1].strip()
                            if item.upper().strip() == product_1.upper().strip():
                                discount = float(discount_str)
                                print("discount")
                                break
                        else:
                            print(repr(count))
                            continue
                # Calculation (Original price, The price after deducted discount, Subtotal, Final Total Price)
                Final_Price = price * (1 - (discount / 100))
                print(f'your item {product} price will be {Final_Price}')
                Amount = Final_Price * quantity
                Total = Total + Amount

                # Save this to the sales report (for future sales history tracking)
                with open("data/sale_reports.txt", "a", encoding="UTF-8") as sales_file:
                    for count in range(quantity):
                        sales_file.write(f"{product}={Final_Price:.2f}\n")
                print("Saved !")
                contain.append(
                    {"ITEM": product, "Quantity": quantity, "Discount": discount, "Price": price, "Amount": Amount,
                     "Total": Total})


        # Display Receipt (Combine All The data)
        if contain:
            print(f"\n{('===' * 12 + 'PWP Restaurant' + '===' * 12).center(158)}\n")
            SET = f"{'Item'.center(15)}{'Unit Price'.center(19)}{'Quantity'.center(18)}{'Discount%'.center(16)}{'Subtotal'.center(18)}"
            print(SET.center(158))
            print(("-" * 88).center(158))
            for display in contain:  # Take out each item from the contain list one by one
                item_display = f"{display['ITEM']:<15}"
                price_display = f"RM{display['Price']:<16.2f}"
                quantity_display = f"{display['Quantity']:<16}"
                discount_display = f"{display['Discount']:.0f}%\t"
                discount_display_1 = f"{discount_display:<17}"
                amount_display = f"RM{display['Amount']:.2f}"

                # combine all together then print at once
                combine = item_display + price_display + quantity_display + discount_display_1 + amount_display
                print(combine.center(158))

            print(f"{("-" * 88).center(158)}")
            Total_Price = f"Total Price: RM{Total:.2f}"
            print(Total_Price.center(212))
            print(f"\n{"Thank you for dining with us.".center(100)}" +
                  "\n" + "We hope to see you again!".center(96) +
                  "\n" + f"Cashier by ".center(87))

        # Prevent users messing around
        while True:
            try:
                press = int(input("Press '1' go back to home page: "))
                if press == 1:
                    Cashier()
                    break
                else:
                    continue
            except Exception as Error:
                print(Error)


    # if any issue (fileNotfound) or value mistake , this can avoid system crash
    except Exception as type_Error:
        print("Mistake! Enter again: ", type_Error)



def Discount():
    new_file_1 =[]
    try:
        while True: # Ensure the user doesn't input incorrectly
            #main
            with open("data/Discount.txt", "r", encoding="UTF-8") as file:
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
                                which_file = os.path.join("data/", choose_file)# Combine the full file path so that can be reading data from the file later
                            else:
                                which_file = os.path.join("data/", choose_file) # if user have added '.txt' ,then we combine full file directly

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
                                        print(repr(show_import))
                            print("\n", ("-" * 40).center(150))
                            comfirm = input("YES/NO/EXIT: ").strip().upper()
                            if comfirm == "YES" :
                                with open("data/Discount.txt", "a", encoding="UTF-8") as files:
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
                            elif comfirm == "EXIT": # go back to Discount() main page
                                break
                            else:
                                print("Sorry Invalid")
                                break

                    except Exception as Error:
                        print(Error)
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
                    with open("data/Discount.txt", "a", encoding="UTF-8") as file:
                        file.writelines(new_file_1)
                    print("\n")
                    mid_display1 = "Item\t\tDiscount"
                    print(mid_display1.center(150))
                    for display in new_file_1:
                        display_clear = display.strip().split("=")
                        if len(display_clear) == 2:
                            display_item = display_clear[0]
                            display_discount = display_clear[1]
                            mid_display = f"{display_item:<11} {display_discount}(%)"
                            print(mid_display.center(154))
                    print(f"\nHAVE BEEN SAVED!")
                    break
            # second
            elif choose == "2": # delete the item which inside the Discount's file
                while True: # if user had completed deleted the item , it will automatically jump to the main page
                    delete = input("Enter the item you want to DELETE: ").strip().upper()
                    new_item_1 = []  # For modified parts, the remaining 剩下的 data will be saved later; deleted parts simply won't be written back
                                     # Data is stored here for convenience — allows storing everything in one go instead of line by line
                    found  = False
                    for delete_item in file_1:
                        Name = delete_item.strip().split("=")  # ["burger " , " 100"]
                        if Name[0].upper().strip() != delete:  # Skip unrelated data and continue when a match is found
                                                               # Add `.strip()` to prevent trailing spaces (e.g., after 'burger ')
                            new_item_1.append(delete_item)
                        else:
                            found = True
                    with open("data/Discount.txt", "w", encoding="UTF-8") as file:
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
                    with open("data/Discount.txt", "r", encoding="UTF-8") as file_1:
                        for modify_file in file_1:
                            modify_Edit = modify_file.strip().split("=")
                            if len(modify_Edit) == 2:
                                item_Original = modify_Edit[0].strip()
                                discount_Original = modify_Edit[1].strip()
                                # print(f"{item_Original:<12}{discount_Original}(%)")  #

                                if item_modify.strip() == item_Original.upper().strip():
                                    found = True
                                    print(f"{item_Original:<12}{discount_Original}(%)")
                                    print(f"Your Original item is: {item_Original}")
                                    while True:
                                        try:
                                            item_discount = float(input( "Pls enter your discount (like: 10 is 10%) if no discount enter '0' ): "))
                                            break
                                        except ValueError:
                                            print("Invalid discount value. Please enter a number.")
                                            continue

                                    print(f"{item_Original:<12}{item_discount}(%)")
                                    new_file_modify.append(f"{item_Original}={item_discount}\n")
                                    # break
                                else:
                                    new_file_modify.append(modify_file)  # Without this line, the entire contents of the file will be lost
                                                                         # Why not use `modify_Edit`? Because we want to write back the original unedited line
                                                                         # like "Popo=122\n", including the newline character and other formatting
                    # end for
                    # main
                    if found:
                        comfirm_modify = input("YES/NO: ").upper().strip()
                        if comfirm_modify == "YES":
                            with open("data/Discount.txt", "w", encoding="UTF-8") as NEW_DISCOUNT:
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
                    # We rewrite the entire file content, but replace the "line to be modified" with the new value
            elif choose == '4':
                print('Exit to the home page...')
                break

    except Exception as Error :
        print("Pls try again: ",Error)

def sales():
    total_price = 0
    count = 0
    count_items = {}  # dict
    try:
        with open("data/sale_reports.txt", "r", encoding="UTF-8") as sales_record_file:
            sales_record = sales_record_file.readlines()
            for record in sales_record:
                items, price = record.strip().split("=")
                price = float(price)
                # Calculate the total sales amount
                total_price = total_price + price
                # Calculate the total number of products sold
                count = count + 1
                if items in count_items:
                    count_items[items] += 1
                else:
                    count_items[items] = 1
    except:
        print("File Not Found")
        return

    print("SALES REPORT".center(150))
    print(("-" * 40).center(150))
    print(f"TOTAL SALES: {count}".center(123))
    print(f"TOTAL AMOUNT: RM {total_price:.2f}".center(133))
    print(f"\n")
    print(("-" * 40).center(150))
    print("HOT SAlES".center(150))
    Adjust = f"{"Name":<25}Amount"
    print(Adjust.center(151))
    print(("-" * 40).center(150))
    for item_name, total_count in sorted(count_items.items(), key=lambda x: x[1], reverse=True):
        # .items() converts a dictionary into a list of (key, value) pairs: [(key, value), (key, value)]
        # key= is a parameter inside sorted. x represents (key, value), and x[1] selects the value part. This is used for dictionaries.
        # .items() converts a dictionary into a list of (key, value) pairs: [(key, value), (key, value)]
        # For list, it's like (name, quantity)
        # reverse=True means sorting from largest to smallest. If not specified, reverse is False by default, which means smallest to largest.
        Adjust_1 = f"{item_name:<25}{total_count}"
        print(Adjust_1.center(145))
    try:
        while True:
            Exit = input("Back to home page press '1':").strip()
            if Exit == "1":
                print("Back to home page...")
                Cashier()
                break
            else:
                print("Typing Error, Try again")
                continue
    except Exception as Error:
        print(Error)







# def test():
#     answer = 63
#     number = -1
#     min =1
#     max = 100
#     while(answer != number):
#         sentence = "Please guess a number between"+str(min)+"-"+str(max)
#         number = int(input(sentence))
#
#
# test()



def Cashier():
    try:
        while True:
            print(f"\n{"Cashier Menu:":^{150}}\n{"1.Product_Display":^{150}}\n{"2.Discount":^{143}}\n{"3.Receipts":^{142}}\n{"4.Sales":^{140}}\n{"5.Exit":^{138}}")
            choice = input("Choose: ")
            if choice == "1":
                Product_Display()
            elif choice == "2":
                Discount()
            elif choice == "3":
                Receipts()
            elif choice == "4":
                sales()
            elif choice == "5":
                print(f"Return back to main page{"."*6}\nLOGIN PAGE")
                login()
                break
            else:
                print("Invalid input.".center(150))
    except Exception as Error:
        print(Error)
# Cashier()
def login():
    try:
        with open("data/Login.txt", "r", encoding="UTF-8") as file:
            login_file = file.readlines()
        count = 0
        while count < 3 :
            user = input("Enter User Name: ").strip()
            password = input("Enter Password: ").strip()
            for login in login_file:
                name = login.strip().split("=")
                user_name = name[0].strip()
                user_password = name[1].strip()

                if user_name == user and user_password == password:
                    return True

            count += 1
            print("Try Again".center(150))

        return False
    except:
        print("Error".center(150))
        return False

def Main():
    try:
        while True:
            if login():
                print(f"{"Login Successfully":^{150}}\n{("-"*25).center(150)}\n{"Welcome to PWP Restaurant":^{150}}")
                Cashier()
            else:
                print("Login Failed".center(150))
    except:
        print("Error")

if __name__ == "__main__":
    Main()

