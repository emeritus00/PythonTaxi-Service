# This code is for a receipt for a car rental or payment
# Author: Joshua Youden
# Date edited: April 12th, 2024

# Enter required liberaries
import datetime
import FormatValues as fv
import sys
import time
import random

# Enter constants here
f = open('Defaults.dat', 'r')
NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
f.close()


firstName = ""
lastName = ""
# Begin program
while True:
    # Enter inputs + input IF statements here
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
        f.close()

        # Now that is has written, display the message to indicate the data is saved.
        print()
        print("Receipt data successfully saved ...", end='\r')
        time.sleep(1)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')

        Cont = input("Do you want to continue or restart the program? (Y/N): ").upper()
        if Cont == "":
            print("Data Entry Error - please enter if you want to continue?")
        elif Cont != "Y" and Cont != "N":
            print("Data Entry Error - enter Y for Yes or N for No.")
        elif Cont == "N":
            break
print("\nEnd program")
