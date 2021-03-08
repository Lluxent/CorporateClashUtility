import enum, time

class BattleState(enum.Enum):
    battle = 20         # default state, seeing the gag select screen, etc.
    targetEnemy = 21    # choosing a suit to target
    targetAlly = 22     # choosing a toon to target
    cancelable = 23     # after target selection, able to cancel ('waiting for other players' state)

    speedchat = 30

_state = BattleState.battle
_previousState = BattleState.battle

def updateState(newState=BattleState.battle):
    "Update the current state to another state."
    global _state
    global _previousState
    if newState == _state:
        return    
    _previousState = _state
    _state = newState
    print('State: Changed to ' + newState.name)

import pyautogui as ag, pygetwindow as gw

try:
    Client = gw.getWindowsWithTitle('Corporate Clash Beta')[0]
    Client.maximize()

    WINDOW_WIDTH = Client.width
    WINDOW_HEIGHT = Client.height
    WINDOW_XPOS = Client.left
    WINDOW_YPOS = Client.top
except IndexError:
    print('No Corporate Clash clients detected. Is the game running?')
    quit()

def moveCursor(xPercent, yPercent, click):
    "Moves the mouse to a specified location on the game screen, using percentages as parameters (0 is entirely left, 1 is entirely right; likewise vertically) with an optional click afterwards."
    ag.moveTo(WINDOW_XPOS + (xPercent * WINDOW_WIDTH), WINDOW_XPOS + (yPercent * WINDOW_HEIGHT))

    if click:
        time.sleep(0.1)
        ag.click()

Actions = { # an action is defined by coordinates to select, then the next state to transition to
    # gag name        X       Y            state
    'feather'   :   [0.380, 0.345, BattleState.targetAlly],
    'megaphone' :   [0.415, 0.345, BattleState.cancelable], # cancelable is used for group target gags, since no targeting is required
    'lipstick'  :   [0.450, 0.345, BattleState.targetAlly],
    'bamboo'    :   [0.490, 0.345, BattleState.cancelable],
    'pixie'     :   [0.525, 0.345, BattleState.targetAlly],
    'juggling'  :   [0.560, 0.345, BattleState.cancelable],
    'cannon'    :   [0.600, 0.345, BattleState.targetAlly],
    'high dive' :   [0.635, 0.345, BattleState.cancelable],

    'banana'        :   [0.380, 0.390, BattleState.targetEnemy],
    'rake'          :   [0.415, 0.390, BattleState.targetEnemy],
    'spring board'  :   [0.450, 0.390, BattleState.targetEnemy],
    'marbles'       :   [0.490, 0.390, BattleState.targetEnemy],
    'quicksand'     :   [0.525, 0.390, BattleState.targetEnemy],
    'trapdoor'      :   [0.560, 0.390, BattleState.targetEnemy],
    'wrecking'      :   [0.600, 0.390, BattleState.targetEnemy],
    'tnt'           :   [0.635, 0.390, BattleState.targetEnemy],

    'one'           :   [0.380, 0.435, BattleState.targetEnemy],
    'small magnet'  :   [0.415, 0.435, BattleState.cancelable],
    'five'          :   [0.450, 0.435, BattleState.targetEnemy],
    'big magnet'    :   [0.490, 0.435, BattleState.cancelable],
    'ten'           :   [0.525, 0.435, BattleState.targetEnemy],
    'hypno'         :   [0.560, 0.435, BattleState.cancelable],
    'fifty'         :   [0.600, 0.435, BattleState.targetEnemy],
    'presentation'  :   [0.635, 0.435, BattleState.cancelable],

    'kazoo'     :   [0.380, 0.485, BattleState.cancelable],
    'bike horn' :   [0.415, 0.485, BattleState.cancelable],
    'whistle'   :   [0.450, 0.485, BattleState.cancelable],
    'bugle'     :   [0.490, 0.485, BattleState.cancelable],
    'aoogah'    :   [0.525, 0.485, BattleState.cancelable],
    'trunk'     :   [0.560, 0.485, BattleState.cancelable],
    'fog'       :   [0.600, 0.485, BattleState.cancelable],
    'opera'     :   [0.635, 0.485, BattleState.cancelable],

    'squirt flower' :   [0.380, 0.535, BattleState.targetEnemy],
    'water glass'   :   [0.415, 0.535, BattleState.targetEnemy],
    'squirt gun'    :   [0.450, 0.535, BattleState.targetEnemy],
    'water balloon' :   [0.490, 0.535, BattleState.targetEnemy],
    'seltzer'       :   [0.525, 0.535, BattleState.targetEnemy],
    'hose'          :   [0.560, 0.535, BattleState.targetEnemy],
    'storm'         :   [0.600, 0.535, BattleState.targetEnemy],
    'geyser'        :   [0.635, 0.535, BattleState.targetEnemy],    

    'buzzer'    :   [0.380, 0.580, BattleState.targetEnemy],
    'rug'       :   [0.415, 0.580, BattleState.targetEnemy],
    'balloon'   :   [0.450, 0.580, BattleState.targetEnemy],
    'battery'   :   [0.490, 0.580, BattleState.targetEnemy],
    'taser'     :   [0.525, 0.580, BattleState.targetEnemy],
    'tv'        :   [0.560, 0.580, BattleState.targetEnemy],
    'tesla'     :   [0.600, 0.580, BattleState.targetEnemy],
    'lightning' :   [0.635, 0.580, BattleState.targetEnemy],       

    # imagine having throw
    'cupcake'               :   [0.380, 0.625, BattleState.targetEnemy],
    'fruit pie slice'       :   [0.415, 0.625, BattleState.targetEnemy],
    'cream pie slice'       :   [0.450, 0.625, BattleState.targetEnemy],
    'birthday cake slice'   :   [0.490, 0.625, BattleState.targetEnemy],
    'whole fruit pie'       :   [0.525, 0.625, BattleState.targetEnemy],
    'cream'                 :   [0.560, 0.625, BattleState.targetEnemy],
    'birthday'              :   [0.600, 0.625, BattleState.targetEnemy],
    'wedding'               :   [0.635, 0.625, BattleState.targetEnemy],       

    'flower pot'    :   [0.380, 0.675, BattleState.targetEnemy],
    'sandbag'       :   [0.415, 0.675, BattleState.targetEnemy],
    'bowling ball'  :   [0.450, 0.675, BattleState.targetEnemy],
    'anvil'         :   [0.490, 0.675, BattleState.targetEnemy],
    'weight'        :   [0.525, 0.675, BattleState.targetEnemy],
    'safe'          :   [0.560, 0.675, BattleState.targetEnemy],
    'boulder'       :   [0.600, 0.675, BattleState.targetEnemy],
    'piano'         :   [0.635, 0.675, BattleState.targetEnemy],

    'sue'   :   [0.235, 0.605, BattleState.targetEnemy],
    'fire'  :   [0.235, 0.665, BattleState.targetEnemy],
    'pass'  :   [0.235, 0.375, BattleState.cancelable],

    'back'  :   [0.500, 0.650, BattleState.battle],
    'lock'  :   [0.580, 0.575, BattleState.cancelable],

    'say'   :   [0.023, 0.059, BattleState.speedchat]
}

