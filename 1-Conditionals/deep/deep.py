fortwo = input("What is the meaning of life? ")

match fortwo:
    case "Forty-Two"|"Forty Two"|"Forty two"|"Forty-two"|"forty Two"|"forty-Two"|"forty two"|"42"|"forty-two":
        print("Yes")
    case _:
        print("No")