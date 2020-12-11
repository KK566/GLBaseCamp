def count_holes(num):
    holes = 0

    try:
        num = int(num)
    except:
        print('Invalid input.')
        return 'err'

    while True:
        flp = num / 10 # number with decimal places
        num = int(flp) # integer
        dgt = round((flp - num) * 10) # resulting digit

        if dgt in [0, 4, 6, 9]:
            holes += 1
        elif dgt == 8:
            holes += 2

        if num == 0: # imitating the do-while behavior
            break

    return holes

def main():
    while True:
        value = input('Enter an integer (q to exit): ')

        if value.lower().strip() == 'q':
            break

        if count_holes(value) != 'err':
            if count_holes(value) > 0:
                print('The number of holes: ', count_holes(value))
            else:
                print('There are no holes in this number.')

if __name__ == '__main__':
    main()
