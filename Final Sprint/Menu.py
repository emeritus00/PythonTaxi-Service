# Decription: This is program menu for HAB Taxi Service for various services
# Author: Group 7
# Date: April 13, 2024

# Importing libraries
import datetime
import sys
import random
import time
import FormatValues as fv

# Program counters for menu options
newEmployee = 0
companyRevenue = 0
companyExpense = 0
carRentals = 0
employeePayment = 0
profitListing = 0
driverFinancial = 0
carTracker = 0


# Open the defaults file and read the values into variables
f = open('Defaults.dat', 'r')

NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
NEXT_INVOICE_NUM = int(f.readline())
f.close()

# Functions for manu options

# Function for enter new employee
def enterNewEmployee():
    while True:
        global NEXT_DRIVER_NUM
        global newEmployee
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
        global monthlyStandFee 
        if ownsCar == "O":
            ownsCar = "Owned"
            monthlyStandFee = MONTHLY_STAND_FEE
            amount = monthlyStandFee
            Tax = amount * HST_RATE
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
        f.write("{}\n".format(str(NEXT_INVOICE_NUM)))
        f.close()

        newEmployee += 1

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

# Functions for enter company revenue
def enterCompanyRevenue():
    global companyRevenue
    print("\nThis program menu is under construction. Please bear with us")

    print("\nProgram ended.")
    print("Thanks for using the HABI Taxi Service!")
    
    companyRevenue += 1

