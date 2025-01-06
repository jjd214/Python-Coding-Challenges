items = []
prices = []

repeat = True

print("Welcome to the Shopping Cart Program!\n")
while repeat:
    print('\nPlease select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    choice = int(input('\nPlease enter an action: '))
    
    match choice:
        case 1:
            item = input('\nWhat item would you like to add? ').strip().lower()
            price = float(input(f"What is the price of '{item}'? ").strip())
            items.append(item)
            prices.append(price)
            print(f"{item} has been added to the cart.")
        case 2:
            if len(items) > 0:
                print('\nThe contents of the shopping cart are:')
                for i in range(len(items)):
                    print(f"{i+1}. {items[i]} - ${prices[i]}")
            else:
                print("NO ITEMS IN YOUR CART")
        case 3:
            if len(items) > 0:
                index = int(input('\nWhich item would you like to remove? '))
                items.pop(index-1)
                prices.pop(index-1)
                print(f'Item removed from your cart!')
            else:
                print('NO ITEM IN YOUR CART')
        case 4:
            if len(items) > 0:
                total = sum(prices)
                print(f"\nThe total price of the items in the shopping cart is ${total}")
        case 5:
            print('Thank you. Goodbye.')
            repeat = False