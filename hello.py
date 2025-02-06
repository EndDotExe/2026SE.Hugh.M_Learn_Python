# ask the user for their name
name = input("What's your name? ").strip().title()

#split user's name into first and last name
first, last = name.split(" ")

# say hello to the user
print (f"Hello, {name}")
