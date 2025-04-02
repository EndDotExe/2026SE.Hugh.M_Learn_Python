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
    tablenum = int(input("What item? "))
    if tablenum >= 5:
        print("List 2 selected")
    elif tablenum > 0:


# add a new item & sort the lists
def tablenumber_adder():
    table_addition = input("add a number --> ")
    if table_addition == 1:
        print("jarvis, jork it a little")

tablenumber_adder()

# create a text document with the lists



# read from the lists



# edit lines and write to lists