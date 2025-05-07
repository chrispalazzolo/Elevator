"""
File: elevator_controller.py

Author: Chris Palazzolo
Date: 5/5/2025

Description:
An app to simulate an elevator by traveling to list of given floors and tracks
the floors visited and the time it took.

Assumptions:
- Floors should be a value of 1 or greater.
- Elevator car will move at constant speed from start to end.
- Elevator will only have one car.
- No direction commands, up or down buttons will not be used.
- The car will visit floors based on order received.

Features not added:
- Allow for basement floors, any floor below 1, such as -1, -2, -3, etc.
- Limits on how high floors can go, such as limit floors to 163 (Burj Khalifa), but then again... space elevator!
- Have an option to make the time traveled to floor efficient as possible.
- Ability to add more cars to split the floors list.

"""

import sys
import array
import pytest
from elevator_car import ElevatorCar

def get_args():
    arg_start_floor = 0
    arg_floor_list = 0
    e_prefix = "Error: Argument: "

    # Check to make sure the right amount of arguments, file name (default), start floor, floors to visit
    if len(sys.argv) < 3:
        sys.exit(e_prefix + "Missing Arguments, Args: start floor and floors")
        
    try:
        # Get starting floor argument and convert from string to int.
        arg_start_floor = int(sys.argv[1])

        # Check if starting floor, if equal to 0, then exit, floor can not be 0.
        if arg_start_floor < 0:
            sys.exit(e_prefix + "Starting floor value can not be less than 1.")

        # Get and split list of floors,.
        arg_floor_list = []
        floors = sys.argv[2].split(",")
        for num in floors:
            num = int(num)

            # Check if starting floor, if equal to 0, then exit, floor can not be 0.
            if num < 0:
                sys.exit(e_prefix + "Floor value can not be less than 1.")

            # Add floor to list    
            arg_floor_list.append(num)

    # If exception, exit app reporting error     
    except ValueError as x:
        sys.exit(e_prefix + str(x))
        
    return arg_start_floor, arg_floor_list

# Function main - Run program 
def main():
    start_floor, floors = get_args()
    default_speed = 10

    # Create elevator car object
    elev_car = ElevatorCar("Car_1", default_speed, start_floor)

    # Move car to the floors provided in args
    elev_car.go_to_floors(floors)

    # Display final time traveled and floors visited.
    print(elev_car.total_travel_time, ",".join(map(str, elev_car.floors_visited)))


# Run script as the main program
if __name__ == "__main__":
    main()
