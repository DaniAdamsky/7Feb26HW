

Volume_lvl: int = int(input("Enter Volume Level: "))

if Volume_lvl in range(1 , 10 + 1):
    match Volume_lvl:
        case 1:
            print("Very quiet")
        case 2:
            print("Quiet")
        case 3 | 4:
            print("low")
        case 5:
            print("medium")
        case 6:
            print("medium high")
        case 7:
            print("loud")
        case 8:
            print("very loud")
        case 9 | 10:
            print("max volume")
else:
    print("Invalid Volume Level")
