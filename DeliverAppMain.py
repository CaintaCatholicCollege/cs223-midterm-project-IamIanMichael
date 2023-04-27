def computationorder(order1,order2,order3,order4,order5):
    order6 = order1 + order2 + order3 + order4 + order5
    return order6
print("_______________________________________")
print("Welcome to GrabPanda")
print("_______________________________________")
print("type [1] for Jolibee")
print("type [2] for Mcdo")
print("type [3] for Mang Inasal")
print("_______________________________________")
choice = input("What do you want to eat: ")
match choice:
    case "1":
        print("_______________________________________")
        print("\t\tWelcome To JOLIBEE")
        print("\t\t\t\tMenu")
        print("Fried Chicken            | Price 82.00")
        print("Jolly Spaghetti          | Price 50.00")
        print("Yum Burger               | Price 35.00")
        print("Coke Float               | Price 37.00")
        print("Sundae Ice Cream         | Price 55.00")
        print("_______________________________________")
        c1 = int(input("How many Fried Chicken:"))
        c2 = int(input("How many Spaghetti:"))
        c3 = int(input("How many Yum Burger:"))
        c4 = int(input("How many Coke Float:"))
        c5 = int(input("How many Sundae Ice Cream:"))
        #price
        totalc1 = c1 * 82.00
        totalc2 = c2 * 50.00
        totalc3 = c3 * 35.00
        totalc4 = c4 * 37.00
        totalc5 = c5 * 55.00
        order = computationorder(totalc1, totalc2, totalc3, totalc4, totalc5)
        print('Total:', order)
        print("_______________________________________")
    case "2":
        print("_______________________________________")
        print("\t\tWelcome To MCDO!")
        print("\t\t\t\tMenu")
        print("Fried Chicken            | Price 90.00")
        print("MC Chicken Fillet        | Price 76.00")
        print("Chicken Burger           | Price 45.00")
        print("MCFloat                  | Price 43.00")
        print("Hot Fudge Sundae         | Price 43.00")
        print("_______________________________________")
        c1 = int(input("How many Fried Chicken:"))
        c2 = int(input("How many Spaghetti:"))
        c3 = int(input("How many Yum Burger:"))
        c4 = int(input("How many Coke Float:"))
        c5 = int(input("How many Sundae Ice Cream:"))
        print("_______________________________________")
        # price
        totalc1 = c1 * 90.00
        totalc2 = c2 * 76.00
        totalc3 = c3 * 45.00
        totalc4 = c4 * 43.00
        totalc5 = c5 * 43.00
        order = computationorder(totalc1, totalc2, totalc3, totalc4, totalc5)
        print('Total:', order)
        print("_______________________________________")
    case "3":
        print("_______________________________________")
        print("\t\tWelcome To Mang Inasal!")
        print("\t\t\t\tMenu")
        print("Chicken Inasal           | Price 99.00")
        print("Pansit Bihon Solo        | Price 49.00")
        print("Halo - Halo              | Price 39.00")
        print("Pork Sisig               | Price 99.00")
        print("Sagu't Gulaman           | Price 29.00")
        print("_______________________________________")
        c1 = int(input("How many Fried Chicken:"))
        c2 = int(input("How many Spaghetti:"))
        c3 = int(input("How many Yum Burger:"))
        c4 = int(input("How many Coke Float:"))
        c5 = int(input("How many Sundae Ice Cream:"))
        print("_______________________________________")
        # price
        totalc1 = c1 * 99.00
        totalc2 = c2 * 49.00
        totalc3 = c3 * 39.00
        totalc4 = c4 * 99.00
        totalc5 = c5 * 29.00
        order = computationorder(totalc1, totalc2, totalc3, totalc4, totalc5)
        print('Total:', order)
        print("_______________________________________")


