# The first piece of this code is a dictionary to provide the menu options

menuOptions = {
    1: 'One slice of pizza: $22.95',
    2: 'A third of a burger: $15.99',
    3: 'Quit\n\n',
}

# Below are the functions used to calculate the total prices and effects of the discounts and taxes. Also there is a funtion to print  the menu.

def pizzaPrice(pizzaAmount: float):

    return (22.95)*(pizzaAmount)

def burgerPrice(burgerAmount: float):

    return (15.95)*(burgerAmount)

def discountPrice(productTotal: float):

    if productTotal > 100:

        return round((productTotal*0.05), 2)

    elif productTotal < 100 and productTotal > 500:

        return round((productTotal*0.1), 2)

    elif productTotal > 500:

        return round((productTotal*0.15), 2)

def taxEffect(total: float):

    return round(((total)*(0.13)), 2)

def printMenu():

    for option in menuOptions:

        print (option, '--', menuOptions[option] )

# Below are the prompts to store the user information so that a future program could interperit the information and provide it to the store

print('Hello, welcome to Arnolds Amazing Eats\n\nBefore we begin making your delicious meal, we need to know a little about you!\n\n')

name = input('What is your name?: ')

deliveryAddress = input('Please give us your delivery address [Street Number], [Street Name], [Unit # (if applicable)]: ')

city = input('What city do you live in?: ')

province = input('What province do ou live in?: ')

postalCode = input('What is your postal code?: ')

phoneNumber = input('What is your phone number?: ')

specialInstructions = input('Are there any special instructions for this delivery?: ')

print('Thank you for your patience, here is our menu!\n')

# This while loop keeps the program running so that if they have made a mistake they can enter N to loop the program

while True:

    printMenu()

    #This vaiable stores the users item selection

    choiceOne = float(input('Which item would you like?: '))

    #This variable stores the quantity of that item

    quantityOne = float(input('How much of this item would you like?: '))

    if choiceOne == 1:

        print('you have ordered ', quantityOne, 'slices of pizza, is this correct?\n ')

    elif choiceOne == 2:

        print('you have ordered ', quantityOne, 'thirds of a burger, is this correct?')

    # The below input engages the if statements that drive this program. if at this poin the user made a mistake
    # they can enter N to restart the program

    finalize = input('[Y/N]: ')

    if finalize == 'y' or finalize == 'Y':

        student = input('Are you a student? [Y/N]: ')

        pizzaTotal = pizzaPrice(quantityOne)

        burgerTotal = burgerPrice(quantityOne)
        
        print('                      Item     Item    ')
        print('Order                  Amt    Price       Total')
        print('-------------         ----   ------    --------')
        if choiceOne == 1:
            print('Slice of pizza       ', quantityOne, '   ', '22.95', ' ', '$', pizzaTotal)
        
            if student == 'y'or student == 'Y':

                pizzaDiscount = round((pizzaTotal * (0.1)), 2)

                print('10% student savings                   ', '$', pizzaDiscount)

                newPizzaDiscount = discountPrice(pizzaTotal)

                print('                           Discount    $', pizzaDiscount)

                newPizzaTotal = float(round((pizzaTotal - pizzaDiscount - newPizzaDiscount), 2))

                print('                           Sub Total   $', newPizzaTotal)

                studentCustomer = taxEffect(newPizzaTotal)

                print('                            Tax (13%)  $', studentCustomer)

                print('                                        -------')

                customerStudentPizzaTotal = round((newPizzaTotal + studentCustomer), 2)

                print('                                       $', customerStudentPizzaTotal)


            else:

                pizzaTotalDiscount = discountPrice(pizzaTotal)

                print('                           Discount    $', pizzaTotalDiscount)

                newPizzaDiscount = round((pizzaTotal - pizzaTotalDiscount), 2)

                print('                           Sub Total   $', newPizzaDiscount)
                
                nonStudentPizzaCustomer = taxEffect(pizzaTotal)

                print('                           Tax (13%)   $', nonStudentPizzaCustomer)

                print('                                        -------')

                nonStudentCustomerPizzaTotal = pizzaTotal + nonStudentPizzaCustomer

                print('                                       $', nonStudentCustomerPizzaTotal)

        
        elif choiceOne == 2:

            print('Third of a burger    ', quantityOne, ' ', '$15.99','  ', '$', burgerTotal)

            if student == 'y'or student == 'Y':

                burgerDiscount = round((burgerTotal * (0.1)), 2)

                print('10% student savings                   ', '$', burgerDiscount)

                burgerDiscount = discountPrice(burgerTotal)

                print('                           Discount    $', burgerDiscount)

                newBurgerTotal = round((burgerTotal - burgerDiscount - burgerDiscount), 2)

                print('                           Sub Total   $', newBurgerTotal)

                studentBurgerTax = taxEffect(newBurgerTotal)

                print('                           Tax (13%)   $', studentBurgerTax)

                print('                                        -------')

                studentCustomerBurgerTotal = round((newBurgerTotal + studentBurgerTax), 2)

                print('                                       $', studentCustomerBurgerTotal)
            
            else:

                burgerDiscount = discountPrice(burgerTotal)

                print('                           Discount    $', burgerDiscount)

                newBurgerTotal = round((burgerTotal - burgerDiscount), 2)

                print('                           Sub Total   $', newBurgerTotal)

                nonStudent = taxEffect(burgerTotal)

                print('                           Tax (13%)   $', nonStudent)

                print('                                        -------')

                nonStudentCustomerBurgerTotal = round((newBurgerTotal + nonStudent), 2)

                print('                                       $', nonStudentCustomerBurgerTotal)

        break

    elif finalize == 'n' or finalize == 'N':

        continue