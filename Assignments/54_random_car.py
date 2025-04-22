import random

def drive_car(selectedCar):
    print("I am going for a drive with my " + str(selectedCar))

def select_car():
    dream_garage = ['Ford F-250', 'Ford F-150 Super', 'Ford F-350', 'John Deer 1600 Turbo TerrainCut™','Icon A5']
    x = random.randint(0,4)
    if x == 0:
        drive_car(dream_garage[0])
    if x == 1:
        drive_car(dream_garage[1])
    if x == 2:
        drive_car(dream_garage[2])
    if x == 3:
        drive_car(dream_garage[3])
    if x == 4:
        drive_car(dream_garage[4])
    else:
        return

        
select_car()
