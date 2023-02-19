from djitellopy import Tello
import sys
import threading

sys.path.insert(0, './src')
import positioning

def move_in_direction(tello: Tello, direction: str, distance: int):
    if direction == 'right':
        tello.move_right(distance)
    elif direction == 'left':
        tello.move_left(distance)
    else:
        print('Error: invalid direction')
def flip_direction(direction: str) -> str:
    if direction == 'left':
        return 'right'
    else:
        return 'left'
if __name__ == '__main__':
    HORIZONTAL_MOVEMENT: int = 3 # total movements to perform horizontally (must be odd)
    VERTICAL_MOVEMENT: int = 9 # total movements to perform vertically
    MOVE_INTERVAL: int = 25 # interval to move for searching in centimeters (>=20)
    SEARCH_ATTEMPTS: int = 3 # number of searches to conduct each movement
    START_DIRECTION = 'left' # direction to start moving, either left or right
    SPEED: int = 80

    pad_ids = {} # used for recording coordinates of each pad

    tello = Tello()
    tello.connect()
    tello.enable_mission_pads()
    tello.set_speed(SPEED)

    coords = [0.0, 0.0]
    threading.Thread(target=positioning.change_position, args=(coords, tello,), daemon=True).start()

    tello.takeoff()

    cur_direction = START_DIRECTION
    # Initialize position
    move_in_direction(tello, cur_direction, MOVE_INTERVAL * (HORIZONTAL_MOVEMENT // 2))

    for i in range(VERTICAL_MOVEMENT):
        tello.move_forward(MOVE_INTERVAL)
        cur_direction = flip_direction(cur_direction)
        for j in range(HORIZONTAL_MOVEMENT):
            pad_id = -1
            for _ in range(SEARCH_ATTEMPTS):
                pad_id = tello.get_mission_pad_id()
                if (pad_id != -1):
                    break
            if pad_id != -1:
                if not (pad_id in pad_ids):
                    # logging
                    print('found:', pad_id)

                    pad_coords = (coords[0] + tello.get_mission_pad_distance_x(), coords[1] + tello.get_mission_pad_distance_y())
                    pad_ids[pad_id] = pad_coords
            if j < SEARCH_ATTEMPTS - 1:
                move_in_direction(tello, cur_direction, MOVE_INTERVAL)

        # logging
        print('all found:', pad_ids)
    
    tello.land()
