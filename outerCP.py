from control_panel import Control_Panel
from lift_manager import Lift_Manager


class Outer_CP(Control_Panel):

    def call_cabin(self, floor):
        Lift_Manager().move_lift(floor)
