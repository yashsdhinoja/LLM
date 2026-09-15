day = 5
month = 3

match day:
    case 1 | 3 | 5 | 7 if month == 3:
        print("Good")
    case 2 | 4 | 6 | 0 if month == 5:
        print("Night")
    case _:
        print("Try Valid Number !!!!!")