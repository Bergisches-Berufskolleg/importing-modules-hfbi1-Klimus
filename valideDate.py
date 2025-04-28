from leapYear import isLeapYear

def validateDate(day, month, year):
    # ...
    return True

def main():
    day   = int(input("Gib ein Tag ein: "))
    month = int(input("Gib ein Monat ein: "))
    year  = int(input("Gib ein Jahr ein: "))
    print(validateDate(day, month, year))

if __name__ == "__main__":
    main()
