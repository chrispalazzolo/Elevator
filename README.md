A fun application which simulates an elevator.

Inputs:
Arg1: Starting floor -> The floor you want the elevator to start 
Arg2: Floors to visit -> A list of floors the elevator needs to visit during operation

example: python elevator_controller.py 1 2,4,6,8

Output:
Total time -> Gives the total time the elevator's travel to each floor
Floors visited -> Lists, in order, of all floors the elevator visited

example: "70 1,2,4,6,8"

To run pytest file: test_elevator_car.py
If needed, install pytest : pip install -U pytest
Run test with command: pytest -v <dir>test_elevator_car.py
