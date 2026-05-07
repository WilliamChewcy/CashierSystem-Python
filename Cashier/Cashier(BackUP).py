
def Cashier():
    try:
        while True:
            # import os
            # print("当前运行路径是：", os.getcwd())
            print(f"\n{"Cashier Menu:":^{150}}\n{"1.Product_Display":^{150}}\n{"2.Discount":^{143}}\n{"3.Receipts.txt":^{147}}\n{"4.Sales":^{140}}\n{"5.Exit":^{138}}")
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
    except:
        print("Error")
Cashier()