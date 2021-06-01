basket = [ ]
print("=" * 40)
while True:
    fruit = input("Fruit name: ")
    print("""              Menu of basket
          [1] = Add Fruit
          [2] = Remove Fruit """)
    option = int(input("Chose Option: "))

    if option == 1:
        basket.append(fruit)
    elif option == 2:
        if fruit in basket:
            basket.remove(fruit)
        else:
            print("This fruit not exist in your basket")
    else:
        input("Invalid option. Press Enter key to continue... ")
    print("=" * 40)
    print("### Fruit Basket ###")
    print("=" * 40)
    print(basket)
    print("=" * 40)
    print("Press enter to add more")
    print("=" * 40)