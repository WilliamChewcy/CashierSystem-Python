
import os
import shutil
customer_cart = []

# --- Login Function (from your previous code) ---
# def login():
#     try:
#         # Assuming login.txt is in a 'FOR_LAB' directory one level up
#         login_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "login.txt") #constructs the path to login.txt assuming it's located in a folder named FOR_LAB
#         if not os.path.exists(login_file_path):
#             print(f"Error: login.txt not found at {login_file_path}") #ensure script will not crash if file is missing
#             return False  # Login fails if file not found
#
#         with open(login_file_path, "r", encoding="UTF-8") as file:
#             login_data = file.readlines() # read all the lines from the file, assuming each line contains one user’s credentials in the format: (username,password)
#
#         count = 0
#         Found = False #ensure the loops exits early if valid credentials entered
#         while count < 3: #allow the user up to 3 attempts
#             user = input("Enter User Name: ").strip() #for user to input username
#             password = input("Enter Password: ").strip() #for user to input password
#             for login_entry in login_data:  # Renamed 'login' to 'login_entry' to avoid shadowing function name
#                 name_pass = login_entry.strip().split(",")
#                 if len(name_pass) == 2:
#                     user_name = name_pass[0].strip()
#                     user_password = name_pass[1].strip()
#
#                     if user_name == user and user_password == password:
#                         Found = True #compare if input matches the text file.
#                         break #This break is used for stop looking for username and password from the file
#             if Found:
#                 break
#             else:
#                 count += 1  #This is for unsucesful of looking for the matching username and password
#                 print("Try Again".center(150))
#
#         if Found:
#             print(f"{"Login Successfully":^{150}}\n{("-" * 25).center(150)}\n{"Welcome to PWP Restaurant":^{150}}")
#             return True  # Login successful
#         else:
#             print("Login Failed".center(150))
#             return False  # Login failed
#
#     except Exception as error:
#         print("An error occurred during login:", error)
#         return False


# --- Helper function to load menu items ---
def load_menu_items(filename):
    items = {}  # Dictionary to store items: {"Item Name": price}
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename) #get the folder containing (__file__)script
        if not os.path.exists(file_path):
            print(f"Warning: {filename} not found at {file_path}")
            return items  # Return empty if file not found

        with open(file_path, "r", encoding="UTF-8") as file:
            for line in file: #read line from file and the len is only allowed to be 2
                parts = line.strip().split("=")
                if len(parts) == 2:
                    name = parts[0].strip()
                    try:
                        price = float(parts[1].strip())
                        items[name] = price
                    except ValueError:
                        print(f"Warning: Invalid price format for '{name}' in {filename}. Skipping.")
                else:
                    print(f"Warning: Invalid line format in {filename}: {repr(line.strip())}. Skipping.")
    except Exception as e:
        print(f"An error occurred while loading {filename}: {e}")
    return items


# --- Global menu data (loaded once) ---
# This will store all available items with their prices for quick lookup
all_menu_items = {}
all_menu_items.update(load_menu_items("data/FOOD menu.txt"))
all_menu_items.update(load_menu_items("data/Beverage menu.txt"))
all_menu_items.update(load_menu_items("data/DESSERT menu.txt"))
# add those item into (all_menu_item)

# --- Cart Management Functions ---

def display_cart():
    """Displays the current items in the customer's cart."""
    print("\n" + "=" * 40)
    print("           YOUR SHOPPING CART         ") #Prints a title for the cart
    print("=" * 40)
    if not customer_cart:
        print("Your cart is empty.")
    else:
        total_price = 0 #total price is intialized to 0 to calculate the final amount
        print(f"{'Item':<25}{'Qty':>5}{'Price':>8}")
        print("-" * 40)
        for i, item in enumerate(customer_cart):
            item_total = item['price'] * item['quantity']
            total_price += item_total
            print(f"{i + 1}. {item['name']:<26}{item['quantity']:<4}RM{item_total:>5.2f}") #loops through each item in the cart, add item_total to the running total_price
        print("-" * 40)
        print(f"{'Total:':<30}RM{total_price:>7.2f}")
    print("=" * 40)