# Functions for enter company expenses
def compnayExpenses():
    while True:
        global NEXT_INVOICE_NUM
        global companyExpense
        # Invoice item information
        invoiceLstItem = []
        invoiceLstSubTotal = []
        invoiceLstItemCost = []
        invoiceLstItemQuantity = []
        invoiceLstHSTItem = []
        invoiceLstItemTotal = []

    # Gathering inputs
        print(f"   ")
        while True:
            try:
                invoiceDate = input("Enter the invoice date (YYYY-MM-DD): ")
                invoiceDate = datetime.datetime.strptime(invoiceDate, "%Y-%m-%d")
            except:
                print("Date Entry Error - invoice date must be entered as (YYYY-MM-DD).")
            else:
                break

        while True:
            driverNum = input("Enter the driver number for this invoice (9999): ")
            with open('Employee.dat', 'r') as file:
                num = file.read()
                if driverNum == "":
                    print("Data Entry Error - driver number must be entered.")
                elif driverNum in num:
                    break
                else:
                    print("Data Entry Error - driver number does not exist, pleas enter existing number.")

        firstName = ""
        lastName = ""
        employeeFile = open('Employee.dat', 'r')
        lines = employeeFile.readlines()
        for line in lines:
            sline = line.split(',')
        
            if sline[0] == driverNum:
                firstName = sline[1]
                lastName = sline[2]

        driverName = firstName + " " + lastName

        # Enter items and calculate total + store in invoice
        while True:
            itemName = input("Enter the item name (Enter 'Done' to finish the entry of items for this invoice): ").title()
            if itemName == "Done":
                break
            itemCost = float(input("Enter the item cost: "))
            itemQuantity = int(input("Enter how many of this item where bought: "))
            itemSubTotal = itemCost * itemQuantity
            itemHST = itemSubTotal * HST_RATE
            itemTotal = itemSubTotal + itemHST

            invoiceLstItem.append(itemName)
            invoiceLstItemCost.append(itemCost)
            invoiceLstItemQuantity.append(itemQuantity)
            invoiceLstSubTotal.append(itemSubTotal)
            invoiceLstHSTItem.append(itemHST)
            invoiceLstItemTotal.append(itemTotal)
            


        # Items cost
        itemTotNum = len(invoiceLstItem)
        subTotal = sum(invoiceLstSubTotal)
        HST = subTotal * HST_RATE
        totPayment = subTotal + HST

        print(f"   ")
        print(f"   ")
        print(f"                                HAB Taxi Services")
        print(f"                                 Company Expenses")
        print(f"   ")
        print(f"   Driver Name:  {driverName:<20s}      Invoice Number: {NEXT_INVOICE_NUM:<4d}")
        print(f"   Driver Number: {driverNum:<4s}                     Invoice Date:   {fv.FDateM(invoiceDate):<9s}")
        print(f"")
        print(f"   ==============================================================================")
        print("    Item  Description         Quantity   Cost       Subtotal    HST        Total")
        print("     No                                                                    Cost")
        print(f"   ==============================================================================")
        Counter = 1
        for i in range(itemTotNum):
            print(f"    {Counter:<2d}    {invoiceLstItem[i]:<20s}   {invoiceLstItemQuantity[i]:>2d}     {fv.FDollar2(invoiceLstItemCost[i]):>7s}     {fv.FDollar2(invoiceLstSubTotal[i]):>7s}   {fv.FDollar2(invoiceLstHSTItem[i]):>7s}     {fv.FDollar2(invoiceLstItemTotal[i]):>7s}")
            Counter += 1
        print(f"   ==============================================================================")
        print(f"                                                  {fv.FDollar2(subTotal):>9s} {fv.FDollar2(HST):>9s}   {fv.FDollar2(totPayment):>9s}")
        print(f"   ==============================================================================")
        print(f"   Number of items: {itemTotNum:<2d}")
        print()
        print(f"   Total Expenses")
        print(f"   Total:         {fv.FDollar2(subTotal):>9s}")
        print(f"   HST:           {fv.FDollar2(HST):>9s}")
        print(f"   Total Payment: {fv.FDollar2(totPayment):>9s}")
        print(f"   ")


        Sure = input("Is information entered correct? (Y/N): ").upper()
        if Sure == "":
            print("Data Entry Error - please enter if the information entered is corect?")
        elif Sure != "Y" and Sure != "N":
            print("Data Entry Error - enter Y for Yes or N for No.")
        elif Sure == "Y":

            # Store the claim data into a file called Claims.dat
            # Print the message that the system is Saving ... so that it blinks.
            for _ in range(5):  # Change to control no. of 'blinks'
                print('Saving claim data ...', end='\r')
                time.sleep(.3)  # To create the blinking effect
                sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
                time.sleep(.3)

            f = open("Expenses.dat", "a")
            f.write("{}, ".format(NEXT_INVOICE_NUM))
            f.write("{}, ".format(fv.FDateM(invoiceDate)))
            f.write("{}, ".format(driverNum)) 
            f.write("{}, ".format(driverName))
            f.write("{}, ".format(invoiceLstItem))
            f.write("{}, ".format(fv.FDollar2(subTotal)))
            f.write("{}, ".format(fv.FDollar2(HST)))
            f.write("{}\n".format(fv.FDollar2(totPayment)))
            f.close()


            NEXT_INVOICE_NUM += 1  # Increase the next invoice number

            f = open('Defaults.dat', 'w')
            f.write("{}\n".format(str(NEXT_TRANSACTION_NUM)))
            f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
            f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
            f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
            f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
            f.write("{}\n".format(str(HST_RATE)))
            f.write("{}\n".format(str(NEXT_INVOICE_NUM)))
            f.close()

            # Now that is has written, display the message to indicate the data is saved.
            print()
            print("Claim data successfully saved ...", end='\r')
            time.sleep(1)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns


            companyExpense += 1

        # Leave the program
        print()
        Cont = input("Do you want to continue or restart the program? (Y/N): ").upper()
        if Cont == "":
            print("Data Entry Error - please enter if you want to continue?")
        elif Cont != "Y" and Cont != "N":
            print("Data Entry Error - enter Y for Yes or N for No.")
        elif Cont == "N":
            break

# Function to track car rentals
def trackCarRentals():
    global carRentals
    print("\nThis program menu is under construction. Please bear with us")

    print("\nProgram ended.")
    print("Thanks for using the HABI Taxi Service!")
    
    carRentals += 1

