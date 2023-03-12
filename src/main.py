from djitellopy import Tello
from threading import Thread
import positioning
from messages import *

def run_drone(send_to_robot: DroneMessage, recieve_from_robot: RobotMessage):
    tello = Tello()
    tello.connect()

    drone_coords = (0.0, 0.0)
    Thread(target=positioning.change_position, args=(drone_coords, tello), daemon=True).start()
def run_robot(send_to_drone: RobotMessage, recieve_from_drone: DroneMessage):
    None

if __name__ == '__main__':
    drone_message = DroneMessage()
    robot_message = RobotMessage()
    Thread(target=run_drone, args=(drone_message, robot_message,))
    Thread(target=run_robot, args=(robot_message, drone_message,))
