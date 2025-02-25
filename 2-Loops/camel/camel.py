imtweaking = input("Variable Name here: ")

for silly in imtweaking:
    if silly.isupper():
        silly = silly.lower()
        silly = "_" + silly
    print (silly, end="")
print("")