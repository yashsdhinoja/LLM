day = 6

match day:
    case 1 | 3 | 5 | 7:
        print("ON")
    case 2 | 4 | 6 :
        print("OFF")
    case _:
        print("Try Again !!!")