action = input("What action would you like to calculate? 1 = +, 2 = -, 3 = *, 4 = / ")
if action == "1":
    first_number_1 = input('First number: ')
    second_number_1 = input('Added to: ')
    sum = float(first_number_1) + float(second_number_1)
    print('The sum is ' + str(sum))
if action == "2":
    first_number_2 = input('First number: ')
    second_number_2 = input('Subtract: ')
    difference = float(first_number_2) + float(second_number_2)
    print('The difference is ' - str(difference))
if action == "3":
    first_number_3 = input('First number: ')
    second_number_3 = input('Multiplied by: ')
    product = float(first_number_3) * float(second_number_3)
    print('The product is ' + str(product))
if action == "4":
    first_number_4 = input('First number: ')
    second_number_4 = input('Divided by: ')
    dividend = float(first_number_4) / float(second_number_4)
    print('The dividend is ' + str(dividend))
if action > "4":
    for i in range(15):
        print('Invalid Action!')