def add_to_cart_prompt():
    """Prompts the user to add an item to the cart."""

    while True:
        item_name = input("\nEnter item name to add (or 'cancel' to return): ").strip().lower()
        if item_name.lower() == 'cancel':
            return
    #
    #     while True:
    #         quantity_number = input("enter the quantity: ")
    #         try:
    #             quantity = int(quantity_number) # avoid users type the wrong number or alphabet
    #             if quantity <= 0:
    #                 print("quantity must be > 0")
    #                 continue # avoid users typed '0' still can continue run the program.
    #             else:
    #                 break
    #         except Exception as error:
    #             print(error)
    #
    #
    #     # find the price (Food, Beverage, Dessert)
    #     price = 0.0  # Initialize the price to 0 in case the product hasn’t been found yet
    #     found_product = False
    #     product = ""  # Create a string variable to temporarily store the name of the found product.
    #     # Food
    #     with open("data/FOOD menu.txt", "r", encoding="UTF-8") as file:
    #         for receipts in file:
    #             name = receipts.strip().split("=")
    #             if len(name) == 2:
    #                 product = name[0].strip()
    #                 price_file = name[1].strip()
    #                 if item_name == product.lower():
    #                     price = float(price_file)
    #                     print(f'{product},{price}')
    #                     found_product = True
    #                     break
    #             else:
    #                 print(repr(receipts))
    #                 continue
    #     # Beverage
    #     if not found_product:  # Avoid unintentional overwriting and value being replaced
    #         with open("data/Beverage menu.txt", "r", encoding="UTF-8") as file:
    #             for receipts in file:
    #                 name = receipts.strip().split("=")
    #                 if len(name) == 2:
    #                     product = name[0].strip()
    #                     price_file = name[1].strip()
    #                     if item_name == product.lower():
    #                         price = float(price_file)
    #                         print(f'{product},{price}')
    #                         found_product = True
    #                         break
    #                 else:
    #                     print(repr(receipts))
    #                     continue
    #     # Dessert
    #     if not found_product:  # Avoid unintentional overwriting and value being replaced
    #         with open("data/DESSERT menu.txt", "r", encoding="UTF-8") as file:
    #             for receipts in file:
    #                 name = receipts.strip().split("=")
    #                 if len(name) == 2:
    #                     product = name[0].strip()
    #                     price_file = name[1].strip()
    #                     if item_name == product.lower():
    #                         price = float(price_file)
    #                         print(f'{product},{price}')
    #                         found_product = True
    #                         break
    #                 else:
    #                     print(repr(receipts))
    #                     continue
    #     if not found_product:
    #         print("Item not found...")
    #         continue
    #
    #     discount = 0.0
    #     with open("data/Discount.txt", "r", encoding="UTF-8") as file_2:
    #         for count in file_2:
    #             discount_item = count.strip().split("=")
    #             if len(discount_item) == 2:
    #                 product_1 = discount_item[0].strip().upper()
    #                 discount_str = discount_item[1].strip()
    #                 if item_name.upper().strip() == product_1.upper().strip():
    #                     discount = float(discount_str)
    #                     print("discount")
    #                     break
    #             else:
    #                 print(repr(count))
    #                 continue
    #     # Calculation (Original price, The price after deducted discount, Subtotal, Final Total Price)
    #     Final_Price = price * (1 - (discount / 100))
    #     print(f'your item {product} price will be {Final_Price}')
    #
    #     for item in customer_cart:
    #         if item['name'].lower() == product.lower():
    #             item['quantity'] += quantity
    #             # print(f"✅ {product} already in cart. Updated quantity to {item['quantity']}")
    #             return
    #     # Save this to the sales report (for future sales history tracking)
    #     # with open("data/to_receipt menu.txt", "a", encoding="UTF-8") as sales_file:
    #     #     for count in range(quantity):
    #     #         sales_file.write(f"{product},{Final_Price:.2f}\n")
    #     with open("data/to_receipt menu.txt", "a", encoding="UTF-8") as sales_file:
    #         sales_file.write(f"{product},{quantity}\n")
    #     print("Saved !")
    #     customer_cart.append(
    #         {"name": product, "quantity": quantity, "price": Final_Price})
    #     print("✅ Current cart:", customer_cart)

        # Normalize item name for lookup
        found_item = None
        # with open
        for name, price in all_menu_items.items():
            if name.lower() == item_name.lower():
                found_item = {"name": name, "price": price}
                break

        if found_item:
            while True:
                try:
                    quantity = int(input(f"Enter quantity for {found_item['name']}: "))
                    if quantity <= 0:
                        print("Quantity must be a positive number.")
                    else:
                        # Check if item already exists in cart, then update quantity
                        item_in_cart = False
                        for item in customer_cart:
                            if item['name'].lower() == found_item['name'].lower():
                                item['quantity'] += quantity #adds the new quantity to the exist one
                                item_in_cart = True #to let us know it is updated
                                print(f"Added {quantity} to existing {found_item['name']} in cart.")
                                break
                        if not item_in_cart:
                            customer_cart.append({
                                "name": found_item['name'],
                                "price": found_item['price'],
                                "quantity": quantity #appends a new dictionary with item details
                            })
                            print(f"{quantity} x {found_item['name']} added to cart.")

                        else:
                            # If pre-existing, update the old quantity in the file (requires rewriting the entire file)
                            temp_lines = []
                            updated = False
                            with open("data/to_receipt menu.txt", "r", encoding="UTF-8") as file:
                                for line in file:
                                    name_qty = line.strip().split(",")
                                    if len(name_qty) == 2 and name_qty[0].strip().lower() == found_item['name'].lower():
                                        old_quantity = int(name_qty[1].strip())
                                        new_qty = old_quantity + quantity
                                        temp_lines.append(f"{found_item['name']},{new_qty}\n")
                                        updated = True
                                    else:
                                        temp_lines.append(line)

                            if updated:
                                with open("data/to_receipt menu.txt", "w", encoding="UTF-8") as file:
                                    file.writelines(temp_lines)

                        if not item_in_cart:
                            # If it's a new addition, just write it in #
                            with open("data/to_receipt menu.txt", "a", encoding="UTF-8") as file:
                                file.write(f"{found_item['name']},{quantity}\n")

                        return  # Exit after successful addition
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
        else:
            print(f"'{item_name}' not found in menu. Please check spelling.")

