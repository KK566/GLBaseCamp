def count_holes(num):
    holes = 0
    while True:
        flp = num / 10 # number with decimal places
        num = int(num / 10) # integer
        dgt = round((flp - num) * 10) # resulting digit

        if dgt == 0 or dgt == 4 or dgt == 6 or dgt == 9:
            holes += 1
        if dgt == 8:
            holes += 2
        if num == 0:
            break
    return holes

while True:
    value = input("Enter an integer: ")
    try:
        value = int(value)
        print("The number of holes: ", count_holes(value))
    except:
        print("Invalid input.")
