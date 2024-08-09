# import libraries 
import datetime
import FormatValues as fv
import sys
import time

# Constants 
f = open('Defaults.dat', 'r')
NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
NEXT_INVOICE_NUM = int(f.readline())
f.close()

# Main program
while True:
    # Invoice item information
    invoiceLstItem = []
    invoiceLstSubTotal = []
    invoiceLstItemCost = []
    invoiceLstItemQuantity = []
    invoiceLstHSTItem = []
    invoiceLstItemTotal = []

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
        driverNum = input("Enter the driver number for this invoice: ")
        with open('Employee.dat', 'r') as file:
            num = file.read()
            if driverNum == "":
                print("Data Entry Error - driver number must be entered.")
            elif driverNum in num:
                break
            else:
                print("Data Entry Error - driver number does not exist, pleas enter existing number.")

    driverFirstName = ""
    driverLastName = ""
    employeeFile = open('Employee.dat', 'r')
    lines = employeeFile.readlines()
    for line in lines:
        sline = line.split(',')
    
        if sline[0] == driverNum:
            driverFirstName = sline[1]
            driverLastName = sline[2]

    driverName = driverFirstName + " " + driverLastName

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



    # Leave the program
    Cont = input("Do you want to continue or restart the program? (Y/N): ").upper()
    if Cont == "":
        print("Data Entry Error - please enter if you want to continue?")
    elif Cont != "Y" and Cont != "N":
        print("Data Entry Error - enter Y for Yes or N for No.")
    elif Cont == "N":
        break