def Product_Display():
    print(f"{" PWP Restaurant Menu:":^{150}}\n")
    try:
        while True:
            print("ITEM\t\t\tUnit Price".center(144))
            print("FOOD".center(150))
            print(f"{("-"*29).center(150)}")
            with open("Food/FOOD menu.txt", "r", encoding="UTF-8") as file_FOOD:
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
            with open("Beverage/Beverage menu.txt", "r", encoding="UTF-8") as file_DRINK:
                DRINK_lines = file_DRINK.readlines()
                for DRINK_line in DRINK_lines:
                    drink = DRINK_line.strip().split("=")
                    if len(drink) == 2:
                        drink_1 = drink[0]
                        price_drink = drink[1]
                        Display_drink = f"{drink_1:<19}RM{price_drink:>8}"# 左对齐
                        print(Display_drink.center(150))
                    else:
                        print(repr(DRINK_line))

            print("\n")
            print("DESSERT".center(150))
            print(f"{("-" * 29).center(150)}")
            with open("Dessert/DESSERT menu.txt", "r", encoding="UTF-8") as file_DESSERT:
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

            click = input("Exit type 1 :").strip()
            if click == "1":
                # Cashier()
                break
            else:
                continue
    except FileNotFoundError:
        print("No This Menu")

Product_Display()