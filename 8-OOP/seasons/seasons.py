from datetime import date

def main():
    #prompt user for their DOB:
    dateofbirth = date.fromisoformat(input("Date of Birth (YYYY-MM-DD): "))
    currentdate = date.today()
    timealive = (currentdate - dateofbirth)
    minutes = 1440 * (timealive)
    youexist = str(minutes).split(' ')[0]
    
    print(f"Today's date is {currentdate}")
    print(f"You've been alive for roughly {youexist} minutes!")


if __name__ == "__main__":
    main()