# Function to record employee payment
def recordEmployeePayment():
    global employeePayment

    firstName = ""
    lastName = ""
    # Begin program
    while True:
        # Enter inputs + input IF statements here
        print()
        Rent_Pay = input("Are you renting a car or making a payment (car or pay): ")
        if Rent_Pay == "car":
            while True:
                Driver_Num = input("Enter the driver number: ")
                with open('Employee.dat', 'r') as file:
                    num = file.read()
                if Driver_Num == "":
                    print("Data Entry Error - driver number must be entered.")
                elif Driver_Num in num:
                    break
                else:
                    print(
                        "Data Entry Error - driver number does not exist, pleas enter existing number.")
            employeeFile = open("Employee.dat", "r")
            for driver in employeeFile:
                driverLst = driver.split(",")
                driverNum = driverLst[0].strip()

                if driverNum == Driver_Num:
                    firstName = driverLst[1].strip()
                    lastName = driverLst[2].strip()
            
            driverName = firstName + " " + lastName
            Start_Date = input("Enter the start date: ")
            Start_Date = datetime.datetime.strptime(Start_Date, "%Y-%m-%d")
            Car_Num = int(input("Enter the car number: "))
            Rent_Type = input("Enter the rental type (day or week): ")
            while True:
                if Rent_Type == "day":
                    Num_Days = int(
                        input("Enter the number of days the car is rented: "))
                    break
                elif Rent_Type == "week":
                    Num_Days = 7
                    break
                elif Rent_Type != "day" or "week":
                    print("Data Entry Error - rent type is not day or week")
                else:
                    break
        elif Rent_Pay == "pay":
            Driver_Num = input("Enter the driver's number: ")
            employeeFile = open("Employee.dat", "r")
            for driver in employeeFile:
                driverLst = driver.split(",")
                driverNum = driverLst[0].strip()
                
                if driverNum == Driver_Num:
                    firstName = driverLst[1].strip()
                    lastName = driverLst[2].strip()
                driverName = firstName + " " + lastName
            
            Pay_Date = datetime.date.today()
            Pay_Amount = float(input("Enter the payment amount: "))
            Pay_Reason = input("Enter the reason for the payment: ").title()
            while True:
                Pay_Method = input("Enter the payment method(cash, debit or credit): ").title()
                if Pay_Method == "Cash":
                    break
                elif Pay_Method == "Debit":
                    break
                elif Pay_Method == "Credit":
                    break
                else:
                    print("Data Entry Error - payment method is not valid")
        else:
            print("Data Entry Error - car or pay haven't been chosen")

        # Enter calculations here
        if Rent_Pay == "car":
            if Rent_Type <= "day":
                Rental_Cost = DAILY_RENTAL_FEE * Num_Days
            else:
                Rental_Cost = WEEKLY_RENTAL_FEE + (DAILY_RENTAL_FEE * Num_Days)
            Tax = Rental_Cost * HST_RATE
            Total = Tax + Rental_Cost
            Cur_Date = datetime.datetime.now()
        else:
            Rental_Cost = 0
            Tax = 0
            Total = 0
            Cur_Date = datetime.datetime.now()

        # Enter print statements here
        if Rent_Pay == "car":
            print(f"\n____________________________________________________________")
            print(f"\n                     HAB Taxi Services")
            print(f"                       Rental Receipt")
            print()
            print(f"                            Transaction ID: {NEXT_TRANSACTION_NUM}")
            print(f"                            Date:           {fv.FDateM(Cur_Date)}")
            print()
            print(f"Driver Number:  {Driver_Num}")
            print(f"Driver Name:    {driverName}")
            print()
            print(f"Rental ID:      {random.randint(1,899999) + 100000}")
            print(f"Start Date:     {Start_Date}")
            print(f"Car Number:     {Car_Num}")
            print(f"Rental Type:    {Rent_Type}")
            print(f"Number of Days: {Num_Days}")
            print()
            print(f"Rental Cost:    {fv.FDollar2(Rental_Cost):>7s}")
            print(f"HST:            {fv.FDollar2(Tax):>7s}")
            print(f"                -------")
            print(f"Total:        {fv.FDollar2(Total):>9s}")
            print(f"                -------")
            print()
            print(f"               Thank you for your business!")
            print(f"____________________________________________________________")

        else:
            print(f"\n____________________________________________________________")
            print(f"\n                     HAB Taxi Services")
            print(f"                       Rental Receipt")
            print()
            print(f"                            Payment ID: {random.randint(1,999999) + 100000}")
            print(f"                            Date:       {fv.FDateM(Cur_Date)}")
            print()
            print(f"Driver Number:      {Driver_Num}")
            print(f"Driver Name:        {driverName}")
            print()
            print(f"Payment Date:       {Pay_Date}")
            print(f"Payment Amount:     {fv.FDollar2(Pay_Amount)}")
            print(f"Reason for payment: {Pay_Reason}")
            print(f"Payment Method:     {Pay_Method}")
            print()
            print(f"               Thank you for your business!")
            print(f"____________________________________________________________")
            print()
            Sure = input("Is information entered corect? (Y/N): ").upper()
            if Sure == "":
                print("Data Entry Error - please enter if the information entered is corect?")
            elif Sure != "Y" and Sure != "N":
                print("Data Entry Error - enter Y for Yes or N for No.")
            elif Sure == "Y":

                # Store the claim data into a file called Claims.dat
                # Print the message that the system is Saving ... so that it blinks.
                for _ in range(5):  # Change to control no. of 'blinks'
                    print('Saving receipt data ...', end='\r')
                    time.sleep(.3)  # To create the blinking effect
                    # Clears the entire line and carriage returns
                    sys.stdout.write('\033[2K\r')
                    time.sleep(.3)
            f = open('Defaults.dat', 'w')
            f.write("{}\n".format(str(NEXT_TRANSACTION_NUM)))
            f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
            f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
            f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
            f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
            f.write("{}\n".format(str(HST_RATE)))
            f.write("{}\n".format(str(NEXT_INVOICE_NUM)))
            f.close()
            

            # Now that is has written, display the message to indicate the data is saved.
            print()
            print("Receipt data successfully saved ...", end='\r')
            time.sleep(1)  # To create the blinking effect
            # Clears the entire line and carriage returns
            sys.stdout.write('\033[2K\r')
        
        employeePayment += 1 # Program counter

        Cont = input("Do you want to continue or restart the program? (Y/N): ").upper()
        if Cont == "":
            print("Data Entry Error - please enter if you want to continue?")
        elif Cont != "Y" and Cont != "N":
            print("Data Entry Error - enter Y for Yes or N for No.")
        elif Cont == "N":
            break

    print("\nProgram ended.")
    print("Thanks for using the HABI Taxi Service!")

