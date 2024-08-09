import datetime

f = open('Defaults.dat', 'r')

NEXT_TRANSACTION_NUM = int(f.readline())
NEXT_DRIVER_NUM = int(f.readline())
MONTHLY_STAND_FEE = float(f.readline())
DAILY_RENTAL_FEE = float(f.readline())
WEEKLY_RENTAL_FEE = float(f.readline())
HST_RATE = float(f.readline())
NEXT_INVOICE_NUM = int(f.readline())
f.close()

# Check if it's the first day of the month
# today = datetime.date.today()
todayStr = "2024-06-01" # for testing
today = datetime.datetime.strptime(todayStr, "%Y-%m-%d")

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
        # BONUS: Implement code to update balance due in text file

            count += 1
            NEXT_TRANSACTION_NUM += 1

    employeeFile.close()

f = open('Defaults.dat', 'w')
f.write("{}\n".format(str(NEXT_TRANSACTION_NUM)))
f.write("{}\n".format(str(NEXT_DRIVER_NUM)))
f.write("{}\n".format(str(MONTHLY_STAND_FEE)))
f.write("{}\n".format(str(DAILY_RENTAL_FEE)))
f.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(NEXT_INVOICE_NUM)))
f.close()

print("Balance due be updated in the employee table")
print(count)
