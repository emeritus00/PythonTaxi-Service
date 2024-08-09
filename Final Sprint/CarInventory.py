import datetime

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