# Function to print company profit listing
def printCompanyProfit():
    global profitListing
    print("\nThis program menu is under construction. Please bear with us")

    print("\nProgram ended.")
    print("Thanks for using the HABI Taxi Service!")

    profitListing += 1
 
# Function to print driver financial listing
def printDriverFinancial():
    global driverFinancial
    # Gathering inputs
    while True:
        while True:
            askDriverNum = input("Enter the driver number (9999): ").strip()
            with open('Employee.dat', 'r') as file:
                num = file.read()
                if askDriverNum == "":
                    print("Data Entry Error - driver number must be entered.")
                elif askDriverNum.isdigit() == False:
                    print("Invalid Entry - Driver number must be digit number.")
                elif len(askDriverNum) != 4:
                    print("Invalid Entry - Driver number must 4 digit number.")
                elif askDriverNum not in num:
                    print("Data Entry Error - Driver number does not exist. Please enter an existing number.")
                else:
                    break
            
        while True:
            try:
                startDateStr = input(f"Enter start date (YYYY-MM-DD): ")
                startDate = datetime.datetime.strptime(startDateStr, "%Y-%m-%d")  
            except:
                print("Invalid Entry - start date entry is not valid date.")
            else:
                break

        while True:
            try:
                endDateStr = input(f"Enter end date (YYYY-MM-DD):   ")
                endDate = datetime.datetime.strptime(endDateStr, "%Y-%m-%d")  
            except:
                print("Invalid Entry - date entry is not valid date.")
            else:
                break
    # Read from employee file
        employeeFile = open("Employee.dat", "r")
        for driver in employeeFile:
                driverLst = driver.split(",")
                driverNum = driverLst[0].strip()

                if driverNum == askDriverNum:
                    firstName = driverLst[1].strip()
                    lastName = driverLst[2].strip()

        employeeFile.close()

    # Counters and accumulators
        counter = 0
        totalAmount = 0
        totalTax = 0
        totalTotal = 0
        totalBalanceDue = 0

    # Displaying the reports
        print("\n")
        print("                                        HABI Taxi Service")
        print("                                     Driver Financial Listing")
        print(f"Name:          {firstName} {lastName}")
        print(f"Driver Number: {askDriverNum}")
        print(f"\nFiancial Lists from {startDateStr} to {endDateStr}")
        print("\nTran    Date        Description            Amount        Tax          Total         Balance")
        print("ID                                                                                    Due")
        print("===========================================================================================")
        revenueFile = open("Revenue.dat", "r")
        for driverFinance in revenueFile:
            driverFinanceLst = driverFinance.split(",")
            if len(driverFinanceLst) >= 7:
                transNo = driverFinanceLst[0].strip()
                transDateStr = driverFinanceLst[1].strip()
                description = driverFinanceLst[2].strip()
                driverNum = driverFinanceLst[3].strip()
                amount = float(driverFinanceLst[4].strip())
                Tax = float(driverFinanceLst[5].strip())
                balanceDue = float(driverFinanceLst[6].strip())
            
            total = amount + Tax

            try:
                transDate = datetime.datetime.strptime(transDateStr, "%Y-%m-%d")
                if driverNum == askDriverNum and startDate <= transDate <= endDate:

                    counter += 1
                    totalAmount = totalAmount + amount
                    totalTax += Tax
                    totalTotal += total
                    totalBalanceDue += balanceDue

                    print(f"{transNo}     {transDateStr}  {description}     {fv.FDollar2(amount):>7s}      {fv.FDollar2(Tax):>7s}       {fv.FDollar2(total):>7s}       {fv.FDollar2(balanceDue):>7s}")
                    
            except ValueError:
                print("Invalid Entry - Date format in Revenue.dat is not valid.")
        print("===========================================================================================")
        print(f"Total                                    {fv.FDollar2(totalAmount):>9s}    {fv.FDollar2(totalTax):>9s}     {fv.FDollar2(totalTotal):>9s}     {fv.FDollar2(totalBalanceDue):>9s}")
        print("===========================================================================================")
        print(f"No of financial record: {counter}")

        print("\n")
        print(f"Amount:        {fv.FDollar2(totalAmount):>7s}  ")
        print(f"HST:           {fv.FDollar2(totalTax):>7s}")

        print(f"\nTotal:       {fv.FDollar2(totalTotal):>7s}")
        print(f"Payment:       $###.## ")
        print("----------------------")
        print(f"Balance Due: {fv.FDollar2(totalBalanceDue):>9s}") 
        print("----------------------")

        print("\n***Note***")
        print("1. Payment made by driver to be in the payment")
        print("2. This is just for dispaly only. Balance due meant to update from employee table")

        revenueFile.close()

        driverFinancial += 1

        # Ask if the user wants to add another customer
        while True:
            anotherDriver = input("\nDo you want to access another driver financial listing? (Y/N): ").upper()
            if anotherDriver == "":
                print("Inalid Entry - another driver entry can not be blank.")
            elif len(anotherDriver) != 1:
                print("Invalid Entry - enter either Y or N if want o proceed to another driver")
            elif anotherDriver != "Y" and anotherDriver != "N":
                print("Invalid Entry - Must enter either Y or N, please try again.")
            else:
                break
        
        if anotherDriver == "N":
            break 

    print("\nProgram ended.")
    print("Thanks for using the driver financial listing program!")