# def remove_from_cart_prompt():
#     item_to_remove =input("Item want to Remove:").strip().upper()
#     temp_lines = []
#
#     try:
#         # 读取所有不包含目标商品的行
#         with open("data/to_receipt menu.txt", "r", encoding="UTF-8") as file:
#             for line in file:
#                 line_tiny = line.strip().split(",")
#                 name = line_tiny[0].strip().upper()
#                 # price = line_tiny[1].strip().upper()
#                 if name != item_to_remove:
#                     temp_lines.append(line)
#                 else:
#                     continue
#
#         # 写回不包含该商品的内容
#         with open("data/to_receipt menu.txt", "w", encoding="UTF-8") as file:
#             file.writelines(temp_lines)
#
#         global customer_cart
#         customer_cart[:] = [item for item in customer_cart if item['name'].upper() != item_to_remove] #####
#
#         print(f"✅ All '{item_to_remove}' items have been removed from the file.")
#     except FileNotFoundError:
#         print("❌ File not found.")
#     except Exception as error:
#         print(f"❌ Error: {error}")

def remove_from_cart_prompt():
    """Prompts the user to remove an item from the cart."""
    if not customer_cart:
        print("Your cart is empty. Nothing to remove.")
        return

    display_cart()
    while True:
        try:
            item_index = input("Enter the number of the item to remove (or 'cancel'): ").strip()
            if item_index.lower() == 'cancel':
                return

            index = int(item_index) - 1
            if 0 <= index < len(customer_cart):
                removed_item = customer_cart.pop(index) #pop is to remove and return an item from a list #the(index) is for specified position
                print(f"'{removed_item['name']}' removed from cart.")

                # Now remove from the file
                updated_lines = []
                try:
                    with open("data/to_receipt menu.txt", "r", encoding="UTF-8") as file:
                        for line in file:
                            parts = line.strip().split(",")
                            if len(parts) == 2:
                                item_name = parts[0].strip().lower()
                                if item_name.lower() != removed_item['name'].strip().lower():
                                    updated_lines.append(line)
                    with open("data/to_receipt menu.txt", "w", encoding="UTF-8") as file:
                        file.writelines(updated_lines)

                    print(f"'{removed_item['name']}' also removed from file.")
                except FileNotFoundError:
                    print("File not found")

                break
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'cancel'.")

