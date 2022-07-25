'''
    const.py

    Gladius et Scutum - Jane Wharton

    
'''

import pygame



# pygame initialization
pygame.init()
WIDTH=1024
HEIGHT=768
SURFACE = pygame.display.set_mode([WIDTH, HEIGHT])

# techs
MAX_TECH_LEVEL = 5

# colors
NEUTRAL_DARK = (30,70,70)
NEUTRAL_LIGHT = (70,150,150)
BLACK   = (0,0,0,)
GRAY    = (128,128,128,)
LTGRAY  = (192,192,192,)
WHITE   = (255,255,255,)


# genders
GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NONBINARY = 2





    #---------------------#
    #        FONTS        #
    #---------------------#


FONT_MENU_1 = pygame.font.SysFont("consolas", 18)



    #-----------------------#
    #        SPRITES        #
    #-----------------------#

IMGSCALE=4

# player sprites
SPR_PLAYER_UNARMED = pygame.transform.scale(
    pygame.image.load('sprites/player-unarmed.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_JAVSHIELD = pygame.transform.scale(
    pygame.image.load('sprites/player-javelin-shield.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_AXESHIELD =  pygame.transform.scale(
    pygame.image.load('sprites/player-axe-shield.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_HAMSHIELD =  pygame.transform.scale(
    pygame.image.load('sprites/player-hammer-shield.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_SWOBUCKLER =  pygame.transform.scale(
    pygame.image.load('sprites/player-sword-buckler.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_CHAKRAM = pygame.transform.scale(
    pygame.image.load('sprites/player-chakram.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_WHIPROPE = pygame.transform.scale(
    pygame.image.load('sprites/player-whip-rope.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_POLE = pygame.transform.scale(
    pygame.image.load('sprites/player-pole.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_SPEAR = pygame.transform.scale(
    pygame.image.load('sprites/player-spear.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_NET = pygame.transform.scale(
    pygame.image.load('sprites/player-net.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_PLAYER_SLING = pygame.transform.scale(
    pygame.image.load('sprites/player-sling.png'), (IMGSCALE*48,IMGSCALE*32))

# enemy sprites
SPR_ENEMY_THOMAS = pygame.transform.scale(
    pygame.image.load('sprites/enemy-thomas.png'), (IMGSCALE*48,IMGSCALE*32))
SPR_ENEMY_ELBA = pygame.transform.scale(
    pygame.image.load('sprites/enemy-elba.png'), (IMGSCALE*48,IMGSCALE*32))

# backgrounds
BG_TEST =  pygame.transform.scale(
    pygame.image.load('sprites/bg-plain.png'), (WIDTH,512,))


    
    #-----------------------#
    #       ELEMENTS        #
    #-----------------------#

ELEM_NONE       = 0
ELEM_FIRE       = 1
ELEM_EARTH      = 2
ELEM_AIR        = 3
ELEM_WATER      = 4

STANCE_NONE     = 0
STANCE_FIRE     = 1
STANCE_EARTH    = 2
STANCE_AIR      = 3
STANCE_WATER    = 4

ELEMENTS={
    "":{'name':'','status':'', 'stance':0},
    "F":{'name':'fire', 'status':'Burning', 'stance':STANCE_FIRE, 'const':ELEM_FIRE,},
    "E":{'name':'earth', 'status':'Stunned', 'stance':STANCE_EARTH, 'const':ELEM_EARTH,},
    "A":{'name':'air', 'status':'Hypoxic', 'stance':STANCE_AIR, 'const':ELEM_AIR,},
    "W":{'name':'water', 'status':'Softened', 'stance':STANCE_WATER, 'const':ELEM_WATER,},
    ELEM_FIRE:"F",
    ELEM_AIR:"A",
    ELEM_EARTH:"E",
    ELEM_WATER:"W",
    STANCE_FIRE:"F",
    STANCE_AIR:"A",
    STANCE_EARTH:"E",
    STANCE_WATER:"W",
    }

STANCES={
    STANCE_NONE : {'name':'neutral', 'weakness':-1},
    STANCE_FIRE : {'name':'fire', 'weakness':STANCE_WATER},
    STANCE_EARTH : {'name':'earth', 'weakness':STANCE_FIRE},
    STANCE_AIR : {'name':'air', 'weakness':STANCE_EARTH},
    STANCE_WATER : {'name':'water', 'weakness':STANCE_AIR},
}



    #-----------------------#
    #       WEAPONS         #
    #-----------------------#

WPN_NONE        =0
WPN_JAVSHIELD   =1
WPN_HAMSHIELD   =2
WPN_AXESHIELD   =3
WPN_SWOBUCKLER  =4
WPN_WHIPROPE    =5
WPN_CHAKRAM     =6
WPN_POLE        =7
WPN_NET         =8
WPN_SLING       =9
WPN_SPEAR       =10
WPN_GREATSWORD  =11

WEAPONS={
    WPN_NONE:{
        "name":"Unarmed",
    },
    WPN_JAVSHIELD:{
        "name":"Javelin & Shield",
        "speed":2,
        "to-hit":5,
        "evasion":12,
        "defense":2,
        "sp_max":-6,         # Extra maximum SP
    },
    WPN_HAMSHIELD:{
        "name":"Hammer & Shield",
        "pierce":2,
        "evasion":6,
        "defense":1,
        "sp_max":-4,
        "destroy":50, # chance to fail destroy weapon cut by 50%
    },
    WPN_AXESHIELD:{
        "name":"Axe & Shield",
        "short speed":2,
        "short to-hit":5,
        "evasion":8,
        "damage":1,
        "defense":1,
        "sp_max":-4,
        "disarm":50, # chance to fail disarm cut by 50%
    },
    WPN_SWOBUCKLER:{
        "name":"Sword & Buckler",
        "speed":1,
        "short to-hit":10,
        "short damage":1,
        "evasion":10,
        "defense":1,
        "sp_max":-4,
    },
    WPN_WHIPROPE:{
        "name":"Whip & Rope",
        "wide speed":1,
        "to-hit":5,
        "short damage":2,
        "evasion":4,
    },
    WPN_CHAKRAM:{
        "name":"Chakram",
        "short speed":3,
        "short to-hit":6,
        "wide damage":1,
        "evasion":12,
        "defense":1,
        "sp_max":-2,
    },
    WPN_POLE:{
        "name":"Pole",
        "wide speed":4,
        "short to-hit":-10,
        "wide damage":1,
        "evasion":6,
        "defense":2,
        "sp_max":-6,
    },
    WPN_NET:{
        "name":"Weighted Net",
        "wide speed":3,
        "wide to-hit":20,
        "wide damage":1,
        "evasion":6,
        "sp_max":-2,
    },
    WPN_SLING:{
        "name":"Sling",
        "wide speed":5,
        "wide to-hit":5,
        "wide damage":2,
        "evasion":4,
        "sp_max":-2,
    },
    WPN_SPEAR:{
        "boon":True,        # only accessible from one-time use boons
        "name":"Spear",
        "wide speed":2,
        "wide to-hit":10,
        "wide damage":2,
        "evasion":12,
        "defense":2,
        "sp_max":-8,
    },
    WPN_GREATSWORD:{
        "boon":True,        # only accessible from one-time use boons
        "name":"Great Sword & Scutum",
        "short speed":2,
        "short to-hit":10,
        "short damage":2,
        "evasion":12,
        "defense":2,
        "sp_max":-8,
    }
}

PC_WEAPON_SPRITES={
    WPN_NONE : SPR_PLAYER_UNARMED,
    WPN_JAVSHIELD : SPR_PLAYER_JAVSHIELD,
    WPN_AXESHIELD : SPR_PLAYER_AXESHIELD,
    WPN_HAMSHIELD : SPR_PLAYER_HAMSHIELD,
    WPN_SWOBUCKLER : SPR_PLAYER_SWOBUCKLER,
    WPN_CHAKRAM : SPR_PLAYER_CHAKRAM,
    WPN_WHIPROPE : SPR_PLAYER_WHIPROPE,
    WPN_POLE : SPR_PLAYER_POLE,
    WPN_SPEAR : SPR_PLAYER_SPEAR,
    WPN_NET : SPR_PLAYER_NET,
    WPN_SLING : SPR_PLAYER_SLING,
}


TECHNIQUES={
"Firebolt": {'name': 'Firebolt', 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 2, 'special': '', 'notes': ''},
"Breath of Fire": {'name': 'Breath of Fire', 'element': 'F', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 10, 'status': 33, 'status-dur': 2, 'special': '', 'notes': ''},
"Burning Touch": {'name': 'Burning Touch', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 90, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 25, 'status-dur': 3, 'special': '', 'notes': ''},
"Ignition": {'name': 'Ignition', 'element': 'F', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 90, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 33, 'status': 67, 'status-dur': 4, 'special': '', 'notes': ''},
"Fire Eater": {'name': 'Fire Eater', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 100, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Singe": {'name': 'Singe', 'element': 'F', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': 'Pierce 1', 'notes': ''},
"Rocket Punch": {'name': 'Rocket Punch', 'element': 'F', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': 3, 'damage': 2, 'defense': 0, 'evasion': 5, 'short': 33, 'wide': 33, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Devil's Tongue": {'name': "Devil's Tongue", 'element': 'F', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Whip & Rope', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 75, 'wide': 0, 'status': 50, 'status-dur': 2, 'special': '', 'notes': ''},
"Fire Mastery": {'name': 'Fire Mastery', 'element': 'F', 'mode': 'Passive', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Accuracy +5% with all Fire techniques per Skill Point spent', 'notes': ''},
"Cannon Calves": {'name': 'Cannon Calves', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Rocket Punch', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 65, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 67, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Speed +1 for 2 turns', 'notes': ''},
"Burning Net": {'name': 'Burning Net', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Any Lv 1 Fire tech', 'req-skill': 5, 'level': 2, 'weapon': 'Weighted Net', 'sp': 3, 'nrg': 2, 'hit': 55, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 83, 'wide': 0, 'status': 33, 'status-dur': 4, 'special': 'Prevents enemy movement for 3 actions', 'notes': ''},
"Combustion": {'name': 'Combustion', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Ignition', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 3, 'hit': 95, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Blue Fire": {'name': 'Blue Fire', 'element': 'F', 'mode': 'Agile', 'pre-reqs': 'Firebolt', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 65, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 6, 'special': '', 'notes': ''},
"Flamespray": {'name': 'Flamespray', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Breath of Fire', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 95, 'priority': 2, 'damage': 3, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 80, 'status-dur': 5, 'special': '', 'notes': ''},
"Singing Grasp": {'name': 'Singing Grasp', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Burning Touch', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 1, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': '', 'notes': ''},
"Shock": {'name': 'Shock', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Any Lv 1 Fire tech', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 95, 'priority': 2, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Hot Temper": {'name': 'Hot Temper', 'element': 'F', 'mode': 'Agile', 'pre-reqs': 'Fire Eater', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': 1, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'SHORT DMG +1 for 2 turns', 'notes': ''},
"Temperature": {'name': 'Temperature', 'element': 'F', 'mode': 'Passive', 'pre-reqs': 'Any Lv 1 Fire tech', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Chance to cause Burning status increased', 'notes': ''},
"Hot Oil": {'name': 'Hot Oil', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Flamespray', 'req-skill': 8, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 65, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 6, 'special': '', 'notes': ''},
"Lightning Bolt": {'name': 'Lightning Bolt', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Shock', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 90, 'priority': 6, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 3', 'notes': ''},
"Targeted Combustion": {'name': 'Targeted Combustion', 'element': 'F', 'mode': 'Wide', 'pre-reqs': 'Combustion', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 50, 'priority': -2, 'damage': 8, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Hit +30% if target is Burning', 'notes': "A grappling move that temporarily disables motor neurons in the opponent's peripheral nervous system, making it impossible for them to move."},
"Fire Whirl": {'name': 'Fire Whirl', 'element': 'F', 'mode': 'Agile', 'pre-reqs': 'Flamespray', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 0, 'status': 75, 'status-dur': 4, 'special': '', 'notes': "This technique lights a fire deep inside your opponent's internal systems, burning them from the inside out and consuming the oxygen directly from their cells."},
"Static Grip": {'name': 'Static Grip', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Shock', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 90, 'priority': 2, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy movement for 2 actions', 'notes': ''},
"Overdrive": {'name': 'Overdrive', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Flaming Aura', 'req-skill': 13, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 2, 'hit': 75, 'priority': -3, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 90, 'status-dur': 3, 'special': '90% chance target is Hypoxic for 3 actions', 'notes': ''},
"Conduction": {'name': 'Conduction', 'element': 'F', 'mode': 'Short', 'pre-reqs': 'Singing Grasp', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': 'Disarm 83%', 'notes': ''},
"Flaming Aura": {'name': 'Flaming Aura', 'element': 'F', 'mode': 'Passive', 'pre-reqs': 'Any Lv 2 Fire tech', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'When struck, 10% chance opponent is Burning for 3 actions', 'notes': ''},
"Cold Fire": {'name': 'Cold Fire', 'element': 'F', 'mode': 'Passive', 'pre-reqs': 'Any Lv 3 Fire tech', 'req-skill': 15, 'level': 4, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Short DMG +1', 'notes': ''},
"Solaris": {'name': 'Solaris', 'element': 'F', 'mode': 'Passive', 'pre-reqs': 'Any Lv 3 Fire tech', 'req-skill': 15, 'level': 4, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Wide DMG +1', 'notes': ''},
"Grind": {'name': 'Grind', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Harden": {'name': 'Harden', 'element': 'E', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 0, 'status-dur': 0, 'special': 'DFN +1 for 3 turns', 'notes': ''},
"Rock Throw": {'name': 'Rock Throw', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 2, 'special': '', 'notes': ''},
"Rockslide": {'name': 'Rockslide', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': -2, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 75, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Tunnel": {'name': 'Tunnel', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 85, 'priority': -2, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Sandblast": {'name': 'Sandblast', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 105, 'priority': 2, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy healing for 3 actions', 'notes': ''},
"Drill": {'name': 'Drill', 'element': 'E', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 90, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 2, 'special': 'Pierce 1', 'notes': ''},
"Missile Weapon": {'name': 'Missile Weapon', 'element': 'E', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 70, 'priority': 1, 'damage': 3, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 2, 'special': 'Disarm self; must be armed to use', 'notes': ''},
"Earth Mastery": {'name': 'Earth Mastery', 'element': 'E', 'mode': 'Passive', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Accuracy +5% with all Earth techniques per Skill Point spent', 'notes': ''},
"Stone Smash": {'name': 'Stone Smash', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Rock Throw', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 85, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': 'Pierce 1', 'notes': ''},
"Fist of Stone": {'name': 'Fist of Stone', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Any Lv 1 Earth tech', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 75, 'priority': 1, 'damage': 5, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Constrict": {'name': 'Constrict', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Grind', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 3, 'special': 'Pierce 1', 'notes': ''},
"Pebblegun": {'name': 'Pebblegun', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Rock Throw', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 65, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 2, 'special': '', 'notes': ''},
"Armorslayer": {'name': 'Armorslayer', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Drill', 'req-skill': 8, 'level': 2, 'weapon': 'Sword & Buckler', 'sp': 2, 'nrg': 2, 'hit': 60, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': "Damage and Pierce scales with target's Defense", 'notes': ''},
"Wall of Clay": {'name': 'Wall of Clay', 'element': 'E', 'mode': 'Agile', 'pre-reqs': 'Harden', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 70, 'priority': 0, 'damage': 2, 'defense': 1, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': 'Wide EVA +5 for 6 turns', 'notes': ''},
"Tremor": {'name': 'Tremor', 'element': 'E', 'mode': 'Agile', 'pre-reqs': 'Rockslide, Tunnel', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 95, 'priority': 3, 'damage': 3, 'defense': 0, 'evasion': 10, 'short': 83, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': '', 'notes': ''},
"Sand Slash": {'name': 'Sand Slash', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Sandblast', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': 2, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 0, 'status-dur': 0, 'special': 'Enemy accuracy -10% for 4 actions', 'notes': ''},
"Mycelium Rave": {'name': 'Mycelium Rave', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Any Lv 1 Earth tech', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 90, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Potency": {'name': 'Potency', 'element': 'E', 'mode': 'Passive', 'pre-reqs': 'Any Lv 1 Earth tech', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Chance to cause Stunned status increased', 'notes': ''},
"Vibrohammer": {'name': 'Vibrohammer', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Drill', 'req-skill': 9, 'level': 3, 'weapon': 'Hammer & Shield', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 3, 'special': '33% chance target is Softened for 3 actions', 'notes': ''},
"Rumble": {'name': 'Rumble', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Tremor', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 80, 'priority': 0, 'damage': 7, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 2, 'special': '', 'notes': ''},
"Earthwave": {'name': 'Earthwave', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Tremor', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 85, 'priority': 0, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 2', 'notes': ''},
"Diamond Smash": {'name': 'Diamond Smash', 'element': 'E', 'mode': 'Agile', 'pre-reqs': 'Stone Smash, Fist of Stone', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 60, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 1; Damage +1 while Short', 'notes': ''},
"Lockdown": {'name': 'Lockdown', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Constrict', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 70, 'priority': -1, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy movement for 3 actions', 'notes': ''},
"Solid Guard": {'name': 'Solid Guard', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Wall of Clay', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 5, 'defense': 1, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Pierce 1; Only works if foe hits after using on this turn', 'notes': ''},
"Leverage Weapon": {'name': 'Leverage Weapon', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Constrict', 'req-skill': 11, 'level': 3, 'weapon': 'Not Unarmed', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Disarm 100%', 'notes': ''},
"Breakout": {'name': 'Breakout', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Constrict', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 90, 'status': 33, 'status-dur': 2, 'special': '', 'notes': ''},
"Mycotoxin": {'name': 'Mycotoxin', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Mycelium Rave', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 75, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '40% chance target is Toxic for 3 turns', 'notes': ''},
"Meteor Smash": {'name': 'Meteor Smash', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Diamond Smash', 'req-skill': 16, 'level': 4, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 70, 'priority': -3, 'damage': 10, 'defense': -1, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Suppressing Sands": {'name': 'Suppressing Sands', 'element': 'E', 'mode': 'Wide', 'pre-reqs': 'Sand Slash', 'req-skill': 13, 'level': 4, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 95, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Clear all status effects on the target', 'notes': ''},
"Grounding": {'name': 'Grounding', 'element': 'E', 'mode': 'Agile', 'pre-reqs': 'Any Lv 3 Earth tech', 'req-skill': 14, 'level': 4, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 2, 'defense': 1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Clear all status effects on the user', 'notes': ''},
"Shatter Weapon": {'name': 'Shatter Weapon', 'element': 'E', 'mode': 'Short', 'pre-reqs': 'Leverage Weapon', 'req-skill': 15, 'level': 4, 'weapon': 'Not Unarmed', 'sp': 4, 'nrg': 2, 'hit': 65, 'priority': -2, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 0, 'status-dur': 0, 'special': 'Destroy Weapon 50%; Disarm 100%', 'notes': ''},
"Spore Cloud": {'name': 'Spore Cloud', 'element': 'E', 'mode': 'Agile', 'pre-reqs': 'Mycotoxin', 'req-skill': 16, 'level': 4, 'weapon': 'Any', 'sp': 5, 'nrg': 1, 'hit': 85, 'priority': 1, 'damage': 0, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '75% chance to cause Toxic for 6 turns', 'notes': ''},
"Stone Skin": {'name': 'Stone Skin', 'element': 'E', 'mode': 'Passive', 'pre-reqs': 'Any Lv 3 Earth tech', 'req-skill': 15, 'level': 4, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'DFN +1', 'notes': ''},
"Breath of Wind": {'name': 'Breath of Wind', 'element': 'A', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 33, 'status-dur': 3, 'special': '', 'notes': ''},
"Pressure Bolt": {'name': 'Pressure Bolt', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Pillow of Winds": {'name': 'Pillow of Winds', 'element': 'A', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 17, 'status': 0, 'status-dur': 0, 'special': 'EVA +5 for 3 turns', 'notes': ''},
"Compression Wave": {'name': 'Compression Wave', 'element': 'A', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 95, 'priority': 3, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 40, 'status': 50, 'status-dur': 3, 'special': '', 'notes': ''},
"Gust Punch": {'name': 'Gust Punch', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': 1, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': '25% chance target is Stunned for 2 actions', 'notes': ''},
"Double Image": {'name': 'Double Image', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 6, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 85, 'priority': 4, 'damage': 1, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Speed +1 for 4 turns', 'notes': ''},
"Suffocate": {'name': 'Suffocate', 'element': 'A', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': 'Pierce 2; Prevents enemy healing for 2 actions', 'notes': ''},
"Foggy Step": {'name': 'Foggy Step', 'element': 'A', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 80, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Air Mastery": {'name': 'Air Mastery', 'element': 'A', 'mode': 'Passive', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Accuracy +5% with all Air techniques per Skill Point spent', 'notes': ''},
"Spiral Out": {'name': 'Spiral Out', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Breath of Wind', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': -1, 'damage': 2, 'defense': 0, 'evasion': 10, 'short': 67, 'wide': 67, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Cloud Clone": {'name': 'Cloud Clone', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Double Image', 'req-skill': 9, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 200, 'priority': -7, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Summon Cloud Clone to assist in combat. Does 1 Neutral Dmg / turn with 90% to-hit, and has 3 HP. When you are struck, divert damage to the Hologram instead. Can only cast once per battle. ', 'notes': ''},
"Obfuscate": {'name': 'Obfuscate', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Pillow of Winds', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 85, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 5, 'special': 'Pierce 1', 'notes': ''},
"Disarming Gust": {'name': 'Disarming Gust', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Pressure Bolt', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 85, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Disarm 50%', 'notes': ''},
"Shockwave": {'name': 'Shockwave', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Compression Wave', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 105, 'priority': 5, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 67, 'status': 50, 'status-dur': 5, 'special': '', 'notes': ''},
"Submission": {'name': 'Submission', 'element': 'A', 'mode': 'Short', 'pre-reqs': 'Suffocate', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 75, 'priority': 1, 'damage': 3, 'defense': 1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': 'Prevents enemy movement for 2 actions', 'notes': ''},
"Compression Bomb": {'name': 'Compression Bomb', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Gust Punch', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 70, 'priority': -2, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '50% chance target is Stunned for 3 actions', 'notes': ''},
"Quicksilver": {'name': 'Quicksilver', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Double Image', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 75, 'priority': 1, 'damage': 3, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 33, 'status-dur': 3, 'special': '', 'notes': ''},
"Zephyr": {'name': 'Zephyr', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Foggy Step', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 65, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Strikes twice', 'notes': ''},
"Anoxia": {'name': 'Anoxia', 'element': 'A', 'mode': 'Passive', 'pre-reqs': 'Any Lv 1 Air tech', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Chance to cause Hypoxia status increased', 'notes': ''},
"Vacuum Chamber": {'name': 'Vacuum Chamber', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Submission', 'req-skill': 13, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 95, 'priority': -6, 'damage': 6, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 100, 'status-dur': 5, 'special': 'Pierce 6', 'notes': ''},
"Vortex": {'name': 'Vortex', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Spiral Out', 'req-skill': 11, 'level': 3, 'weapon': 'Chakram', 'sp': 3, 'nrg': 3, 'hit': 90, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 10, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 3, 'special': 'Disarm 75%', 'notes': ''},
"Third Eye": {'name': 'Third Eye', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Cloud Clone', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'ACC +5 for 6 turns', 'notes': ''},
"Dust Devils": {'name': 'Dust Devils', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Spiral Out', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 85, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'WIDE DMG +1 for 2 turns', 'notes': ''},
"Misdirection": {'name': 'Misdirection', 'element': 'A', 'mode': 'Agile', 'pre-reqs': 'Obfuscate', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 95, 'priority': -2, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 83, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Cloudwalk": {'name': 'Cloudwalk', 'element': 'A', 'mode': 'Wide', 'pre-reqs': 'Zephyr', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 1, 'nrg': 3, 'hit': 90, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Wide EVA +5% for 6 turns', 'notes': ''},
"Aether": {'name': 'Aether', 'element': 'A', 'mode': 'Passive', 'pre-reqs': 'Any Lv 3 Air tech', 'req-skill': 15, 'level': 4, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Wide EVA +10%', 'notes': ''},
"Bubble": {'name': 'Bubble', 'element': 'W', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 75, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 17, 'status-dur': 2, 'special': '', 'notes': ''},
"Watergun": {'name': 'Watergun', 'element': 'W', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 33, 'status': 50, 'status-dur': 2, 'special': '', 'notes': ''},
"Wavecrash": {'name': 'Wavecrash', 'element': 'W', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 1, 'nrg': 2, 'hit': 90, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 5, 'short': 33, 'wide': 0, 'status': 75, 'status-dur': 3, 'special': '', 'notes': ''},
"Adhesion": {'name': 'Adhesion', 'element': 'W', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 80, 'priority': -1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Disarm 40%', 'notes': ''},
"Slippery Skin": {'name': 'Slippery Skin', 'element': 'W', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 50, 'status': 0, 'status-dur': 0, 'special': 'EVA +10 for 3 turns', 'notes': ''},
"Downpour": {'name': 'Downpour', 'element': 'W', 'mode': 'Wide', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 1, 'hit': 100, 'priority': 2, 'damage': 0, 'defense': 0, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 90, 'status-dur': 3, 'special': '', 'notes': ''},
"Dissolve": {'name': 'Dissolve', 'element': 'W', 'mode': 'Short', 'pre-reqs': '', 'req-skill': 4, 'level': 1, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 75, 'priority': -1, 'damage': 2, 'defense': -1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 3, 'special': '33% chance target is Toxic for 3 turns', 'notes': ''},
"Hailstorm": {'name': 'Hailstorm', 'element': 'W', 'mode': 'Agile', 'pre-reqs': '', 'req-skill': 5, 'level': 1, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 90, 'priority': 0, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Water Mastery": {'name': 'Water Mastery', 'element': 'W', 'mode': 'Passive', 'pre-reqs': '', 'req-skill': 3, 'level': 1, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Accuracy +5% with all Water techniques per Skill Point spent', 'notes': ''},
"Wavesurf": {'name': 'Wavesurf', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Wavecrash', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 90, 'priority': 2, 'damage': 3, 'defense': 1, 'evasion': 5, 'short': 40, 'wide': 0, 'status': 83, 'status-dur': 2, 'special': '', 'notes': ''},
"Jet Stream": {'name': 'Jet Stream', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Watergun', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 80, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 2, 'special': 'Pierce 1 while Short', 'notes': ''},
"Shield": {'name': 'Shield', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Bubble', 'req-skill': 5, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': 1, 'damage': 0, 'defense': 2, 'evasion': 5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': ''},
"Liquefy": {'name': 'Liquefy', 'element': 'W', 'mode': 'Short', 'pre-reqs': 'Slippery Skin', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -1, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 75, 'wide': 75, 'status': 0, 'status-dur': 0, 'special': 'DFN +1 for 3 turns', 'notes': ''},
"Cold Knuckle": {'name': 'Cold Knuckle', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Hailstorm', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 3, 'hit': 80, 'priority': 1, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': '', 'notes': ''},
"Heal": {'name': 'Heal', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Any Lv 1 Water tech', 'req-skill': 6, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -2, 'damage': 0, 'defense': 0, 'evasion': -5, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 1 HP/turn for 4 turns', 'notes': ''},
"Tentacle": {'name': 'Tentacle', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Adhesion', 'req-skill': 8, 'level': 2, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 75, 'priority': 0, 'damage': 3, 'defense': 0, 'evasion': 0, 'short': 83, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Prevents enemy movement for 3 actions', 'notes': ''},
"Acid Rain": {'name': 'Acid Rain', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Downpour, Dissolve', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 100, 'priority': 2, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 67, 'status-dur': 3, 'special': '33% chance target is Toxic for 3 turns', 'notes': ''},
"Permeability": {'name': 'Permeability', 'element': 'W', 'mode': 'Passive', 'pre-reqs': 'Any Lv 1 Water tech', 'req-skill': 7, 'level': 2, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Chance to cause Softened status increased', 'notes': ''},
"Bubble Bomb": {'name': 'Bubble Bomb', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Shield', 'req-skill': 8, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 3, 'hit': 80, 'priority': 0, 'damage': 5, 'defense': 0, 'evasion': 5, 'short': 50, 'wide': 0, 'status': 25, 'status-dur': 3, 'special': '', 'notes': ''},
"Icicle": {'name': 'Icicle', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Cold Knuckle', 'req-skill': 9, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 75, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 75, 'status-dur': 5, 'special': 'Pierce 2', 'notes': ''},
"Mend": {'name': 'Mend', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Heal', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 4, 'nrg': 1, 'hit': 200, 'priority': -3, 'damage': 0, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 5 HP; can only use once per turn', 'notes': ''},
"Mana Rain": {'name': 'Mana Rain', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Heal, Downpour', 'req-skill': 11, 'level': 3, 'weapon': 'Any', 'sp': 1, 'nrg': 1, 'hit': 200, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Heal 1 SP/turn for 6 turns', 'notes': ''},
"Purify": {'name': 'Purify', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Heal', 'req-skill': 8, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 200, 'priority': -9, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Clear status effects on the user', 'notes': ''},
"Pressure Beam": {'name': 'Pressure Beam', 'element': 'W', 'mode': 'Short', 'pre-reqs': 'Jet Stream', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 3, 'nrg': 1, 'hit': 85, 'priority': -2, 'damage': 2, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 3, 'special': 'Pierce 2', 'notes': ''},
"Poison Diffusion": {'name': 'Poison Diffusion', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Acid Rain', 'req-skill': 10, 'level': 3, 'weapon': 'Any', 'sp': 2, 'nrg': 2, 'hit': 65, 'priority': 1, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '100% chance to cause Toxic for 4 turns', 'notes': ''},
"Medusa": {'name': 'Medusa', 'element': 'W', 'mode': 'Wide', 'pre-reqs': 'Tentacle', 'req-skill': 12, 'level': 3, 'weapon': 'Any', 'sp': 5, 'nrg': 3, 'hit': 75, 'priority': 2, 'damage': 3, 'defense': 1, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 50, 'status-dur': 2, 'special': 'Strikes twice; 50% chance target is Stunned for 2 actions', 'notes': ''},
"Frostbite": {'name': 'Frostbite', 'element': 'W', 'mode': 'Agile', 'pre-reqs': 'Icicle', 'req-skill': 13, 'level': 4, 'weapon': 'Any', 'sp': 4, 'nrg': 2, 'hit': 65, 'priority': 0, 'damage': 4, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 83, 'status-dur': 6, 'special': '50% chance target is Burning for 6 actions', 'notes': ''},
"Life Leech": {'name': 'Life Leech', 'element': 'W', 'mode': 'Short', 'pre-reqs': 'Tentacle, Mend', 'req-skill': 14, 'level': 4, 'weapon': 'Any', 'sp': 3, 'nrg': 2, 'hit': 60, 'priority': -1, 'damage': 3, 'defense': 0, 'evasion': -10, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'You heal HP equal to the damage dealt', 'notes': ''},
"Flow": {'name': 'Flow', 'element': 'W', 'mode': 'Passive', 'pre-reqs': 'Any Lv 3 Water tech', 'req-skill': 15, 'level': 4, 'weapon': 'Any', 'sp': 0, 'nrg': 0, 'hit': 0, 'priority': 0, 'damage': 0, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': 'Short EVA +10%', 'notes': ''},
"Attack": {'name': 'Attack', 'element': '', 'mode': 'both', 'pre-reqs': '', 'req-skill': 0, 'level': 0, 'weapon': 'Any', 'sp': 0, 'nrg': 1, 'hit': 50, 'priority': 0, 'damage': 1, 'defense': 0, 'evasion': 0, 'short': 0, 'wide': 0, 'status': 0, 'status-dur': 0, 'special': '', 'notes': 'The most basic of combat techniques.'},
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













