"""
Send a package from USPS.
1. Define package
    -create user menu with options
2. Enter receiver info
    -check to see if input info is correct
3. Enter sender info
    -check to see if input info is correct
4. Calculate payment depending on shipping location (from - to)
5. Make payment
"""
import json
import time
import sys


class GetAddress:
    def __init__(self, name, street, city, state, zipcode):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode


# define package
def package():
    print("")
    print("Hello! What would you like to send?")
    print("-" * 20 + "USPS MAIN MENU" + "-" * 20)
    print("")
    print("1. Send Mail")
    print("2. Send Package")
    print("")
    print("0. Cancel")
    print("")
    print("-" * 54)

    user = int(input("What would you like to do today? (Select number): "))

    if user == int(1):
        print("Sending Mail.")
    elif user == int(2):
        print("Sending Package.")
    elif user == int(0):
        exit()
    else:
        print("Invalid option. Please select again")
        return package()


package()


# define receiver address
def recipient_address():
    print("Enter shipping info: ")
    send_to = GetAddress(input("Full Name: "),
                         input("Street: "),
                         input("City: "),
                         input("State: "),
                         input("zipcode: "))

    print("")
    print("shipping to:")
    print(json.dumps(send_to.__dict__, indent=4))

    def check_address():
        user = input("Does this address look correct? y/n: ")

        if user.lower() == "y":
            print("")
        elif user.lower() == "n":
            print("Please re-enter address. ")
            return recipient_address()
        else:
            print("Invalid option.")
            return check_address()

    check_address()


recipient_address()


# define sender address
def sender_address():
    print("")
    print("Please enter your address:")
    send_from = GetAddress(input("Full Name: "),
                           input("Street: "),
                           input("City: "),
                           input("State: "),
                           input("zipcode: "))

    print("")
    print("shipping from:")
    print(json.dumps(send_from.__dict__, indent=4))

    def check_address2():
        user = input("Does this address look correct? y/n: ")

        if user.lower() == "y":
            print("")
        elif user.lower() == "n":
            print("Please re-enter address: ")
            return sender_address()
        else:
            print("Invalid option.")
            return check_address2()

    check_address2()


sender_address()


# calculate payment depending on shipping location
def regions():
    """
    west = ["CA", "OR", "WA", "NV", "ID", "UT", "CO", "WY", "MT"]
    midwest = ["ND", "SD", "NE", "KS", "MN", "IA", "MO", "WI", "IL", "IN", "MI", "OH"]
    southwest = ["AZ", "NM", "TX", "OK"]
    southeast = ["AR", "LA", "MS", "TN", "AL", "KY", "GA", "WV", "VA", "NC", "SC", "FL", "MD", "DE"]
    northeast = ["CT", "DC", "HI", "ME", "MA", "NH", "NJ", "NY", "PA", "RI", "VT"]
    noncontig = ["HI", "AK"]
    """

    west_cost = 4.99
    midwest_cost = 6.99
    southwest_cost = 5.99
    southeast_cost = 7.99
    northeast_cost = 8.99
    noncontig_cost = 9.99

    print("")
    print("-" * 35 + "REGIONS" + "-" * 35)
    print("1. West - CA, OR, WA, NV, ID, UT, CO, WY, MT ")
    print("2. Mid West - ND, SD, NE, KS, MN, IA, MO, WI, IL, IN, MI , OH")
    print("3. South West - AZ, NM, TX, OK")
    print("4. South East - AR, LA, MS, TN, AL, KY, GA, WV, VA, NC, SC, FL, MD, DE")
    print("5. North East - CT, DC, HI, ME, MA, NH, NJ, NY, PA, RI, VT")
    print("6. Non Contiguous - HI, AK")
    print("")
    print("0. Return & change shipping addresses.")
    print("-" * 77)
    print("")

    user = int(input("Please select region to ship to. #1-5: "))
    print("")

    if user == int(1):
        print("Region: WEST - United States.")
        print(f"Shipping cost: {west_cost}")
    elif user == int(2):
        print("Region: MID WEST - United States.")
        print(f"Shipping cost: {midwest_cost}")
    elif user == int(3):
        print("Region: SOUTH WEST - United States.")
        print(f"Shipping cost: {southwest_cost}")
    elif user == int(4):
        print("Region: SOUTH EAST - United States.")
        print(f"Shipping cost: {southeast_cost}")
    elif user == int(5):
        print("Region: NORTH EAST - United States.")
        print(f"Shipping cost: {northeast_cost}")
    elif user == int(6):
        print("Region: Non Contiguous - United States.")
        print(f"Shipping cost: {noncontig_cost}")
    elif user == int(0):
        return recipient_address(), sender_address(), regions()
    else:
        print("Invalid option.")
        return user


regions()


# Pay for shipping cost
def pay_shipping():
    cash = "Processing cash ..."
    cash_insert = "Cash received ..."
    card = "Processing card ..."
    pin = "Processing pin ..."

    print("")
    print("-" * 20 + "PAYMENT METHOD" + "-" * 20)
    print("")
    print("1. Cash")
    print("2. Credit/Debit")
    print("")
    print("0. Cancel Transaction")
    print("")
    print("-" * 54)

    user = int(input("How would you like to pay? (Select number): "))

    if user == int(1):
        print("Insert cash below")
        for chars in cash_insert:
            sys.stdout.write(chars)
            time.sleep(0.1)
        for char in cash:
            sys.stdout.write(char)
            time.sleep(0.1)
        print("Payment Successful!")
    elif user == int(2):
        print("Swipe or insert chip.")
        for char in card:
            sys.stdout.write(char)
            time.sleep(0.1)

        input("Enter 4-digit pin: ")

        for chars in pin:
            sys.stdout.write(chars)
            time.sleep(0.1)
        print("Payment Successful!")
    elif user == int(0):
        print("Transaction Cancelled.")
        exit()
    else:
        print("Invalid option")
        return pay_shipping()


pay_shipping()

thanks = "Thank you for shipping with USPS. Have a good day!"
for character in thanks:
    sys.stdout.write(character)
    time.sleep(0.02)
