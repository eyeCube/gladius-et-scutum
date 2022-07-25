
from const import *


class Combatant_Stats:
    def __init__(self, owner=None, weapon=0, favorite_weapon=0):
        self.owner=owner
        self.weapon=weapon
        self.favorite_weapon=favorite_weapon
        self.lost_weapon=0
        self.stance=0

        self.dead = False
        self.update_needed = True
        self.buffs={}

        self.body=15        # -> HP
        self.spirit=20      # -> SP
        self.skill=3
        
        self.energy=0
        self.sp_max=0
        self.sp=0
        self.hp_max=0
        self.hp=0

        # Modifiable stats:
            # do not reference these directly, but use gets() function to get them
            # To modify the stat, call update_base() function
        self.acc=0          # Accuracy -- denoted as "HIT: +/-X%"
        self.acc_base=0
        self.acc_short=0
        self.acc_short_base=0
        self.acc_wide=0
        self.acc_wide_base=0
        self.acc_buff=0     # A temporary buff granted from techniques.
                            #   Lasts until the end of the turn.
        self.eva=0
        self.eva_base=0
        self.eva_short=0
        self.eva_short_base=0
        self.eva_wide=0
        self.eva_wide_base=0
        self.eva_buff=0
        
        self.dfn=0
        self.dfn_base=0
        self.dfn_short=0
        self.dfn_short_base=0
        self.dfn_wide=0
        self.dfn_wide_base=0
        self.dfn_buff=0
        
        self.dmg=0
        self.dmg_base=0
        self.dmg_short=0
        self.dmg_short_base=0
        self.dmg_wide=0
        self.dmg_wide_base=0
        self.dmg_buff=0
        
        self.spd=0
        self.spd_base=0
        self.spd_short=0
        self.spd_short_base=0
        self.spd_wide=0
        self.spd_wide_base=0
        self.spd_buff=0

        self.res_fire=0
        self.res_fire_base=0
        self.res_earth=0
        self.res_earth_base=0
        self.res_air=0
        self.res_air_base=0
        self.res_water=0
        self.res_water_base=0
        
        self.res_short=0        # resistance to opponent moving short
        self.res_short_base=0
        self.res_wide=0         # resistance to opponent moving wide
        self.res_wide_base=0

        self.pierce=0
    # end def

    def gets(self, stat):
        if self.update_needed: # To test calculate_stats(), remove this check.
            self.calculate_stats()
            self.update_needed = False
        return self.__dict__[stat]

    def improve_core_attribute(self, stat, add_value):
        self.__dict__[stat] += add_value
        self.update_needed = True

    def update_base(self, stat, value):
        # only for stats with _base
        assert(self.__dict__.get("{}_base".format(stat), None) != None)
        self.__dict__["{}_base".format(stat)] = value
        self.update_needed = True

    def heal_hp(self, amount):
        if amount <= 0: return
        if "Prevent Healing" in self.buffs.keys():
            print("{} heal prevented!".format(self.owner.name))
            return
        self.hp = min(self.gets("hp_max"), self.hp + amount)
    def harm_hp(self, amount):
        if amount <= 0: return
        self.hp = max(0, self.hp - amount)
        if self.hp <= 0:
            self.die()
    def heal_sp(self, amount):
        if amount <= 0: return
        self.sp = min(self.gets("sp_max"), self.sp + amount)
    def harm_sp(self, amount):
        if amount <= 0: return
        self.sp = max(0, self.sp - amount)

    def set_stance(self, stance):
        self.stance=stance
        self.update_needed=True

    def die(self):
        self.dead = True
        
    def fill_energy(self):
        self.energy = 3

    def purify(self):   # for use with the Purify technique.
                        #   Clear negative status effects, excepting those that are
                        #   physical in nature e.g. Prevent Movement, Prevent Healing
        keys=self.buffs.keys()
        if "Burning" in keys:
            del self.buffs["Burning"]
        elif "Softened" in keys:
            del self.buffs["Softened"]
        elif "Hypoxic" in keys:
            del self.buffs["Hypoxic"]
        elif "Stunned" in keys:
            del self.buffs["Stunned"]
        elif "Toxic" in keys:
            del self.buffs["Toxic"]
        self.update_needed = True

    def clear_status(self): # clear ALL status effects, good and bad
        self.buffs={}
        self.update_needed = True

    def remove_tech_buffs(self): # do this at the beginning of each turn for all players.
        self.dmg_buff = 0
        self.spd_buff = 0
        self.acc_buff = 0
        self.eva_buff = 0
        self.dfn_buff = 0
        self.update_needed = True

    def get_status(self, status):
        return self.buffs.get(status, 0)
    def add_status(self, status, duration):
        self.buffs.update({status : duration})
        self.update_needed = True
        print("Added status to {}: {} for {}".format(self.owner.name, status, duration))
    def remove_status(self, status):
        del self.buffs[status]
        self.update_needed = True
        print("Removed status from {}: {}".format(self.owner.name, status))
    def accumulate_status(self, status, duration):
        # add the status if it doesn't exist, or if it does, add to the duration.
        if status in self.buffs.keys():
            self.buffs.update({status : self.buffs[status] + duration})
        else:
            self.add_status(status, duration)

    def decrement_status_counters(self):
        # Status effects that last for a set number of ACTIONS
        # IMPORTANT NOTE!!!!!
        #   This is done when you make an action. NOT when a turn counter increments.

        tlist=["Burning", "Softened", "Stunned", "Hypoxic",
               "Prevent Movement", "Prevent Healing", "Guiding Line",
               ]
        self._decrement_statuses(tlist)
    # end def
    def decrement_turn_timers(self):
        # Status effects that last for a set number of TURNS

        tlist=["Harden", "Wall of Clay", "Pillow of Winds", "Double Image",
               "Slippery Skin", "Liquefy", "Heal", "Mana Rain", "Toxic", "Third Eye",
               "Dust Devils", "Hot Temper", "Cannon Calves", "Cloudwalk", 
               ]
        self._decrement_statuses(tlist)
    # end def
    def _decrement_statuses(self, tlist):
        removelist=[]
        for k,v in self.buffs.items():
            if k not in tlist:
                continue
            newtime = v-1
            if newtime <= 0:
                removelist.append(k)
            else:
                self.buffs.update({k : v-1})
        for i in removelist:
            self.remove_status(i)
    # end def

    def _retrieve_weapon(self):
        if self.lost_weapon == WPN_NONE:
            return False
        self.weapon = self.lost_weapon
        self.lost_weapon = WPN_NONE
        self.update_needed = True
        return True
    def _disarm_weapon(self):
        if self.weapon == WPN_NONE:
            return False
        self.lost_weapon = self.weapon
        self.weapon = WPN_NONE
        self.update_needed = True
        return True
    def _destroy_weapon(self):
        if self.weapon == WPN_NONE:
            return False
        self.lost_weapon = WPN_NONE
        self.weapon = WPN_NONE
        self.update_needed = True
        return True

    def calculate_stats(self):
        # update stats -- calculate from gear, buffs, etc.

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    default values from base    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.hp_max = self.body
        self.sp_max = self.spirit
        
        self.res_fire = self.res_fire_base
        self.res_earth = self.res_earth_base
        self.res_air = self.res_air_base
        self.res_water = self.res_water_base
        self.res_short = self.res_short_base
        self.res_wide = self.res_wide_base

        self.spd = self.spd_base
        self.spd_wide = self.spd_wide_base
        self.spd_short = self.spd_short_base
        
        self.acc = self.acc_base
        self.acc_wide = self.acc_wide_base
        self.acc_short = self.acc_short_base
        
        self.eva = self.eva_base
        self.eva_wide = self.eva_wide_base
        self.eva_short = self.eva_short_base
        
        self.dfn = self.dfn_base
        self.dfn_wide = self.dfn_wide_base
        self.dfn_short = self.dfn_short_base
        
        self.dmg = self.dmg_base
        self.dmg_wide = self.dmg_wide_base
        self.dmg_short = self.dmg_short_base
        

            #~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from gear    #
            #~~~~~~~~~~~~~~~~~~~~~~~~#
        
        self.spd += WEAPONS[self.weapon].get("speed", 0)
        self.spd_wide += WEAPONS[self.weapon].get("wide speed", 0)
        self.spd_short += WEAPONS[self.weapon].get("short speed", 0)
        
        self.acc += WEAPONS[self.weapon].get("to-hit", 0)
        self.acc_wide += WEAPONS[self.weapon].get("wide to-hit", 0)
        self.acc_short += WEAPONS[self.weapon].get("short to-hit", 0)
        
        self.eva += WEAPONS[self.weapon].get("evasion", 0)
        self.eva_wide += WEAPONS[self.weapon].get("wide evasion", 0)
        self.eva_short += WEAPONS[self.weapon].get("short evasion", 0)
        
        self.dfn += WEAPONS[self.weapon].get("defense", 0)
        self.dfn_wide += WEAPONS[self.weapon].get("wide defense", 0)
        self.dfn_short += WEAPONS[self.weapon].get("short defense", 0)
        
        self.dmg += WEAPONS[self.weapon].get("damage", 0)
        self.dmg_wide += WEAPONS[self.weapon].get("wide damage", 0)
        self.dmg_short += WEAPONS[self.weapon].get("short damage", 0)

        self.sp_max += WEAPONS[self.weapon].get("sp_max", 0)

        # set instead of add, because there is no base value for pierce
        self.pierce = WEAPONS[self.weapon].get("pierce", 0)

        # favorite weapon bonus
        if self.weapon == self.favorite_weapon:
            self.acc += 5
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from buffs    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.spd += self.spd_buff
        self.acc += self.acc_buff
        self.eva += self.eva_buff
        self.dfn += self.dfn_buff
        self.dmg += self.dmg_buff
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #     update from ability buffs     #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        for k,v in self.buffs.items():
            if k=="Harden":
                self.dfn += 1
            elif k=="Wall of Clay":
                self.eva_wide += 5
            elif k=="Pillow of Winds":
                self.eva += 5
            elif k=="Double Image":
                self.spd += 1
            elif k=="Slippery Skin":
                self.eva += 10
            elif k=="Liquefy":
                self.dfn += 1
            elif k=="Softened":
                self.dfn -= 1
                self.spd -= 1
            elif k=="Hypoxic":
                self.eva -= 10
                self.acc -= 10
            elif k=="Third Eye":
                self.acc += 5
            elif k=="Guiding Line":
                self.acc += 5
            elif k=="Dust Devils":
                self.dmg_wide += 1
            elif k=="Flaming Aura":
                self.dmg_short += 1
            elif k=="Grasshopper":
                self.spd += 1
            elif k=="Cloudwalk":
                self.eva_wide += 5
        # end for

        
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from stance     #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        if self.stance==STANCE_FIRE:
            self.acc += 5
        elif self.stance==STANCE_EARTH:
            self.eva_short += 5
        elif self.stance==STANCE_AIR:
            self.spd += 5
        elif self.stance==STANCE_WATER:
            self.eva_wide += 5
            
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from battle position    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            # AFTER all changes to wide/short stats have been made

        if self.owner.mode=="wide":
            self.spd += self.spd_wide
            self.acc += self.acc_wide
            self.eva += self.eva_wide
            self.dmg += self.dmg_wide
            self.dfn += self.dfn_wide
        elif self.owner.mode=="short":
            self.spd += self.spd_short
            self.acc += self.acc_short
            self.eva += self.eva_short
            self.dmg += self.dmg_short
            self.dfn += self.dfn_short

            
            #~~~~~~~~~~~~#
            #    caps    #
            #~~~~~~~~~~~~#

        if self.sp > self.sp_max:
            self.sp = self.sp_max
        if self.hp > self.hp_max:
            self.hp = self.hp_max
            
    # end def
        
