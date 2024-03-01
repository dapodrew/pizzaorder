print("Thank you for choosing Python Pizza Deliveries!")
size = input("what size do you want? S, M, L. ")
add_pepperoni = input("Do you need pepperoni ? Y or N. ")
extra_cheese = input("chesse? Y or N. ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")

elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")


elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")





