from djitellopy import Tello

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    tello.takeoff()
    tello.move_up(20)

    tello.flip_forward()
    tello.flip_left()
    tello.flip_back()
    tello.flip_right()

    tello.land()
