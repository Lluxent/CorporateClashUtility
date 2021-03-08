import control as c, keyboard as k, mouse as m, time

_position = [0, 0]          # which gag we are currently on, [gag level, gag track]

UPPER_BOUND = 7
LOWER_BOUND = 0

INTERVAL_DURATION = 0.01    # time in seconds for the program to wait between button presses

def move(direction=''):
    global _position

    if direction == 'right':
        if _position[0] < UPPER_BOUND:
            _position[0] += 1
    elif direction == 'left':
        if _position[0] > LOWER_BOUND:
            _position[0] -= 1
    elif direction == 'up':
        if _position[1] > LOWER_BOUND:
            _position[1] -= 1
    elif direction == 'down':
        if _position[1] < UPPER_BOUND:
            _position[1] += 1
    else:
        return

    item = list(c.Actions.items())[(_position[1] * 8) + _position[0]]

    print('GamepadHelper: Moved to \'' + item[0] + '\'.')
    c.moveCursor(item[1][0], item[1][1], False)    

while(True):
    if k.is_pressed('left'):
        move('left')
        time.sleep(INTERVAL_DURATION)
    elif k.is_pressed('up'):       
        move('up')
        time.sleep(INTERVAL_DURATION)        
    elif k.is_pressed('right'):
        move('right')
        time.sleep(INTERVAL_DURATION)        
    elif k.is_pressed('down'):
        move('down')
        time.sleep(INTERVAL_DURATION)        
    elif m.is_pressed('left'):
        print('GamepadHelper: Click Registered')
        time.sleep(INTERVAL_DURATION * 20)       
    elif k.is_pressed('esc'):
        print('GamepadHelper: Terminating...')
        quit()
