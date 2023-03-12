from enum import Enum, auto
from copy import copy
from utilities import QRCodeType

class DroneMessageType(Enum):
    BoxCoordinates = auto()
    Landing = auto()
    TookOff = auto()
class DroneMessage:
    message: DroneMessageType
    box_coordinates: list()
    def __init__(self):
        self.message = None
        self.box_coordinates = None
    def __init__(self, message: DroneMessageType):
        self.message = message
        self.box_coordinates = None
    def __init__(self, box_coordinates: list()):
        self.message = DroneMessageType.BoxCoordinates
        self.box_coordinates = list(box_coordinates)

class RobotMessageType(Enum):
    QRCode = auto()
    TouchNGo = auto()
class RobotMessage:
    message: RobotMessageType
    qr_code: QRCodeType
    def __init__(self):
        self.message = None
        self.qr_code = None
    def __init__(self, message: RobotMessageType):
        self.message = copy(message)
        self.qr_code = None
    def __init__(self, qr_code: QRCodeType):
        self.message = RobotMessageType.QRCode
        self.qr_code = copy(qr_code)
