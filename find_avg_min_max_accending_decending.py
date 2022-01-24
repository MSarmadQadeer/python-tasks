# it will find minimum from list
def find_minimum(list):
    minimum_number = list[0]
    for i in range(1, len(list)):
        if(list[i] < minimum_number):
            minimum_number = list[i]

    return minimum_number


# it will find maximum from list
def find_maximum(list):
    maximum_number = list[0]
    for i in range(1, len(list)):
        if(list[i] > maximum_number):
            maximum_number = list[i]

    return maximum_number


# it will find average
def find_average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)


# it will convert list to accending order
def find_accending_order(list):
    for a in range(len(list)):
        for b in range(len(list)-1):
            if list[b] > list[b+1]:
                list[b], list[b+1] = list[b+1], list[b]


# it will convert list to decending order
def find_decending_order(list):
    for a in range(len(list)):
        for b in range(len(list)-1):
            if list[b] < list[b+1]:
                list[b], list[b+1] = list[b+1], list[b]


condition = "y"
while condition == "y":
    # taking length of list
    list_length = input("\nDear User Kindly Set Your List Length: ")

    # validating the length
    if list_length.isdigit():
        length = eval(list_length)
    else:
        print("\nPlease Enter A Valid Data Type\n")
        continue

    # inserting numbers to list
    list_of_numbers = []
    for i in range(length):
        user_input = input("Enter Any Number: ")
        if user_input.lstrip("+,-").replace(".", "").isdigit():
            list_of_numbers.append(eval(user_input))
        else:
            print("\nEnter A Valid Data Type\n")

    print(list_of_numbers)
    print("\nPress 1 For Finding Average...\nPress 2 For Finding Maximum...\nPress 3 For Finding Minimum...", end="")
    print("\nPress 4 For Finding Accending Order...\nPress 5 For Finding Decending Order...\n")
    check_list = []

    while len(check_list) < 5:
        ask = input("\nEnter Any Number In Range 1-5: ")
        if ask.isdigit():
            x = eval(ask)
            if x == 0 or x > 5:
                print("\nThis Number Is Not Available\n")
                continue
            if x in check_list:
                print("\nYou Already Used This Number\n")
                continue

            if x == 1:
                print("\nList Average = ", find_average(list_of_numbers))
            if x == 2:
                print("\nList Maximum = ", find_maximum(list_of_numbers))
            if x == 3:
                print("\nList Minimum = ", find_minimum(list_of_numbers))
            if x == 4:
                print("\nAccending Order Of List = ", end="")
                find_accending_order(list_of_numbers)
                print(list_of_numbers)
            if x == 5:
                print("\nDecending Order Of List = ", end="")
                find_decending_order(list_of_numbers)
                print(list_of_numbers)

            check_list.append(x)
        else:
            print("\nEnter A Valid Number\n")
            continue

    condition = input("\nPress 'Y' To Run Again = ").lower()
