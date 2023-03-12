from djitellopy import Tello
import time
import threading

def change_position(coords: tuple[float, float], tello: Tello):
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
def distance(prev_coords: tuple[float, float], coords: tuple[float, float]) -> tuple[float, float]:
    return (coords[0] - prev_coords[0], coords[1] - prev_coords[1])

if __name__ == '__main__':
    tello = Tello()
    tello.connect()

    coords = (0.0, 0.0)
    threading.Thread(target=change_position, args=(coords, tello), daemon=True).start()

    tello.takeoff()
    print(coords)
    prev_coords = tuple(coords)

    DECREMENT: int = 50
    INITIAL: int = 280
    NUM_MOVES: int = 12
    for i in range(NUM_MOVES):
        decrement_factor: int = i // 2
        move_distance: int = INITIAL - (DECREMENT * decrement_factor)
        if i % 2 == 0:
            tello.move_forward(move_distance)
        else:
            tello.move_back(move_distance)

        print(coords)
        prev_coords = tuple(coords)
    
    tello.land()
