from datetime import date

def main():
    #prompt user for their DOB:
    dateofbirth = date(input("Date of Birth: (YYYY•MM•DD)"))
    timealive = int(date.today - dateofbirth) 


if __name__ == "__main__":
    main()