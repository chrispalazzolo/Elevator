"""
Class File: elevator_car.py
App File: elevator_app.py

Author: Chris Palazzolo
Date: 5/5/2025

Description:
A class to instantiate elevator cars for the elevator_app.  The elevator car will keep track of floors
traveled and how long it took to travel all given floors.

Inital arguments:
name: A name for the elevator car.
speed: The value it takes for the car to move per floor.
start_floor: The floor the elevator car will start from.
"""

class ElevatorCar:
    def __init__(self, name, speed, start_floor):
        self.name = name
        self.speed = speed
        self.start_floor = start_floor

        # After caller defined values have been set, call set_defaults() method to finish initializing
        self.set_defaults()

    # Method to set default values and inital setup
    def set_defaults(self):
        self.current_floor = self.start_floor
        self.floors_visited = [self.start_floor]
        self.total_travel_time = 0

    # Method that moves the car to a given floor
    def go_to_floor(self, next_floor):

        # Check to see if car is already at the floor being requested to move to.
        if self.current_floor != next_floor:
            # Get a count of how many floors the car moved, abs() because car can't move negative floors.
            floors_traveled = abs(self.current_floor - next_floor)

            # Get the time traveled by multiplying the number of floors by car speed, then add it to total.
            self.total_travel_time += floors_traveled * self.speed

            # Update the car's current floor to the floor car just moved to then add it to the floors visited list.
            self.current_floor = next_floor
            self.floors_visited.append(next_floor)

    # Method that takes a list of floors and moves the car to each floor.
    def go_to_floors(self, floors):
        # Iterate through floors list and call method go_to_floor with each floor.
        for floor in floors:
            self.go_to_floor(floor)

    # Method to reset the car back to when it was first created.
    def reset(self):
        self.set_defaults()
