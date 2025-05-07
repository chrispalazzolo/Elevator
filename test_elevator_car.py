"""
Test File: test_elevator_car

Author: Chris Palazzolo
Date: 5/6/2025

Description:
A test file which tests the ElevatorCar class.

Run Command: pytest -v test_elevator_car.py
"""

import pytest
from elevator_car import ElevatorCar

# Test moving the car one floor.
def test_floor_movement():
    # Test values
    test_speed = 10
    test_start_floor = 1
    test_go_to_floor = 2

    # Test object
    car = ElevatorCar("TestCar", test_speed, test_start_floor)

    # Test action
    car.go_to_floor(test_go_to_floor)

    # Test assertions
    assert car.total_travel_time == 10
    assert car.current_floor == test_go_to_floor
    assert len(car.floors_visited) == 2
    assert test_start_floor in car.floors_visited
    assert test_go_to_floor in car.floors_visited

# Test moving the car to multiple floors.
def test_floor_list_movement():
    # Test values
    test_speed = 10
    test_start_floor = 1
    test_go_to_floors = [2,6,10]

    # Test object
    car = ElevatorCar("TestCar", test_speed, test_start_floor)

    # Test actions
    car.go_to_floors(test_go_to_floors)

    # Test assertions
    assert car.total_travel_time == 90
    assert car.current_floor == test_go_to_floors[-1]
    assert len(car.floors_visited) == (len(test_go_to_floors) + 1)
    assert test_start_floor in car.floors_visited
    
    for floor in test_go_to_floors:
        assert floor in car.floors_visited

# Test resetting elevator car back to initialization.    
def test_car_reset():
    # Test values
    test_speed = 10
    test_start_floor = 1
    test_go_to_floors = [2,6,10]

    # Test object
    car = ElevatorCar("TestCar", test_speed, test_start_floor)

    # Test actions
    car.go_to_floors(test_go_to_floors)
    car.reset()

    # Test assertions
    assert car.total_travel_time == 0
    assert car.start_floor == test_start_floor
    assert car.current_floor == test_start_floor
    assert len(car.floors_visited) == 1
    assert test_start_floor in car.floors_visited
