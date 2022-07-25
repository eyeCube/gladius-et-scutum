
from const import *
import battle as battlepy
import combatant



# creation functions

def create_AI_L1(pc):
    ai = AI_L1()
    if pc.favorite_element=="Earth":
        ai.init_v2()
    return ai
def create_AI_L2(pc):
    ai = AI_L2()
    if pc.favorite_element=="Air":
        ai.init_v2()
    return ai
def create_AI_L3(pc):
    ai = AI_L3()
    return ai
def create_AI_L4(pc):
    ai = AI_L4()
    return ai
def create_AI_L5(pc):
    ai = AI_L5()
    return ai
def create_AI_L6(pc):
    ai = AI_L6()
    return ai
def create_AI_L7(pc):
    ai = AI_L7()
    return ai
def create_AI_L8(pc):
    ai = AI_L8()
    return ai
def create_AI_L9(pc):
    ai = AI_L9()
    return ai
def create_AI_L10(pc):
    ai = AI_L10()
    return ai
def create_AI_L11(pc):
    ai = AI_L11()
    return ai
def create_AI_L12(pc):
    ai = AI_L12()
    return ai
def create_AI_L13(pc):
    ai = AI_L13()
    return ai
def create_AI_L14(pc):
    ai = AI_L14()
    return ai
def create_AI_L15(pc):
    ai = AI_L15()
    return ai

LEVELS={
    1 : create_AI_L1,
    2 : create_AI_L2,
    3 : create_AI_L3,
    4 : create_AI_L4,
    5 : create_AI_L5,
    6 : create_AI_L6,
    7 : create_AI_L7,
    8 : create_AI_L8,
    9 : create_AI_L9,
    10 : create_AI_L10,
    11 : create_AI_L11,
    12 : create_AI_L12,
    13 : create_AI_L13,
    14 : create_AI_L14,
    15 : create_AI_L15, # etc.
}


# how to use:
#   moveset = npc.ai.decide()

class AI: # TODO: check NRG, SP; if not enough, use fallback action
            # (this applies to all combatants including PC) --
            # something can e.g. drain SP in the middle of a fight and make you unable to complete a tech
            # for this we need a temporary SP and NRG pool for picking techniques;
            # SP and NRG are not drained until the tech goes off!!!
    def decide(self, target, mode):

        # sort by priority (TODO)
        sortlist = sorted(self.components, key=lambda x: (x.priority), reverse=True)

        # go through the logic for each component
        for component in sortlist:
            print("component: {} | {}".format(component.strat_wide, component.strat_short))
            result = component.choose(self.npc, target, mode)
            if result:
                return result
        # default action
        return ["Rest"]

        
class AI_L1(AI):
    def __init__(self):
        self.npc = combatant.Combatant(
            name="Amber",
            favorite_element=ELEM_FIRE,
            weapon=WPN_SLING,
            ai_obj=self
            )
        self.npc.gender=GENDER_FEMALE
        self.npc.stats.body = 12
        self.npc.stats.spirit = 24
        self.npc.stats.acc_base = 0
        self.npc.stats.eva_base = 5
        self.npc.fallback_behavior="Attack"
        
        self.components = [
            Behavior_Default(
                strat_wide=["Firebolt", "Firebolt", "Firebolt",],
                strat_short=["Burning Touch", "Burning Touch", "Burning Touch",]
                )
            ]

    def init_v2(self): # initialize alternate version
        # Use this version if player chooses Earth for their favorite element
        #   (this is to avoid the first encounter having an elemental advantage)
        self.npc.favorite_element = ELEM_EARTH
        self.components = [
            Behavior_Default(
                strat_wide=["Rock Throw", "Rock Throw", "Rock Throw",],
                strat_short=["Tunnel", "Grind",],
                )
            ]
        
        
class AI_L2(AI):
    def __init__(self):
        self.npc = combatant.Combatant(
            name="Thomas",
            favorite_element=ELEM_EARTH,
            weapon=WPN_AXESHIELD,
            sprite=SPR_ENEMY_THOMAS,
            ai_obj=self
            )
        self.npc.gender=GENDER_MALE
        self.npc.stats.body = 18
        self.npc.stats.spirit = 16
        self.npc.stats.acc_base = 5
        self.npc.stats.eva_base = 10
        self.npc.fallback_behavior="Attack"
        
        self.components = [
            Behavior_Default(
                strat_wide=["Harden", "Rockslide",],
                strat_short=["Harden", "Drill",]
                ),
            Behavior_Status_Self(
                status="Harden", value=1,
                strat_wide=["Rock Throw", "Rockslide",],
                strat_short=["Drill", "Grind",]
                ),
            ]

    def init_v2(self): # initialize alternate version
        # Use this version if player chooses Air for their favorite element
        #   (this is to avoid the first encounter having an elemental advantage)
        self.npc.favorite_element = ELEM_AIR
        
        self.components = [
            Behavior_Status_Self(
                status="Pillow of Winds", value=1,
                strat_wide=["Pressure Bolt", "Gust Punch",],
                strat_short=["Drill", "Grind",]
                ),
            Behavior_Default(
                strat_wide=["Pillow of Winds", "Gust Punch",],
                strat_short=["Breath of Wind", "Compression Wave",]
                ) 
            ]
        
        
