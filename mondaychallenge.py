# create two lists


list_one = [1, 2, 3, 4, 5]
list_two = [9, 8, 7, 6, 10]
lists = [list_one, list_two]


# create two lists with an ID so line items can be paired

#listids = [
#    {'listone': '1', 'listtwo': '9'},
#    {'listone': '2', 'listtwo': '8'},
#    {'listone': '3', 'listtwo': '7'},
#    {'listone': '4', 'listtwo': '6'},
#    {'listone': '5', 'listtwo': '5'}
#]

# print the two lists as a table
def table_builder():
    print("|list_one|list_two|")
    print("|-----|-----|")
    for i in range(len(list_one)):
        print(f"|{list_one[i]}|{list_two[i]}|", sep='\n')
        print("|-----|-----|")

table_builder()

# user input an item to a prompt and only that name from the table prints
def get_tablenumber():
    global tablenum
    tablenum = int(input("What item? "))

    if tablenum == 80085 or tablenum == 69 or tablenum == 420:
        print("real funny...")
        print("invalid input")
    elif tablenum > 10:
        print("invalid input: not on list")
    elif tablenum >= 5 or tablenum == 10:
        print(f"List 2 selected, item: {tablenum}")
        tablenumber_adder()
    elif tablenum > 0 or tablenum < 5:
        print(f"List 1 selected, item: {tablenum}")
        tablenumber_adder()

    else:
        print("invalid input: not on list ")
    


# add a new item & sort the lists
def tablenumber_adder():
    table_addition = []

    with open("table.txt", "r") as file:
        for line in file:
            table_addition.append(line.rstrip())
            print("does this work?")


get_tablenumber()


# create a text document with the lists



# read from the lists



# edit lines and write to lists