# end class


class Combatant_Techniques:
    def __init__(self, owner=None, favorite_element=None):
        self.owner=owner
        self.techniques={ "fire":{}, "earth":{}, "air":{}, "water":{} }
        # example: {"fire": {1: ["Firebolt",],},
        self.favorite_element=favorite_element
        self.mastery={
            # element : {n points in basic mastery, bool for elemental status mastery}
            "F":{"hit":0, "status":False},
            "E":{"hit":0, "status":False},
            "A":{"hit":0, "status":False},
            "W":{"hit":0, "status":False},
            }

    def add_tech(self, tech):
        # TODO: special case for hybrid / multi-element techniques,
            # passive techs, passive techs you can spend points on, TODO: mastery....
        element = ELEMENTS[TECHNIQUES[tech]['element']]['name']
        level = TECHNIQUES[tech]['level']
        if self.techniques[element].get(level):
            self.techniques[element][level].append(tech)
        else:
            self.techniques[element].update({level: [tech]})

    def remove_tech(self, tech):
        element = ELEMENTS[TECHNIQUES[tech]['element']]['name']
        level = TECHNIQUES[tech]['level']
        try:
            self.techniques[element][level].remove(tech)
        except:
            print("Failed to remove tech -- {} lv{}: '{}'".append(element, level, tech))

    def learn_tech(self, tech):
        data = TECHNIQUES[tech]
        reqSkill = data["req-skill"]
        if ELEMENTS[data["element"]]['const']==self.favorite_element:
            reqSkill -= 2
        if self.owner.stats.skill >= reqSkill:
            self.add_tech(tech)
            return True
        return False

    def draw_terse(self, surface, x,y, tech): # show brief info as it appears in lists
        pygame.draw.rect(surface, NEUTRAL_LIGHT, pygame.Rect(x,y,300,32))
        font = FONT_MENU_1
        text = font.render(TECHNIQUES[tech]['mode'], True, BLACK)
        surface.blit(text, (x+4,y+4))
        text = font.render("SP {}".format(TECHNIQUES[tech]['sp']), True, BLACK)
        surface.blit(text, (x+96,y+4))
        text = font.render("NRG {}".format(TECHNIQUES[tech]['nrg']), True, BLACK)
        surface.blit(text, (x+192,y+4))

    def draw_details(self, surface, x,y, tech, show_reqs=True): # show detailed information for technique
        font = FONT_MENU_1
        data = TECHNIQUES[tech]
        
        if show_reqs:
            reqs='''
    Req. Techs: {reqs}
    Req. Skill: {skill}'''.format(reqs=data['pre-reqs'], skill=data['req-skill'])
        else:
            reqs=""

        spec='''
{hit}{dmg}{dfn}{eva}{short}{wide}{status}{special}{desc}'''.format(
    hit="    Hit: {}%\n".format(data['hit']) if data['hit']>0 else "",
    dmg="    DMG: {}\n".format(data['damage']) if data['damage']>0 else "",
    dfn="    DFN: {}\n".format(data['defense']) if data['defense']>0 else "",
    eva="    EVA: {}\n".format(data['evasion']) if data['evasion']>0 else "",
    short="    {}% chance to move Short\n".format(data['short']) if data['short']>0 else "",
    wide="    {}% chance to move Wide\n".format(data['wide']) if data['wide']>0 else "",
    special="    Special: {}\n".format(data['special']) if data['special'] else "",
    status="    {}% chance target is {} for {} actions\n".format(
        data['status'], ELEMENTS[data['element']]['status'], data['statusDur']
        ) if data['status']>0 else "",
    desc="    {}\n".format(data['notes']) if data['notes'] else ""
)
            
        text = font.render(
            '''{name}
    L{lv} {elem} tech | {mode}{reqs}
    Weapon: {wpn}
    SP: {sp}
    NRG: {nrg}
    Priority: {priority}{spec}'''.format(
    name=data['name'], elem=ELEMENTS[data['element']], lv=data['level'],
    mode=data['mode'], reqs=reqs, wpn=data['weapon'],
    sp=data['sp'], nrg=data['nrg'],
    spec=spec,
    priority=data['priority'] ),
            True, BLACK
            )
        
        surface.blit(text, (x,y,))
