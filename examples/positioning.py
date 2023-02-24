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
        coords[0] += tello.get_speed_x() * TIME_INTERVAL
        coords[1] += tello.get_speed_y() * TIME_INTERVAL

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    coords = [0.0, 0.0]
    threading.Thread(target=change_position, args=(coords, tello), daemon=True).start()

    tello.takeoff()
    print(coords)

    decrement: int = 50
    initial: int = 280
    num_moves: int = 10
    for i in range(num_moves):
        decrement_factor: int = i // 2
        move_distance: int = initial - (decrement * decrement_factor)
        if i % 2 == 0:
            tello.move_forward(move_distance)
        else:
            tello.move_back(move_distance)

        print(coords)
    
    tello.land()
