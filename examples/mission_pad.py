from djitellopy import Tello

# Two states: one is searching for pad, two is landing on pad
if __name__ == '__main__':
    LAND_DIST: int = 4 # distance the drone is allowed to be away from the pad
    FLY_HEIGHT: int = 45
    MIN_HEIGHT: int = 30 # minimum height allowed to fly, determined by VPS
    SPEED: int = 80
    MOVE_INTERVAL: int = 40 # interval to move for searching in centimeters
    SEARCH_ATTEMPTS: int = 3 # number of searches to conduct each movement
    LAND_ATTEMPTS: int = 2 # number of pad positionings to attempt

    tello = Tello()
    tello.connect()
    tello.enable_mission_pads()
    tello.set_speed(SPEED)

    tello.takeoff()
    
    # 1. Search for pad
    state_loop = ['left', 'forward', 'right', 'right', 'forward', 'left']
    i = 0

    found_pad = False
    pad_id = -1
    for _ in range(SEARCH_ATTEMPTS):
        pad_id = tello.get_mission_pad_id()
        if (pad_id != -1):
            found_pad = True
    while (not found_pad):
        # Search operation
        if (i >= len(state_loop)):
            i = 0
        move_direction = state_loop[i]
        if (move_direction == 'left'):
            tello.move_left(MOVE_INTERVAL)
        elif (move_direction == 'forward'):
            tello.move_forward(MOVE_INTERVAL)
        elif (move_direction == 'right'):
            tello.move_right(MOVE_INTERVAL)
        i += 1

        for _ in range(SEARCH_ATTEMPTS):
            pad_id = tello.get_mission_pad_id()
            if (pad_id != -1):
                found_pad = True
    # 2. Land on pad
    for _ in range(LAND_ATTEMPTS):
        tello.go_xyz_speed_mid(0, 0, MIN_HEIGHT, SPEED, pad_id)
        
    tello.land()
