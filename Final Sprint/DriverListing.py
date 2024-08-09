import datetime
import FormatValues as fv

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

    # Ask if the user wants to add another customer
    while True:
        anotherDriver = input("\nDo you want to another driver financial listing? (Y/N): ").upper()
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