# end class
        

    
class Combatant: # class PC class and non-player character NonPlayerCharacter
    def __init__(self,
                 name="", favorite_element=0, weapon=0,
                 pc=False, sprite=None, gender=GENDER_MALE, ai_obj=None
                 ):
        
        self.stats = Combatant_Stats(owner=self, weapon=weapon, favorite_weapon=weapon)
        self.techs = Combatant_Techniques(owner=self, favorite_element=favorite_element)
        self.name = name
        self.pc=pc
        self.gender=gender
        self.ai=ai_obj
        
        if sprite:
            self.sprite=sprite
        else:
            self.update_sprite()
            
        self.mode = "wide"
        self.dead = False
        self.resting = False
        self.rest_interrupted = False
        self.stale_moves = 0        # counter for doing the same move x times in a row
                                    # reduce accuracy proportional to this value
        self.fallback_behavior = "Attack"   # use this action if chosen action fails

    @property
    def favorite_element(self):
        return self.techs.favorite_element
    @property
    def favorite_weapon(self):
        return self.stats.favorite_weapon
        
    def move_wide(self):
        self.mode = "wide"
        self.stats.update_needed=True
    def move_short(self):
        self.mode = "short"
        self.stats.update_needed=True

    def update_sprite(self):
        # TODO: call this when updating weapon / disarming / rearming etc.
        if self.pc:
            self.sprite = PC_WEAPON_SPRITES.get(self.stats.weapon, SPR_PLAYER_UNARMED)

    def disarm_weapon(self):
        self.stats._disarm_weapon()
        self.update_sprite()
    def destroy_weapon(self):
        self.stats._destroy_weapon()
        self.update_sprite()
    def retrieve_weapon(self):
        self.stats._retrieve_weapon()
        self.update_sprite()

    def draw(self, surface):
        if self.sprite==None:
            print("self.sprite value for player with name '{}' is None.".format(self.name))
            return
        
        ypos=280
        if self.pc:
            if self.mode=="wide":
                xpos=200
            else:
                xpos=380
        else:
            if self.mode=="wide":
                xpos=WIDTH-440
            else:
                xpos=WIDTH-620

        # draw the sprite
        surface.blit(self.sprite, (xpos,ypos,))
# end class

