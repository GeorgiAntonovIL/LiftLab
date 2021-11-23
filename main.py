import time


# I had a problem with the imports so i dumped all the classes in one file
class Lift:
    current_floor = 0

    @classmethod
    def open_door(cls):
        print("Door is open")

    @classmethod
    def close_door(cls):
        print("Door is closed")


class Lift_Manager:

    def move_lift(floor):

        while Lift.current_floor != floor:
            if Lift.current_floor > floor:
                Lift.current_floor -= 1
            else:
                Lift.current_floor += 1
            time.sleep(1)
            print(f"You are on {Lift.current_floor} floor")

        print("You are at your floor")
        Lift.open_door()
        time.sleep(3)
        Lift.close_door()


class Control_Panel:

    def call_cabin(self, floor):
        Lift_Manager.move_lift(floor)


class Inner_CP(Control_Panel):
    pass


class Outer_CP(Control_Panel):
    pass


def run_method():
    ground_level = Outer_CP()
    outer_1 = Outer_CP()
    outer_2 = Outer_CP()
    outer_3 = Outer_CP()
    outer_4 = Outer_CP()
    outer_5 = Outer_CP()
    inner = Inner_CP()

    inner.call_cabin(3)
    outer_1.call_cabin(1)
    inner.call_cabin(2)
    outer_5.call_cabin(5)
    inner.call_cabin(0)


if __name__ == '__main__':
    run_method()
