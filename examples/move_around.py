from djitellopy import Tello

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    tello.takeoff()
    tello.move_up(20)

    tello.move_forward(20)
    tello.move_right(20)

    tello.move_down(20)

    tello.move_back(20)
    tello.move_left(20)

    tello.move_up(20)

    tello.land()
