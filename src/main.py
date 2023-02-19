from djitellopy import Tello
import threading
import positioning

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    coords = [0.0, 0.0]
    threading.Thread(target=positioning.change_position, args=(coords, tello), daemon=True).start()
