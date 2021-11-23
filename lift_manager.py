import time
from lift import Lift


class Lift_Manager:

    def move_lift(floor):
        while (Lift.current_floor != floor):
            if (Lift.current_floor > floor):
                Lift.current_floor -= 1
            else:
                Lift.current_floor += 1
            time.sleep(1)
            print(f"You are on {Lift.current_floor} floor")


print("You are at your floor")
print(Lift.open_door())
time.sleep(3)
print(Lift.close_door())


def go_to_ground_level():
    Lift.current_floor = 0
