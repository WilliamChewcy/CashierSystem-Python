def Receipts():
    contain = []
    Total = 0.0
    # while True:
    try:
        while True:
            # user input
            item = input("Enter your item if 'done' type done: ").upper().strip()
            if item == 'DONE':
                break
            quantity = int(input("enter the quantity: "))
            if quantity <= 0:
                print("quantity must be > 0")

            # find the price (Food, Beverage, Dessert)
            price = 0.0 #Initialize the price to 0 in case the product hasn’t been found yet
            found_product = False
            product = "" # Create a string variable to temporarily store the name of the found product.
            # Food
            with open("Food/FOOD menu.txt", "r", encoding="UTF-8") as file:
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
                        print(repr(file))
                        continue
            # Beverage
            if not found_product: # Avoid unintentional overwriting and value being replaced
                with open("Beverage/Beverage menu.txt", "r", encoding="UTF-8") as file:
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
                            print(repr(file))
                            continue
            # Dessert
            if not found_product:# Avoid unintentional overwriting and value being replaced
                with open("Dessert/DESSERT menu.txt", "r", encoding="UTF-8") as file:
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
                            print(repr(file))
                            continue
            if not found_product:
                print("Item not found...")
                continue


            # Once the price is found, apply the discount
            # open discount file
            discount = 0.0
            with open("./Discount/Discount.txt", "r", encoding="UTF-8") as file_2:
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
                        print(repr(file_2))
                        continue
            # Calculation (Original price, The price after deducted discount, Subtotal, Final Total Price)
            Final_Price = price * (1 - (discount / 100))
            print(f'your item {product} price will be {Final_Price}')
            Amount = Final_Price * quantity
            Total = Total + Amount

            # Save this to the sales report (for future sales history tracking)
            with open("./Sales_Reports/sale_reports.txt", "a", encoding="UTF-8") as sales_file:
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
                  "\n" + "Cashier by William".center(87))

        # Prevent users messing around
        while True:
            try:
                press = int(input("Press '1' go back to home page: "))
                if press == 1:
                    Cashier()
                    break
                else:
                    continue
            except:
                print('Error')


    # if any issue (fileNotfound) or value mistake , this can avoid system crash
    except Exception as type_Error:
        print("Mistake! Enter again: ", type_Error)

Receipts()