# Decription: This is program menu for HAB Taxi Service for various services
# Author: Adewale Gbadamosi
# Date: March 31, 2024

# Importing libraries
import datetime
import sys
import random
import time
import FormatValues as fv

# Open the defaults file and read the values into variables
f = open('Defaults.dat', 'r')

NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
f.close()


while True:
    # Gathering customer information and validations 
    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.,")
    while True:
        firstName = input("\nEnter the first name:                      ").strip().title()
        if firstName == "":
            print("Invalid Entry: first name cannot be blank.")
        elif set(firstName).issubset(allowed_char) == False:
            print("Invalid Entry - first name contains invalid character.")
        else:
            break

    while True:
        lastName = input("Enter the last name:                       ").strip().title()
        if lastName == "":
            print("Invalid Entry: last name cannot be blank.")
        elif set(lastName).issubset(allowed_char) == False:
            print("Invalid Entry - last name contains invalid character.")
        else:
            break

    while True:
        strAddress = input("Enter the address:                         ").strip().title()
        if strAddress == "":
            print("Invalid Entry: address cannot be blank.")
        else:
            break
    
    while True:
        city = input("Enter the city of residence:             ").strip().title()
        if city == "":
            print("Invalid Entry: city of residence cannot be blank.")
        elif set(city).issubset(allowed_char) == False:
            print("Invalid Entry - city of residence contains invalid character.")
        else:
            break

    provinceList = ["AB", "BC", "MB", "NB", "NS", "NL", "NT", "NU", "ON", "PE", "SK", "QC", "YT" ]
    while True:
        province = input("Enter the province of residence (XX):    ").strip().upper()
        if province == "":
            print("Invalid Entry: province of residence cannot be blank.")
        elif province not in provinceList:
            print("Invalid Entry - Invalid province, please enter of one of the provinces listed: AB, BC, MB, NB, NS, NL, NT, NU, ON, PE, SK, QC, YT.")
        elif len(province) != 2:
            print("Invalid Entry: province of residence must be two character.")
        else:
            break
    
    while True:
        postalCode = input("Enter the postal code (X9X9X9):                ").strip().upper()
        if postalCode == "":
            print("Invalid Entry: postal code cannot be blank.")
        elif len(postalCode) != 6:
            print("Invalid Entry: postal must be six characters.")
        else:
            break

    while True:
        phoneNum = input("Enter phone number (9999999999):                    ").strip()
        if phoneNum == "":
            print("Invald Entry - Phone number cannot be blank.")
        elif phoneNum.isdigit() == False:
            print("Invalid Entry - phone number must be digit number.")
        elif len(phoneNum) != 10:
            print("Invalid Entry - phone number must 10 digit number.")
        else:
            break
    
    while True:
        licenceNum = input("Enter licence number:                               ").strip()
        if licenceNum == "":
            print("Invald Entry - licence number cannot be blank.")
        else:
            break

    global licenceExpiryDate
    while True:
            try:
                licenceExpiryDateStr = input(f"Enter licence expiry date (YYYY-MM-DD):             ")
                licenceExpiryDate = datetime.datetime.strptime(licenceExpiryDateStr, "%Y-%m-%d")  
            except:
                print("Invalid Entry - licence expiry date entry is not valid date.")
            else:
                break

    while True:
        insuranceCompnay = input("Enter the insurance company:                        ").strip().title()
        if insuranceCompnay == "":
            print("Invalid Entry: insurance company cannot be blank.")
        else:
            break
    while True:
        policyNum = input("Enter policy number:                                ").strip()
        if policyNum == "":
            print("Invald Entry - policy number cannot be blank.")
        else:
            break

    while True:
        ownsCar = input("Enter if car is owned or rental (O for owned and R for rental): ").strip().upper()
        if ownsCar == "":
            print("Invalid Entry: the entry cannot be blank.")
        elif len(ownsCar) != 1:
            print("Invalid Entry - enter either O or R for owned or rental respectively")
        elif ownsCar != "O" and ownsCar != "R":
            print("Invalid Entry - Must enter either O or R, please try again.")
        else:
            break
    # Get current date
    currentDate = fv.FDateS(datetime.datetime.now())
    global montlyStandFee 
    if ownsCar == "O":
        ownsCar = "Owned"
        monthlyStandFee = MONTHLY_STAND_FEE
        payment = monthlyStandFee
        Tax = payment * HST_RATE
        balanceDue = monthlyStandFee + Tax

    if ownsCar == "R":
        ownsCar = "Rental"
        while True:
            try:
                startDateStr = input(f"Enter rental start date (YYYY-MM-DD):               ")
                startDate = datetime.datetime.strptime(startDateStr, "%Y-%m-%d")  
            except:
                print("Invalid Entry - rental start date entry is not valid date.")
            else:
                break
        while True:
            try:
                endDateStr = input(f"Enter rental end date (YYYY-MM-DD):                 ")
                endDate = datetime.datetime.strptime(endDateStr, "%Y-%m-%d")  
            except:
                print("Invalid Entry - rental date entry is not valid date.")
            else:
                break

        global RentalFee
        rentalDuration = endDate.day - startDate.day
        if rentalDuration < 7:
            rentalFee = rentalDuration * DAILY_RENTAL_FEE
            amount = rentalFee
            Tax = amount * HST_RATE
            balanceDue = rentalFee + Tax
        else:
            rentalFee = WEEKLY_RENTAL_FEE + (rentalDuration % 7) * DAILY_RENTAL_FEE
            amount = rentalFee
            Tax = amount * HST_RATE
            balanceDue = rentalFee + Tax

    global fullName
    fullName = firstName + " " + lastName
    global cityProvincePostalCode
    cityProvincePostalCode = city + " " + province + " " + postalCode


    print()
    print(f"                                 HAB Taxi Service")
    print(f"                              New Employee Record Slip")
    print()
    print(f" Driver Number: {NEXT_DRIVER_NUM}") 
    print()
    print(f" Driver Personal Details ")
    print(f"        Name:                {fullName}")
    print(f"        Address:             {strAddress}")
    print(f"                             {cityProvincePostalCode}")
    print(f"        Phone Numner:        {phoneNum}")
    print()
    print(f" Licence Details ")
    print(f"        Licence Number:      {licenceNum}")
    print(f"        Licence Expiry Date: {licenceExpiryDateStr}")
    print()
    print(f" Insurance Details ")
    print(f"        Insurance Company:   {insuranceCompnay}")
    print(f"        Policy Number:       {policyNum}")
    print()
    print(f" Car Details ")
    print(f"        Car Type:            {ownsCar}")
    if ownsCar == "O":
        print(f"        Monthly Stand Fee:   {amount}")
    else:
        print(f"        Rental Fee:          {amount}")
    print(f"        HST:                 {Tax}")
    print(f"        Balance Due:         {balanceDue}")


        # Store the policy data into a file called Policy.dat
    for _ in range(5):  # Change to control no. of 'blinks'
        print('Saving policy data ...', end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)

    print()
    print("Claim data successfully saved ...", end='\r')
    time.sleep(1)  # To create the blinking effect
    sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns

    f = open("Employee.dat", "a")
    f.write("{}, ".format(NEXT_DRIVER_NUM))
    f.write("{}, ".format(firstName))
    f.write("{}, ".format(lastName)) 
    f.write("{}, ".format(strAddress))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postalCode))
    f.write("{}, ".format(phoneNum))
    f.write("{}, ".format(licenceNum))
    f.write("{}, ".format(licenceExpiryDateStr))
    f.write("{}, ".format(insuranceCompnay))
    f.write("{}, ".format(policyNum))
    f.write("{}, ".format((ownsCar)))
    f.write("{}, ".format(str(currentDate)))
    f.write("{}, ".format(str(amount)))
    f.write("{}, ".format(str(Tax)))
    f.write("{}\n".format(str(balanceDue)))
    f.close()


    NEXT_DRIVER_NUM += 1  # Increase the next policy number

    f = open('Defaults.dat', 'w')
    f.write("{}\n".format(str(NEXT_TRANSACTION_NUM)))
    f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
    f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
    f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
    f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.close()

    # Ask if the user wants to add another customer
    while True:
        anotherDriver = input("\nDo you want to enter information for another customer? (Y/N): ").upper()
        if anotherDriver == "":
            print("Inalid Entry - another customer can not be blank.")
        elif len(anotherDriver) != 1:
            print("Invalid Entry - enter either Y or N if want o proceed to another customer")
        elif anotherDriver != "Y" and anotherDriver != "N":
            print("Invalid Entry - Must enter either Y or N, please try again.")
        else:
            break
    
    if anotherDriver == "N":
        print(f"\nPolicy data has been saved. Next policy number: {NEXT_DRIVER_NUM}")
        break 

print("\nProgram ended.")
print("Thanks for using the new employee program!")