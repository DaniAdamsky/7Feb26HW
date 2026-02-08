
#Last_name: str = str(input("Enter Last name: "))
#First_name: str = str(input("Enter Last name: "))
#Country: str = str(input("Enter Last name: "))
#Zipcode: str = str(input("Enter Last name: "))

while True:
    Last_name = input("Enter Last name: ")
    if Last_name.isupper():
        break
    else:
        print("Please enter a valid last name")

while True:
    First_name = input("Enter first name: ")
    if First_name.islower():
        break
    else:
        print("Please enter a valid first name")

while True:
    Country = input("Enter Country name: ")
    if Country.isalpha() and len(Country) <= 3:
        break
    else:
        print("Please enter a valid Country name (ex. US,IL,RU,GER)")

City = input("Enter city address: ")

while True:
    Zipcode = input("Enter Zipcode: ")
    if Zipcode.isdigit() and len(Zipcode) >= 4:
        break
    else:
        print("Please enter a valid Zipcode (at least 4 numbers)")
print(f"'FOR: {Last_name.upper()} {First_name.lower()} \nCOUNTRY: {Country} \nCITY: {City} \nZIPCODE: {Zipcode}")
