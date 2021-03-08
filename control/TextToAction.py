import pyautogui as ag
import pygetwindow as gw
import time

# this program assumes a resolution of 1920x1080
# TODO: fix that

Layout = {  # coordinates for all four clients
    0 : [-7,0],
    1 : [953,0],
    2 : [-7,520],
    3 : [953,520]
}

# get all active clients
Clients = gw.getWindowsWithTitle('Corporate Clash BETA')

if len(Clients) > 3:
    print('Max number of clients is 4.')
    quit

# for each active client, position them in a quadrant of the screen
for x in range(0, len(Clients)):
    Clients[x].resizeTo(974,527)    # all clients share the same size
    Clients[x].moveTo(Layout.get(x)[0], Layout.get(x)[1])

# moves the mouse to the position given, within relation to the top left of the given client
def moveMouseRelative(x, y, client):
    if client > len(Clients):
        print('Error, client index exceeds number of active clients.')

    ag.moveTo(Clients[client].left + x, Clients[client].top + y)
    time.sleep(0.1)
    ag.click()

gagSlots = [316,355,390,430,470,510,550,590]    # X coordinates on the gag battle screen
gagTracks = [160,185,210,235,265,290,315,345]   # Y coordinates on the gag battle screen

cogSlotsY = 225 # Y coordinate for choosing a cog
toonSlotsY = 0  # Y coordinate for choosing a toon

cogSlotsTwo = [435,535]
cogSlotsThree = [390,490,590]
cogSlotsFour = [335,435,535,635]

identifierTwo = ['left','right']
identifierThree = ['left','middle','right']
identifierFour = ['left','mid left','mid right','right']

healNames = ['feather','megaphone','lipstick','cane','dust','juggling','cannon','dive']
trapNames = ['banana','rake','spring','marbles','quicksand','trapdoor','ball','tnt']
lureNames = ['one','small','five','magnet','ten','hypno','fifty','presentation']
soundNames = ['kazoo','bike','whistle','bugle','aoogah','trunk','fog','opera']
squirtNames = ['flower','glass','squirtgun','water','seltzer','hose','storm','geyser']
zapNames = ['joybuzzer','rug','balloon','battery','taser','tv','tesla','lightning']
throwNames = ['cupcake','fruit','slice','bday','pie','cream','birthday','wedding'] #imagine using throw
dropNames = ['flowerpot','sandbag','bowlingball','anvil','weight','safe','boulder','piano']

gagArray = [healNames,trapNames,lureNames,soundNames,squirtNames,zapNames,throwNames,dropNames]

def chooseGag(gag, client):
    for x in range(len(gagArray)):
        for y in range(len(gagArray[x])):
            if gag.lower() == gagArray[x][y]:
                moveMouseRelative(gagSlots[y], gagTracks[x], client)
                break

numCogs = 4 # number of cogs in battle, change through updateCogs

def updateCogs(cogs):
    global numCogs
    
    numCogs = cogs
    print('Number of Cogs in battle updated to ' + str(numCogs))

def chooseTarget(target, client):
    if numCogs <= 1:
        print('Called chooseTarget, but there was only one cog.')
        return
    
    if numCogs > 4:
        print('Called chooseTarget, but there was more than four cogs???')
        return

    if numCogs == 2:
        if target.lower() == identifierTwo[0]:
            moveMouseRelative(cogSlotsTwo[0], cogSlotsY, client)
            return
        elif target.lower() == identifierTwo[1]:
            moveMouseRelative(cogSlotsTwo[1], cogSlotsY, client)
            return
        else:
            print('Called chooseTarget, but identifier ' + target + ' did not match (numCogs = 2).')
            return
    elif numCogs == 3:
        if target.lower() == identifierThree[0]:
            moveMouseRelative(cogSlotsThree[0], cogSlotsY, client)
            return
        elif target.lower() == identifierThree[1]:
            moveMouseRelative(cogSlotsThree[1], cogSlotsY, client)
            return
        elif target.lower() == identifierThree[2]:
            moveMouseRelative(cogSlotsThree[2], cogSlotsY, client)
            return            
        else:
            print('Called chooseTarget, but identifier ' + target + ' did not match (numCogs = 3).')
            return
    elif numCogs == 4:
        if target.lower() == identifierFour[0]:
            moveMouseRelative(cogSlotsFour[0], cogSlotsY, client)
            return
        elif target.lower() == identifierFour[1]:
            moveMouseRelative(cogSlotsFour[1], cogSlotsY, client)
            return
        elif target.lower() == identifierFour[2]:
            moveMouseRelative(cogSlotsFour[2], cogSlotsY, client)
            return            
        elif target.lower() == identifierFour[3]:
            moveMouseRelative(cogSlotsFour[3], cogSlotsY, client)
            return             
        else:
            print('Called chooseTarget, but identifier ' + target + ' did not match (numCogs = 3).')
            return            

# TODO: implement this list within the already implemented ones above
groupAttacks = ['megaphone','cane','juggling','dive','small','magnet','hypno','presentation','kazoo','bike','whistle','bugle','aoogah','trunk','fog','opera']

# returns True if a sound gag, or certain heal or lure gags
def isGroupAttack(gag):
    for x in range(len(groupAttacks)):
        if gag.lower() == groupAttacks[x]:
            return True
    
    return False

# the assumption is the string is:
# CLIENT GAG TARGET
def parseInput(value):
    if len(value) == 0:
        return

    preToken = value.split()

    if(preToken[0].lower() == 'cogs') and len(preToken) == 2:
        updateCogs(int(preToken[1]))
        return

    if len(preToken) == 2:
        tokens = [int(preToken[0]), preToken[1]]
        if numCogs == 1:
            chooseGag(tokens[1], tokens[0])
            return
        elif isGroupAttack(tokens[1]):
            chooseGag(tokens[1], tokens[0])
        else:
            print('Error, only two tokens, but gag used was not group, or there is more than one cog.')
            return
    elif len(preToken) == 3:
        tokens = [int(preToken[0]), preToken[1], preToken[2]]        
        chooseGag(tokens[1], tokens[0])
        chooseTarget(tokens[2], tokens[0])
        return
    elif len(preToken) == 4:
        tokens = [int(preToken[0]), preToken[1], preToken[2], preToken[3]]         
        chooseGag(tokens[1], tokens[0])
        chooseTarget(tokens[2] + ' ' + tokens[3], tokens[0]) 
        return    
    else:
        print('Error, invalid number of parameters.')
        return

# for debugging
def position():
    print(ag.position())

while(True):
    bruh = input('> ')
    parseInput(bruh)
