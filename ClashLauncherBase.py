import os, requests, subprocess, sys

API_PATH = 'https://corporateclash.net/api/v1/login/'       # the API path given by Corporate Clash
APP_PATH = r'C:\Users\erich\AppData\Local\Corporate Clash'  # the location of the CorporateClash.exe game executable

TT_GS = ''  # Toontown Gameserver: a gameserver given by the login server to connect to
TT_CK = ''  # Toontown Cookie: a randomly generated cookie given by the login server to play

# a list of fields, containing USERNAME, and PASSWORD, respectively, with multiple slots, for multi-toon support
accounts = {
    '1':   ['',''],
    '2':   ['',''],
    '3':   ['',''],
    '4':   ['','']
}

# script can be run through command line with the following syntax
# CorporateClashBase.py ACCOUNT_NUMBER DISTRICT_NAME TOON_INDEX

# Ask for user input if no command line argument given, otherwise proceed with given login
if len(sys.argv) > 1:
    userInput = sys.argv[1]
else:
    userInput = input('Login with account ID: ')

# shorthands for district names, ease of access
def resolveDistrict(arg):
    districts = {
        "anvil"     :   "Anvil Acres",
        "cupcake"   :   "Cupcake Cove",
        "quicksand" :   "Quicksand Quarry",
        "tesla"     :   "Tesla Tundra",
        "highdive"  :   "High-Dive Hills",
        "hypno"     :   "Hypno Heights",
        "seltzer"   :   "Seltzer Summit",
        "kazoo"     :   "Kazoo Kanyon"
    }

    return districts.get(arg, "")

# if user specified a district in the command line, use it here
if len(sys.argv) > 2:
    district = resolveDistrict(sys.argv[2])
else:
    fuck = input('District select: ')
    district = resolveDistrict(fuck)

# if user specified a toon ID to force, use it here
if len(sys.argv) > 3:
    toon = sys.argv[3]
else:
    toon = input('Toon select: ')

USERNAME = accounts.get(userInput, ['',''])[0]
PASSWORD = accounts.get(userInput, ['',''])[1]

if USERNAME == '':
    print('Invalid input given. Terminating.')
    sys.exit(1)

response = requests.post(API_PATH + USERNAME, data = {'password': PASSWORD}).json()

if response['status']:
    # Good response from the login server
    TT_GS = 'gs.corporateclash.net'
    TT_CK = response['token']

    print('Login success. Server gave token ' + TT_CK + ' (' + str(response['friendlyreason']) + ')')

    subprocess.run(APP_PATH + r'\CorporateClash.exe', cwd = APP_PATH, env = dict(os.environ, TT_GAMESERVER = TT_GS, TT_PLAYCOOKIE = TT_CK, FORCE_TOON_SLOT = toon, FORCE_DISTRICT = district))
    sys.exit(0)
else:
    # Bad response from the server, results print
    print('Login failed. Server gave us status ' + str(response['reason']) + ' (' + str(response['friendlyreason']) + ')')
    sys.exit(2)