# def modify_cart_item_prompt():
#     global customer_cart
#     temp_lines = []
#     found = False
#     modify_item = input("Enter your previous item:").strip().upper()
#     try:
#         with open("data/to_receipt menu.txt", "r", encoding="UTF-8") as file:
#             for line in file:
#                 parts = line.strip().split(",")
#                 if len(parts) == 2:
#                     name = parts[0].strip().upper()
#                     quantity = parts[1].strip()
#                     if name == modify_item.upper():
#                         found = True
#                         print(f"Make sure your item:{name} \nThe Quantity:{quantity}\n")
#                         new_items = input("Enter your new items:").strip().upper()
#                         while True:
#                             try:
#                                 quantity = int(input("Enter item quantity:").strip())
#                                 if quantity < 0:
#                                     print("Invalid Value,Please enter again")
#                                     continue
#                                 else:
#                                     break
#                             except Exception as error:
#                                 print(error)
#                         print(f"{new_items},{quantity}")
#                         temp_lines.append(f"{new_items},{quantity}\n")
#                         break
#
#                     else:
#                         temp_lines.append(line)
#                 else:
#                     temp_lines.append(line)
#         if not found:
#             print("Item not found, no changes made.")
#             return
#
#             # 安全写入：先备份，再写文件
#         shutil.copy("data/to_receipt menu.txt", "data/to_receipt_backup menu.txt") # copy the data in the file, to the backup file
#         with open("data/to_receipt menu.txt", "w", encoding="UTF-8") as file:
#             file.writelines(temp_lines)
#         print("Item modified successfully.")
#
#         for item in customer_cart:
#             if item['name'].upper() == modify_item.upper():
#                 item['name'] = new_items # change the item's name from (customer_cart's container)
#                 item['quantity'] = quantity
#                 item['price'] = float(all_menu_items.get(new_items, item['price']))
#                 print(f"Modified {modify_item} to {new_items}, Quantity {quantity}")
#                 return
#
#     except Exception as error:
#         print("Error occurred:", error)



def modify_cart_item_prompt():
    """Prompts the user to modify the quantity of an item in the cart."""
    if not customer_cart:
        print("Your cart is empty. Nothing to modify.")
        return

    display_cart()
    while True:
        try:
            item_index = input("Enter the number of the item to modify (or 'cancel'): ").strip()
            if item_index.lower() == 'cancel':
                return #converts the index into an interger #validates the index within its range #let user input new quantity #update cart

            index = int(item_index) - 1
            if 0 <= index < len(customer_cart):
                item_to_modify = customer_cart[index]
                while True:
                    try:
                        new_quantity = int(input(
                            f"Enter new quantity for {item_to_modify['name']} (current: {item_to_modify['quantity']}): "))
                        if new_quantity <= 0:
                            print("Quantity must be a positive number. If you want to remove, use the 'remove' option.")
                        else:
                            item_to_modify['quantity'] = new_quantity
                            print(f"Quantity of '{item_to_modify['name']}' updated to {new_quantity}.")

                            updated_lines = []
                            item_name_upper = item_to_modify['name'].strip().upper()

                            with open("data/to_receipt menu.txt", "r", encoding="UTF-8") as file:
                                for line in file:
                                    parts = line.strip().split(",")
                                    if len(parts) == 2:
                                        name = parts[0].strip().upper()
                                        if name == item_name_upper:
                                            updated_lines.append(f"{item_to_modify['name']},{new_quantity}\n")
                                        else:
                                            updated_lines.append(line)
                                    else:
                                        updated_lines.append(line)

                            with open("data/to_receipt menu.txt", "w", encoding="UTF-8") as file:
                                file.writelines(updated_lines)

                            print("File updated successfully.")
                            return  # Exit after successful modification
                    except ValueError:
                        print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'cancel'.")


