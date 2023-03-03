from djitellopy import Tello

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    tello.takeoff()
    tello.land()