# Function to track car inventory
def trackCarInventory():
    global carTracker
    count = 0
    lastCounter = 0
    nextCounter = 0
    moreMileageCar = 0

    lastSixMonth = datetime.datetime.now() + datetime.timedelta(days = -180)
    nextSixMonth = datetime.datetime.now() + datetime.timedelta(days = 180)

    print(f"\n                                                HAB Taxi Services")
    print("                                                  Vehicle Report")
    print("Date:", datetime.date.today().strftime('%Y-%m-%d'))
    print(f"================================================================================================================================")
    print(f"Car    Make      Model     Year      Color     Plate      Year        Mileage    Rented     Rental     Last           Next")
    print(f"                                               Number     Registered             Driver     ID         Service        Serive")
    print(f"================================================================================================================================")
    vehicleFile = open("Vehicles.dat", "r")
    for car in vehicleFile:
        carLst = car.split(",")
        if len(carLst) >= 2:
            carNumber = carLst[0].strip()
            carMarker = carLst[1].strip()
            carModel = carLst[2].strip()
            carYear = carLst[3].strip()
            carColor = carLst[4].strip()
            carPlateNum = carLst[5].strip()
            carRegYear = carLst[6].strip()
            carMileage = int(carLst[7].strip())
            driverNum = carLst[8].strip()
            rentalID = carLst[9].strip()
            lastServiceStr = carLst[10].strip()
            nextServiceStr = carLst[11].strip()

            lastService = datetime.datetime.strptime(lastServiceStr, "%Y-%m-%d")
            nextService = datetime.datetime.strptime(nextServiceStr, "%Y-%m-%d")

            if lastService >= lastSixMonth:
                lastCounter += 1
            
            if nextService <= nextSixMonth:
                nextCounter += 1
            
            if carMileage > 100000:
                moreMileageCar += 1
        
            count += 1

        print(f"{carNumber}     {carMarker:<6s}    {carModel:<7s}    {carYear:<6s}    {carColor:<6s}    {carPlateNum:<6s}     {carRegYear:<6s}  {carMileage:<6d}     {driverNum:<4s}       {rentalID:<6s}     {lastServiceStr}     {nextServiceStr}")
    print(f"================================================================================================================================")
    print(f"Number of cars: {count}")


    print(f"\n {lastCounter} vehicle(s) was/were service in last 180 days")
    print(f" {nextCounter} vehicle(s) is/are due service in next 180 days")
    print(f" {moreMileageCar} vehicle(s) has/have mileage of over 100,000")



    vehicleFile.close()

    print("\nProgram ended.")
    print("")

    carTracker += 1

