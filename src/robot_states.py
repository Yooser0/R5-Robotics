from djitellopy import Tello
from enum import Enum, auto

class RobotState(Enum):
    MovingToFirstBox = auto()
    EnteringBox = auto()
    ScanningQRCode = auto()
    ExitingBox = auto()
    WaitingForCoords = auto()
    MovingToBox = auto()
    # AvoidingPoison = auto() # implementation to be determined
