from enum import Enum, auto

MOVE_INTERVAL = [20, 500]
SPEED_INTERVAL = [10, 100]

class Move:
    distance: int
    speed: int
    def __init__(self, distance: int, speed: int):
        if distance < MOVE_INTERVAL[0] or distance > MOVE_INTERVAL[1]:
            raise "Distance out of bounds"
class GoMove:
    x: int
    y: int
    z: int
    speed: int
    def __init__(self, x: int, y: int, z: int, speed: int):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
class QRCodeType(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
    Done = auto()
class BoxType(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    F = auto()