# This is the begining of the program that charge driver with own vehicle at the start of the month

# Check if it's the first day of the month
today = datetime.date.today()
todayStr = today.strftime("%Y-%m-%d")
# This line can be used for testing for first day of the month
'''
# todayStr = "2024-06-01" 
# today = datetime.datetime.strptime(todayStr, "%Y-%m-%d")
'''

count = 0
description = "Monthly Stand Fees"

if today.day == 1:
    employeeFile = open("Employee.dat", "r")
    for driver in employeeFile:
        driverLst = driver.split(",")
        driverNum = driverLst[0].strip()
        firstName = driverLst[1].strip()
        lastName = driverLst[2].strip()
        strAddress = driverLst[3].strip()
        city = driverLst[4].strip()
        province = driverLst[5].strip()
        postalCode = driverLst[6].strip()
        phoneNum = driverLst[7].strip()
        licenceNum = driverLst[8].strip()
        licenceExpiryDateStr = driverLst[9].strip()
        insuranceCompnay = driverLst[10].strip()
        policyNum = driverLst[11].strip()
        ownsCar = driverLst[12].strip()
        currentDate = driverLst[13].strip()
        amount = driverLst[14].strip()
        Tax = driverLst[15].strip()
        balanceDue = driverLst[16].strip()

        
        if ownsCar == "Owned":  # Check if the employee has their own car
            balanceDue = float(balanceDue) + MONTHLY_STAND_FEE + (HST_RATE * MONTHLY_STAND_FEE) # Update balance due
            balanceDue = str(balanceDue)
            #Update balance due in the employees table

            revenueFile = open("Revenue.dat", "a")
            revenueFile.write("{}, ".format(NEXT_TRANSACTION_NUM))
            revenueFile.write("{}, ".format(todayStr))
            revenueFile.write("{}, ".format(description)) 
            revenueFile.write("{}, ".format(driverNum))
            revenueFile.write("{}, ".format(amount))
            revenueFile.write("{}, ".format(Tax))
            revenueFile.write("{}\n".format(balanceDue))
            revenueFile.close()

        # Update balance due in the employees table - not coded
        

            count += 1
            NEXT_TRANSACTION_NUM += 1

    employeeFile.close()

