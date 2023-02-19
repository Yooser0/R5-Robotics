from djitellopy import Tello
import time
import threading

def change_position(coords: list[float], tello: Tello):
    """ Function to change the given coordinates'
    positions every time interval. Meant to be
    called through a thread daemon at the beginnning
    of the program when the drone is still.
    Note: Z-axis movement (up and down) is not
    calculated due to inconsistent velocity readings
    from the drone.
    """
    TIME_INTERVAL = 0.01
    UNITS_TO_CENT_X = -10.7
    UNITS_TO_CENT_Y = 10.7

    while (True):
        time.sleep(TIME_INTERVAL)

        # Integral approximation using addition of parts
        coords[0] += (tello.get_speed_x() * UNITS_TO_CENT_X) * TIME_INTERVAL
        coords[1] += (tello.get_speed_y() * UNITS_TO_CENT_Y) * TIME_INTERVAL

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    coords = [0.0, 0.0]
    threading.Thread(target=change_position, args=(coords, tello), daemon=True).start()

    time.sleep(3)
    print(coords)

    for _ in range(6):
        time.sleep(13)
        print(coords)
