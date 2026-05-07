def sales():
    total_price = 0
    count = 0
    count_items = {}  # dict
    try:
        with open("./Sales_Reports/sale_reports.txt", "r", encoding="UTF-8") as sales_record_file:
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
        # key= is a parameter （参数） inside sorted. x represents (key, value), and x[1] selects the value part. This is used for dictionaries.
        # .items() converts a dictionary into a list of (key, value) pairs: [(key, value), (key, value)]
        # For list, it's like (name, quantity)
        # reverse=True means sorting （排序） from largest to smallest. If not specified, reverse is False by default, which means smallest to largest.
        Adjust_1 = f"{item_name:<25}{total_count}"
        print(Adjust_1.center(145))
    try:
        while True:
            Exit = int(input("Back to home page press '1':"))
            if Exit == 1:
                print("Back to home page...")
                # Cashier()
                break
            else:
                print("Typing Error, Try again")
                continue
    except:
        print("Error")

sales()