def cart_management_menu():
    """Presents cart management options to the user."""
    while True:
        display_cart()
        print("\n--- Cart Options ---")
        print("1. Add items (back to menu)")
        print("2. Remove item")
        print("3. Modify item quantity")
        print("4. Proceed to Checkout (Not implemented yet)")
        print("5. Back to Main Menu")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            menu()  # Go back to the main menu to add items
        elif choice == '2':
            remove_from_cart_prompt()
        elif choice == '3':
            modify_cart_item_prompt()
        elif choice == '4':
            print("Proceeding to checkout... (Functionality to be added)")
            # Here you would typically lead to payment, delivery details etc.
            break  # Exit cart management after 'checkout'
        elif choice == '5':
            break  # Exit cart management to go back to the main application flow
        elif choice == '6':
            print("Exiting PWP Restaurant. Goodbye!")
            exit()  # Terminate the program
        else:
            print("Invalid choice. Please try again.")


# --- Menu Display Function ---
def display_menu_category(filename, category_name, line_length=30):
    """
    Helper function to display items from a specific menu category file.
    """
    print(f"\n{category_name.upper()}")
    print("-" * line_length)
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(file_path):
            print(f"Warning: {filename} not found at {file_path}")
            return  # Skip displaying this category if file not found

        with open(file_path, "r", encoding="UTF-8") as file:
            for line in file:
                items = line.strip().split("=")
                if len(items) == 2:
                    name, price = items[0].strip(), items[1].strip()
                    try:
                        # Attempt to convert price to float to catch invalid prices
                        _ = float(price)
                        print(f"{name:<19}RM{price:>8}")
                    except ValueError:
                        print(f"Invalid price format for '{name}': {price}")
                else:
                    print(f"Invalid line format in {filename}: {repr(line.strip())}")
    except Exception as e:
        print(f"An unexpected error occurred while reading {filename}: {e}")


def menu():
    """
    Displays the PWP Restaurant menu from text files and allows adding items to cart.
    """
    while True:  # Loop to allow user to add multiple items or go to cart
        print("\n" + "=" * 40)
        print("           PWP RESTAURANT MENU        ")
        print("=" * 40)

        # Display categories using the helper function
        display_menu_category("data/FOOD menu.txt", "FOOD", 35)
        display_menu_category("data/Beverage menu.txt", "DRINK", 30)
        display_menu_category("data/DESSERT menu.txt", "DESSERT", 29)

        print("\n--- Menu Options ---")
        print("1. Add item to cart")
        print("2. View/Manage Cart")
        print("3. Back to Main Menu")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_to_cart_prompt()
        elif choice == '2':
            cart_management_menu()
        elif choice == '3':
            break  # Exit menu loop to go back to main application flow
        elif choice == '4':
            print("Exiting PWP Restaurant. Goodbye!")
            exit()  # Terminate the program
        else:
            print("Invalid choice. Please try again.")


# --- Main Application Flow ---
def main_app():
    """The main entry point for the PWP Restaurant application."""
    # if login():
    while True:
        print("\n--- Main Menu ---")
        print("1. Browse Menu")
        print("2. View/Manage Cart")
        print("3. Exit")
        main_choice = input("Enter your choice: ").strip()

        if main_choice == '1':
            menu()
            # break
        elif main_choice == '2':
            cart_management_menu()
            # break
        elif main_choice == '3':
            print("Thank you for visiting PWP Restaurant!")
            break  # Exit the main application loop
        else:
            print("Invalid choice. Please try again.")
    # else:
    #     print("Login failed. Exiting application.")


if __name__ == "__main__":


    main_app()
