'''
    const.py

    Gladius et Scutum - Jane Wharton

    
'''


MAX_TECH_LEVEL = 5

BLACK   = (0,0,0,)
GRAY    = (128,128,128,)
WHITE   = (255,255,255,)


    #-----------------------#
    #       ELEMENTS        #
    #-----------------------#

ELEM_AIR    =0
ELEM_WATER  =1
ELEM_FIRE   =2
ELEM_EARTH  =3

'''
    Element      Status
    ----------------------
    Air          Hypoxic
    Water        Softened
    Earth        Stunned
    Fire         Burning
'''



    #-----------------------#
    #       WEAPONS         #
    #-----------------------#

WPN_NONE        =0
WPN_JAVSHIELD   =1
WPN_HAMSHIELD   =2
WPN_SWODAGGER   =3
WPN_AXESHIELD   =4
WPN_WHIPROPE    =5
WPN_CHAKRAM     =6
WPN_SPEAR       =7
WPN_POLE        =8
WPN_NET         =9
WPN_SLING       =10

WEAPONS={
    WPN_NONE:{
        "name":"Unarmed",
    },
    WPN_JAVSHIELD:{
        "name":"Javelin & Shield",
        "speed":2,
        "to-hit":5,
        "evasion":10,
        "defense":1,
    },
    WPN_HAMSHIELD:{
        "name":"Hammer & Shield",
        "evasion":5,
        "damage":1,
        "pierce":1,
    },
    WPN_SWODAGGER:{
        "name":"Sword & Dagger",
        "speed":1,
        "short to-hit":10,
        "evasion":8,
        "short damage":1,
    },
    WPN_AXESHIELD:{
        "name":"Axe & Shield",
        "short speed":2,
        "short to-hit":5,
        "evasion":6,
        "damage":1,
    },
    WPN_WHIPROPE:{
        "name":"Whip & Rope",
        "wide speed":1,
        "wide to-hit":5,
        "evasion":2,
        "defense":-1,
        "short damage":2,
    },
    WPN_CHAKRAM:{
        "name":"Chakram",
        "short speed":3,
        "short to-hit":6,
        "evasion":10,
        "wide damage":1,
    },
    WPN_SPEAR:{
        "name":"Spear",
        "wide speed":2,
        "wide to-hit":10,
        "evasion":10,
        "wide damage":1,
    },
    WPN_POLE:{
        "name":"Pole",
        "wide speed":4,
        "short to-hit":-10,
        "evasion":4,
        "defense":1,
        "wide damage":1,
    },
    WPN_NET:{
        "name":"Net",
        "wide speed":3,
        "wide to-hit":15,
        "evasion":4,
        "defense":-1,
        "wide damage":1,
    },
    WPN_SLING:{
        "name":"Sling",
        "wide speed":5,
        "wide to-hit":5,
        "evasion":2,
        "defense":-1,
        "wide damage":2,
    }
}


ELEMENTS={
    "F":'fire',
    "E":'earth',
    "A":'air',
    "W":'water',
    }