class AI_L3(AI):
    def __init__(self):
        self.npc = combatant.Combatant(
            name="Elba",
            favorite_element=WATER,
            weapon=WPN_POLE,
            sprite=SPR_ENEMY_ELBA,
            ai_obj=self
            )
        self.npc.gender=GENDER_FEMALE
        self.npc.stats.body = 15
        self.npc.stats.spirit = 24
        self.npc.stats.acc_base = 5
        self.npc.stats.eva_base = 15
        self.npc.fallback_behavior="Attack"

        self.components = [
            Behavior_Status_Self_Inverted(
                status="Slippery Skin", value=0,
                strat_wide=["Slippery Skin", "Wavecrash",],
                strat_short=["Slippery Skin", "Bubble", "Bubble",]
                ),
            Behavior_Random(
                strat_list_wide=[
                    ["Hailstorm", "Bubble", "Bubble",],
                    ["Watergun", "Bubble", "Bubble",],
                    ["Bubble", "Bubble", "Bubble",],
                    ["Guiding Line", "Bubble", "Bubble",],
                    ],
                strat_list_short=[
                    ["Adhesion", "Bubble", "Bubble",],
                    ["Watergun", "Watergun", "Watergun",],
                    ["Bubble", "Bubble", "Bubble",],
                    ["Guiding Line", "Bubble", "Bubble",],
                    ],
                ),
            ]

        
class AI_L4(AI):
    def __init__(self):
        self.npc = combatant.Combatant(
            name="Peter",
            favorite_element=ELEM_FIRE,
            weapon=WPN_WHIPROPE,
            ai_obj=self
            )
        self.npc.gender=GENDER_MALE
        self.npc.stats.body = 24
        self.npc.stats.spirit = 18
        self.npc.stats.acc_base = 10
        self.npc.stats.eva_base = 10
        self.npc.fallback_behavior="Attack"
        
        self.components = [
            Behavior_HighDfn_Status_Opponent(
                status="Burning", value=2,
                strat_wide=["Devil's Tongue", "Rocket Punch",],
                strat_short=["Fire Eater", "Fire Eater", "Fire Eater",]
                ),
            Behavior_HighDfn_Opponent(
                value=2,
                strat_wide=["Devil's Tongue", "Rocket Punch",],
                strat_short=["Singe", "Ignition",]
                ),
            Behavior_Default(
                strat_wide=["Devil's Tongue", "Firebolt", "Firebolt",],
                strat_short=["Fire Eater", "Fire Eater", "Fire Eater",]
                )
            ]






class Behavior:
    def choose(self, p1, p2, mode="wide"):
        if self._think(p1, p2, mode):
            if mode=="wide":
                return self.strat_wide
            else:
                return self.strat_short
        return None
        
class Behavior_LowSP_Self(Behavior): # if we have low SP
    def __init__(self, value=6, strat_wide=[], strat_short=[], priority=30):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.low_sp_value = value        # which status to look for

    def _think(self, p1, p2, mode="wide"):
        if (p1.stats.get("sp") <= self.low_sp_value):
            return True
        return False

class Behavior_HighDfn_Status_Opponent(Behavior): # if opponent has high DFN and is afflicted with status
    def __init__(self, status=None, value=2, strat_wide=[], strat_short=[], priority=20):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.status = status        # which status to look for
        self.high_dfn_value = value  # what value of DFN is needed to use the highDfn strats

    def _think(self, p1, p2, mode="wide"):
        if (p2.stats.get_status(self.status) and
            p2.stats.get("dfn") >= self.high_dfn_value):
            return True
        return False

class Behavior_Status_Self_Inverted(Behavior): # if we are afflicted with status
    def __init__(self, status=None, value=0, strat_wide=[], strat_short=[], priority=18):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.status = status        # which status to look for
        self.status_value = value   # what duration of the status is needed

    def _think(self, p1, p2, mode="wide"):
        if (p1.stats.get_status(self.status) <= self.status_value):
            return True
        return False
        
class Behavior_Status_Self(Behavior): # if we are afflicted with status
    def __init__(self, status=None, value=1, strat_wide=[], strat_short=[], priority=19):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.status = status        # which status to look for
        self.status_value = value   # what duration of the status is needed

    def _think(self, p1, p2, mode="wide"):
        if (p1.stats.get_status(self.status) >= self.status_value):
            return True
        return False
        
class Behavior_Status_Opponent(Behavior): # if opponent is afflicted with status
    def __init__(self, status=None, strat_wide=[], strat_short=[], priority=17):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.status = status        # which status to look for

    def _think(self, p1, p2, mode="wide"):
        if (p2.stats.get_status(self.status)):
            return True
        return False

class Behavior_HighDfn_Opponent(Behavior): # if opponent has high DFN
    def __init__(self, value=2, strat_wide=[], strat_short=[], priority=10):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short
        self.high_dfn_value = value  # what value of DFN is needed to use the highDfn strats

    def _think(self, p1, p2, mode="wide"):
        if (p2.stats.get("dfn") >= self.high_dfn_value):
            return True
        return False

class Behavior_Random(Behavior): # randomized result from list
    def __init__(self, strat_list_wide=[], strat_list_short=[], priority=1):
        self.priority = priority
        self.strat_list_wide = strat_list_wide
        self.strat_list_short = strat_list_short
        self.strat_wide = None
        self.strat_short = None

    def _think(self, p1, p2, mode="wide"):
        if mode=="wide":
            self.strat_wide = random.choice(self.strat_list_wide)
        else:
            self.strat_short = random.choice(self.strat_list_short)
        return True 
        
class Behavior_Default(Behavior): # used if nothing else yields a result
    def __init__(self, strat_wide=[], strat_short=[], priority=0):
        self.priority = priority
        self.strat_wide = strat_wide
        self.strat_short = strat_short

    def _think(self, p1, p2, mode="wide"):
        return True






def choose_moves(ai):
    pass
