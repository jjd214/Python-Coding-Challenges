def main():

    print("Welcome to the Shopping Cart Program!")

    play = True
    items = []
    prices = []

    while(play):
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        action = int(input("Please enter an action: "))

        match action:
            case 1:
                item = input("What item would you like to add? ")
                price = int(input(f"What is the price of the {item}"))
                items.append(item)
                prices.append(price)
                print(f"{item} has been added to the cart.")

            case 2:
                if len(items) > 0:
                    for i in range(len(items)):
                        print(f"{i+1}. {items[i]} - ${prices[i]}")
                else:
                    print("No items in cart")

            case 3:
                if len(items) > 0:
                    removeIndex = int(input("Which item would you like to remove? "))
                    del items[removeIndex-1]
                    del prices[removeIndex-1]
                    print("Item removed from your cart!")
                else:
                    print("No items in cart")

            case 4:
                if len(items) > 0:
                    print(f"The total price of the items in the Shopping cart is {sum(prices)}")
                else:
                    print("No items in cart")

            case 5:
                print("Goodbye.")
                play = False

main()