TECHNIQUES={
'Firebolt': {'name': 'Firebolt', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 2, 'special': ''},
'Breath of Fire': {'name': 'Breath of Fire', 'element': 'F', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 10, 'status': 33, 'status-dur': 2, 'special': ''},
'Burning Touch': {'name': 'Burning Touch', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 90, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 25, 'status-dur': 3, 'special': ''},
'Ignition': {'name': 'Ignition', 'element': 'F', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 90, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 33, 'status': 67, 'status-dur': 4, 'special': ''},
'Fire Eater': {'name': 'Fire Eater', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 100, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Singe': {'name': 'Singe', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': 'Pierce 1'},
'Cannon Calves': {'name': 'Cannon Calves', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 65, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 50, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Speed +1 for 2 turns'},
'Rocket Punch': {'name': 'Rocket Punch', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 80, 'priority': 3, 'damage': 2, 'defense': 0, 'evasion': 5, 'short': 33, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Flame Whip': {'name': 'Flame Whip', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Whip & Rope', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 75, 'wide': 0, 'status': 50, 'status-dur': 2, 'special': ''},
'Burning Net': {'name': 'Burning Net', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 2, 'weapon': 'Net', 'sp': 3, 'nrg': 2, 'hit': 60, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 90, 'wide': 0, 'status': 33, 'status-dur': 4, 'special': 'Prevents enemy movement for 3 actions'},
'Combustion': {'name': 'Combustion', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Ignition', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 3, 'hit': 95, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': ''},
'Blue Fire': {'name': 'Blue Fire', 'element': 'F', 'mode': 'Both', 'pre-reqs': 'Firebolt', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 65, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 6, 'special': ''},
'Flamespray': {'name': 'Flamespray', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Breath of Fire', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 95, 'priority': 2, 'damage': 3, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 80, 'status-dur': 5, 'special': ''},
'Singing Grasp': {'name': 'Singing Grasp', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Burning Touch', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 1, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': ''},
'Shock': {'name': 'Shock', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 95, 'priority': 2, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': ''},
'Flaming Aura': {'name': 'Flaming Aura', 'element': 'F', 'mode': 'Both', 'pre-reqs': 'Fire Eater', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': 1, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'SHORT DMG +1 for 2 turns'},
'Burning Oil': {'name': 'Burning Oil', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Flamespray', 'req-skill': 8, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 65, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 4, 'special': ''},
'Lightning Bolt': {'name': 'Lightning Bolt', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Shock', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 90, 'priority': 6, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 3'},
'Targeted Combustion': {'name': 'Targeted Combustion', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Combustion', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 85, 'priority': -2, 'damage': 7, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Fire Whirl': {'name': 'Fire Whirl', 'element': 'F', 'mode': 'Both', 'pre-reqs': 'Flamespray', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 0, 'status': 75, 'status-dur': 4, 'special': ''},
'Static Grip': {'name': 'Static Grip', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Shock', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 95, 'priority': 2, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy movement for 3 actions'},
'Overdrive': {'name': 'Overdrive', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Flaming Aura', 'req-skill': 13, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 2, 'hit': 75, 'priority': -3, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 90, 'status-dur': 3, 'special': '90% chance target is Hypoxic for 3 actions'},
'Grind': {'name': 'Grind', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Harden': {'name': 'Harden', 'element': 'E', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 0, 'status-dur': 0, 'special': 'DFN +1 for 3 turns'},
'Rock Throw': {'name': 'Rock Throw', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 25, 'status-dur': 2, 'special': ''},
'Rockslide': {'name': 'Rockslide', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': -2, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 50, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Tunnel': {'name': 'Tunnel', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 95, 'priority': -3, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': ''},
'Sandstorm': {'name': 'Sandstorm', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 105, 'priority': 2, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy healing for 2 actions'},
'Drill': {'name': 'Drill', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 90, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 1'},
'Stone Smash': {'name': 'Stone Smash', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Rock Throw', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 85, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': ''},
'Fist of Stone': {'name': 'Fist of Stone', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 75, 'priority': 0, 'damage': 5, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 1'},
'Constrict': {'name': 'Constrict', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Grind', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 4, 'special': 'Pierce 1'},
'Pebblegun': {'name': 'Pebblegun', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Rock Throw', 'req-skill': 7, 'level': 2, 'weapon': 'Sling', 'sp': 2, 'nrg': 1, 'hit': 65, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 1, 'special': ''},
'Armorslayer': {'name': 'Armorslayer', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Drill', 'req-skill': 8, 'level': 2, 'weapon': 'J&S,H&S,S&D,A&S', 'sp': 2, 'nrg': 2, 'hit': 70, 'priority': -1, 'damage': 4, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 3; Only works if enemy has >= 1 Defense'},
'Vibrohammer': {'name': 'Vibrohammer', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Drill', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 25, 'status-dur': 3, 'special': '33% chance target is Softened for 3 actions'},
'Wall of Clay': {'name': 'Wall of Clay', 'element': 'E', 'mode': 'Both', 'pre-reqs': 'Harden', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 70, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': 'EVA +5 for 6 turns'},
'Tremor': {'name': 'Tremor', 'element': 'E', 'mode': 'Both', 'pre-reqs': 'Rockslide, Tunnel', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 90, 'priority': 3, 'damage': 3, 'defense': 0, 'evasion': 10, 'short': 75, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Rumble': {'name': 'Rumble', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Tremor', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 80, 'priority': 0, 'damage': 7, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 2, 'special': ''},
'Earthwave': {'name': 'Earthwave', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Tremor', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 85, 'priority': 0, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 2'},
'Diamond Smash': {'name': 'Diamond Smash', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Stone Smash, Fist of Stone', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 60, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 1'},
'Lockdown': {'name': 'Lockdown', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Constrict', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': -1, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy movement for 3 actions'},
'Meteor Smash': {'name': 'Meteor Smash', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Diamond Smash', 'req-skill': 16, 'level': 4, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 75, 'priority': -3, 'damage': 9, 'defense': -1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 3, 'special': ''},
'Suppressing Sands': {'name': 'Suppressing Sands', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Sandstorm', 'req-skill': 13, 'level': 4, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 95, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Clear all status effects on the target'},
'Breath of Wind': {'name': 'Breath of Wind', 'element': 'A', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 25, 'status': 33, 'status-dur': 3, 'special': ''},
'Pressure Bolt': {'name': 'Pressure Bolt', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Pillow of Winds': {'name': 'Pillow of Winds', 'element': 'A', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 17, 'status': 0, 'status-dur': 0, 'special': 'EVA +5 for 3 turns'},
'Compression Wave': {'name': 'Compression Wave', 'element': 'A', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 95, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 50, 'status-dur': 3, 'special': ''},
'Gust Punch': {'name': 'Gust Punch', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 70, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': '25% chance target is Stunned for 2 actions'},
'Double Image': {'name': 'Double Image', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 85, 'priority': 4, 'damage': 1, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Speed +1 for 4 turns'},
'Suffocate': {'name': 'Suffocate', 'element': 'A', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 2, 'special': 'Pierce 2; Prevents enemy healing for 2 actions'},
'Spiral Out': {'name': 'Spiral Out', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Breath of Wind', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 67, 'wide': 67, 'status': 0, 'status-dur': 0, 'special': ''},
'Cloud Clone': {'name': 'Cloud Clone', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Double Image', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 200, 'priority': -7, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Summon Cloud Clone to assist in combat. Does 1 Neutral Dmg / turn with 90% to-hit, and has 3 HP. When you are struck, divert damage to the Hologram instead. Can only cast once per battle. '},
'Obfuscate': {'name': 'Obfuscate', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Pillow of Winds', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 5, 'special': 'Pierce 1'},
'Disarming Gust': {'name': 'Disarming Gust', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Pressure Bolt', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 85, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Disarm 50%'},
'Shockwave': {'name': 'Shockwave', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Compression Wave', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 105, 'priority': 5, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 67, 'status': 67, 'status-dur': 5, 'special': ''},
'Submission': {'name': 'Submission', 'element': 'A', 'mode': 'Short', 'pre-reqs': 'Suffocate', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 75, 'priority': 1, 'damage': 3, 'defense': 1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': 'Prevents enemy movement for 2 actions'},
'Compression Bomb': {'name': 'Compression Bomb', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Gust Punch', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 70, 'priority': -2, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '50% chance target is Stunned for 3 actions'},
'Vacuum Chamber': {'name': 'Vacuum Chamber', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Submission', 'req-skill': 13, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 95, 'priority': -6, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 5, 'special': 'Pierce 6'},
'Vortex': {'name': 'Vortex', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Spiral Out, Disarming Gust', 'req-skill': 11, 'level': 3, 'weapon': 'Chakram', 'sp': 4, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 3, 'special': 'Disarm 75%'},
'Third Eye': {'name': 'Third Eye', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Cloud Clone', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'ACC +5 for 6 turns'},
'Dust Devils': {'name': 'Dust Devils', 'element': 'A', 'mode': 'Both', 'pre-reqs': 'Spiral Out', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 85, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'WIDE DMG +1 for 2 turns'},
'Bubble': {'name': 'Bubble', 'element': 'W', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 2, 'special': ''},
'Watergun': {'name': 'Watergun', 'element': 'W', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 50, 'status-dur': 2, 'special': ''},
'Wavecrash': {'name': 'Wavecrash', 'element': 'W', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 25, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': ''},
'Grab Weapon': {'name': 'Grab Weapon', 'element': 'W', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 80, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Disarm 33%'},
'Slippery Skin': {'name': 'Slippery Skin', 'element': 'W', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': 'EVA +10 for 3 turns'},
'Acid Rain': {'name': 'Acid Rain', 'element': 'W', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 100, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': '33% chance target is Burning for 6 actions'},
'Dissolve': {'name': 'Dissolve', 'element': 'W', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': -1, 'damage': 2, 'defense': -1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': ''},
'Wavesurf': {'name': 'Wavesurf', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Wavecrash', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 3, 'hit': 90, 'priority': 2, 'damage': 3, 'defense': 1, 'evasion': 5, 'short': 33, 'wide': 0, 'status': 83, 'status-dur': 2, 'special': ''},
'Jet Stream': {'name': 'Jet Stream', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Watergun', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': 'Pierce 1 while Short'},
'Shield': {'name': 'Shield', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Bubble', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 1, 'damage': 1, 'defense': 2, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
'Liquefy': {'name': 'Liquefy', 'element': 'W', 'mode': 'Short', 'pre-reqs': 'Slippery Skin', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -1, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 75, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': 'DFN +1 for 3 turns'},
'Cold Knuckle': {'name': 'Cold Knuckle', 'element': 'W', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 80, 'priority': 1, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': ''},
'Heal': {'name': 'Heal', 'element': 'W', 'mode': 'Both', 'pre-reqs': '', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -2, 'damage': 0, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 1 HP/turn for 4 turns'},
'Downpour': {'name': 'Downpour', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Acid Rain', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 105, 'priority': 2, 'damage': 1, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 3, 'special': ''},
'Bubble Bomb': {'name': 'Bubble Bomb', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Shield', 'req-skill': 8, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 80, 'priority': 0, 'damage': 5, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 0, 'status': 25, 'status-dur': 3, 'special': ''},
'Icicle': {'name': 'Icicle', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Cold Knuckle', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 75, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 5, 'special': 'Pierce 2'},
'Mend': {'name': 'Mend', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Heal', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 200, 'priority': -3, 'damage': 0, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 5 HP; can only use once per turn'},
'Mana Rain': {'name': 'Mana Rain', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Downpour', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 1 SP/turn for 6 turns'},
'Purify': {'name': 'Purify', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Heal', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -9, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Clear status effects on the caster'},
'Pressure Beam': {'name': 'Pressure Beam', 'element': 'W', 'mode': 'Short', 'pre-reqs': 'Jet Stream', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 85, 'priority': -2, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': 'Pierce 2'},
'Frostbite': {'name': 'Frostbite', 'element': 'W', 'mode': 'Both', 'pre-reqs': 'Icicle', 'req-skill': 13, 'level': 4, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 65, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 83, 'status-dur': 6, 'special': '50% chance target is Burning for 6 actions'},
'Attack': {'name': 'Attack', 'element': '', 'mode': 'both', 'pre-reqs': '', 'req-skill': 0, 'level': 0, 'weapon': 'Any', 'sp': 0, 'nrg': 1, 'hit': 50, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': ''},
}


BOONS={
    # A boon requires 1 energy to use, however, after a boon is used,
        # both combatants recover all 3 energy again.
        # Boons cannot be spammed, however, as you cannot use a boon
        # two turns in a row. You will be booed for that and denied --
        # people want to see *some* legit fighting, but will tolerate
        # some "cheating" here and there.
    # Boons can be bought with Favor Points, and each has a certain cost.
        # (Favor Points are earned from fulfilling specific random requirements
        #   for each battle.)
    # Boons also have a Level requirement, and cannot be bought until the player
    # has reached the appropriate tournament Level.
    "Reset":{"level":1, "favor-cost": 1,
        "description":'''Set combatants to Wide position.''',
        },
    "Spring Water L1":{"level":5, "favor-cost": 2,
        "description":'''Heal 5 SP.''',
        },
    "Medical Ward L1":{"level":5, "favor-cost": 2,
        "description":'''Heal 5 HP.''',
        },
    "Spring Water L2":{"level":10, "favor-cost": 3,
        "description":'''Heal 10 SP.''',
        },
    "Medical Ward L2":{"level":10, "favor-cost": 3,
        "description":'''Heal 10 HP.''',
        },
    "Spring Water L3":{"level":15, "favor-cost": 4,
        "description":'''Heal 15 SP.''',
        },
    "Medical Ward L3":{"level":15, "favor-cost": 4,
        "description":'''Heal 15 HP.''',
        },
    "Walk it Off":{"level":1, "favor-cost": 1,
        "description":'''Reset all status effects.''',
        },
    "Hammock":{"level":6, "favor-cost": 4,
        "description":'''Heal 5 HP, 5 SP. Reset all status effects.''',
        },
    "Bed":{"level":11, "favor-cost": 6,
        "description":'''Heal 10 HP, 10 SP. Reset all status effects.''',
        },
    "Luxury Suite":{"level":16, "favor-cost": 8,
        "description":'''Heal 15 HP, 15 SP. Reset all status effects.''',
        },
    "Free Hit":{"level":3, "favor-cost": 2,
        "description":'''You are allowed to make one action for free.''',
        },
    "Do Over":{"level":1, "favor-cost": 2,
        "description":'''You may restart the fight from the beginning tomorrow
when you are both fully rested and healed.''',
        },
    "":{"level":1,
        "description":'''''',
        },
}













