from djitellopy import Tello
from enum import Enum, auto
from utilities import BoxType

class DroneState(Enum):
    LiftingOff = auto()
    Scanning = auto()
    GoingToBox = auto()
    Landing = auto()
    # Poison = auto() # implementation to be determined

def lifting_off(tello: Tello):
    None
def scanning(tello: Tello, box_positions: list((BoxType, tuple[int, int])), terminate: bool):
    None
def going_to_box(tello: Tello, box_coordinates: tuple[int, int]):
    None
def landing(tello: Tello, robot_coordinates: tuple[int, int]):
    None