Targets = {
    # 4 cogs
    'far left'  :   .3,
    'mid left'  :   .435,   # also acts as 'left' in 2 cog sets
    'mid right' :   .565,   # also acts as 'right' in 2 cog sets
    'far right' :   .7,
    # 3 cogs
    'left'      :   .365,
    'middle'    :   .5,
    'right'     :   .635,

    'back'  :   None
}

def doAction(param='back'):
    "Process an action, passed by a single string. Depending on the current state, a valid action will be chosen, or nothing happens."
    if param in Actions and _state in (BattleState.battle, BattleState.cancelable):
        print('Action: Trying \'' + param + '\'...')
        var = Actions.get(param)

        if var[0] != None and var[1] != None:
            moveCursor(var[0], var[1], True)
        updateState(var[2])
    elif param in Targets and _state in (BattleState.targetAlly, BattleState.targetEnemy):
        print('Target: Trying \'' + param + '\'...')
        var = Targets.get(param)

        if param == 'back':
            moveCursor(Actions.get('back')[0], Actions.get('back')[1], True)
            updateState(BattleState.battle)
            return
        elif _state == BattleState.targetAlly:
            moveCursor(var, 0.675, True)
        else:
            moveCursor(var, 0.325, True)
        updateState(BattleState.cancelable)
        return
    elif _state == BattleState.speedchat:
        print('Sending \'' + param + '\' to Speedchat')
        moveCursor(0.023, 0.059, True)
        ag.write(param)
        ag.press('enter')        
        updateState(_previousState)
    else:
        print('Action \'' + param + '\' not found. Skipping...')
    return

while(True):
    x = input('> ')
    doAction(x)