# Write constant back to the defaults file
f = open('Defaults.dat', 'w')
f.write("{}\n".format(str(NEXT_TRANSACTION_NUM)))
f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(NEXT_INVOICE_NUM)))
f.close()

print("*** Balance update ***")
print("Balance due updated in the employee table")
print(count)


while True:
    print()
    print("**********************************************")
    print("This is the beginning of a new program session ")
    print("**********************************************")
    print("")
    print("HABI Taxi Service - Main Menu")
    print(f"Date: {todayStr}")
    print(f"Session totals:  New Employee: {newEmployee} Company Revenue: {companyRevenue} Company Expenses: {companyExpense} Track Car Rental: {carRentals} Employee Payment: {employeePayment}  Company Profit Listing: {profitListing} Driver Financial Listing: {driverFinancial} Car Inventory: {carTracker}")
    print()
    print("1. Enter a New Employee (Driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing")
    print("7. Print Driver Financial Listing")
    print("8. Car Inventory")
    print("9. Quit Program")
    print()
   
    while True:
        try:
            Choice = input("Enter choice (1 - 9): ")
            Choice = int(Choice)
        except:
            print("Data Entry Error - must be a valid number between 1 and 6.")
        else:
            if Choice < 1 or Choice > 9:
                print("Data Entry Error - must be a valid number between 1 and 6.")
            else:
                break
            
    if Choice == 1:
        enterNewEmployee()
    elif Choice == 2:
        enterCompanyRevenue()
    elif Choice == 3:
       compnayExpenses()
    elif Choice == 4:
        trackCarRentals()
    elif Choice == 5:
        recordEmployeePayment()
    elif Choice == 6:
        printCompanyProfit()
    elif Choice == 7:
        printDriverFinancial()
    elif Choice == 8:
        trackCarInventory()
    else:
        break
 
# Any housekeeping duties at the end of the program.
print("\nProgram ended.")
print("HABI Taxi Service.")
print("\nSummary of your session: ")
print(f"New Employee: {newEmployee} \nCompany Revenue: {companyRevenue} \nCompany Expenses: {companyExpense} \nTrack Car Rental: {carRentals} \nEmployee Payment: {employeePayment}  \nCompany Profit Listing: {profitListing} \nDriver Financial Listing: {driverFinancial} \nCar Inventory: {carTracker}")
print("Total Sessions: ", newEmployee + companyRevenue + companyExpense + carRentals + employeePayment + profitListing + driverFinancial + carTracker)