'''
    gladius.py

    Gladius et Scutum - Jane Wharton

    
'''

import pygame
import pygame_menu
import random

from const import *

pygame.init()
SURFACE = pygame.display.set_mode([1024, 768])

menu = pygame_menu.Menu('Character Name', 300, 600,
                       theme=pygame_menu.themes.THEME_DARK)

def act_technique():
    pass
def act_boon():
    pass
def act_retrieve():
    pass
def act_rest():
    pass
def act_suspend():
    pass
def act_forfeit():
    pass


class Game:
    def __init__(self):
        self.pc=PlayerCharacter(ELEM_AIR,weapon=0) #temporary
        self.pc_level = 1
    def level_up(self):
        self.pc_level += 1
        # choose what to improve!
        # HP + 1
        # SP + 1
        # Skill + 1


class Battle:
    def __init__(self, pc, npc):
        self.pc=pc
        self.npc=npc

    def turn(self):
        # reset buffs from techs
        self.pc.stats.remove_tech_buffs()
        self.npc.stats.remove_tech_buffs()

        # give players their energy
        self.pc.stats.fill_energy()
        self.npc.stats.fill_energy()

        self.upkeep(self.pc)
        self.upkeep(self.npc)
        
        # menu (TODO)

        
        
        # player selects their moves
        pc_techs = self.pc.techs
        pc_chosen_moves=[]
        #temporary
        pc_chosen_moves.append(TECHNIQUES["Pressure Bolt"])
        pc_chosen_moves.append(TECHNIQUES["Gust Punch"])
        # spend SP (TODO)
        # Ensure that you have enough SP and Energy;
        #   also that you are in the right position to perform the technique (TODO!!)
        
        # NPC selects their moves
        npc_techs = self.npc.techs
        npc_chosen_moves=[]
        #temporary
        npc_chosen_moves.append(TECHNIQUES["Firebolt"])
        npc_chosen_moves.append(TECHNIQUES["Flame Whip"])
        # spend SP (TODO)

        # move resolution
        self.resolve_techniques(pc_chosen_moves, npc_chosen_moves)
    # end def

    def resolve_techniques(self, pc_moves, npc_moves):
        plist=[]
        
        # resolution
        for move in pc_moves:
            priority = move['priority']
            speed = self.pc.stats.get("spd")
            plist.append((priority,speed,"PC",move,))
            if dfn != 0: # temporary buffs (until beginning of next turn) are applied instantly
                self.pc.stats.dfn_buff += dfn 
            if eva != 0:
                self.pc.stats.eva_buff += eva
        for move in npc_moves:
            priority = move['priority']
            speed = self.npc.stats.get("spd")
            plist.append((priority,speed,"NPC",move,))
            if dfn != 0:
                self.npc.stats.dfn_buff += dfn 
            if eva != 0:
                self.npc.stats.eva_buff += eva
        # sort by priority first, then by player speed, and finally,
        #   add some randomness for when speed and priorities are equal.
        sortlist = sorted(
            plist, key=lambda x: (x[0], x[1], int(random.random()*1000)), reverse=True
            )

##        print(sortlist)

        for item in sortlist:
            priority,speed,playerName,movedata=item
            
            if playerName=="PC":
                player=self.pc
                target=self.npc
            elif playerName=="NPC":
                player=self.npc
                target=self.pc
                
            disarm = 0
            pierce = 0

            element = movedata['element']
            movename = movedata['name']
            mode = movedata['mode']
            spcost = movedata['sp']
            nrgcost = movedata['nrg']
            acc = movedata['hit']
            dmg = movedata['damage']
            dfn = movedata['defense']
            eva = movedata['evasion']
            short = movedata['short'] # chance to move short
            wide = movedata['wide'] # chance to move wide
            status = movedata['status']
            statusDur = movedata['status-dur']
            
            player.stats.sp -= spcost
            player.stats.energy -= nrgcost

            damage = dmg + player.stats.get("dmg")
            tohit = acc + player.stats.get("acc")
            tohit -= target.stats.get("eva")

            print("{} used {}!".format(playerName, movename))
            
            if (1+int(random.random()*100)) > tohit: # miss
                print("    It missed!")
            else: # hit

                # apply special effects for the technique (from "Special" column)
                damage,pierce,disarm = self.apply_special(player, target, movename, damage)

                # standard status effect from element (burning, softened, hypoxic, stunned)
                if (1+int(random.random()*100)) <= status:
                    if element=="F": # Fire
                        target.stats.accumulate_status("Burning", statusDur)
                    elif element=="W": # Water
                        target.stats.accumulate_status("Softened", statusDur)
                    elif element=="A": # Air
                        target.stats.accumulate_status("Hypoxic", statusDur)
                    elif element=="E": # Earth
                        target.stats.accumulate_status("Stunned", statusDur)
                
                # apply pierce by reducing defense of the target, down to a minimum of 0.
                # If the target already has below 0 defense, no change is made.
                targetDfn = max(
                    min(0,target.stats.get("dfn")),
                    target.stats.get("dfn") - pierce
                    )
                actual_dmg = max(0, damage - targetDfn)
                print("    It does {} dmg!".format(actual_dmg))

                # deal damage
                target.stats.harm_hp(actual_dmg)

                # attempt disarm based on disarm stat (TODO)

                # attempt to go wide or short as the technique may call for

            # countdown status timers
            player.stats.decrement_status_counters()
        # end for
    # end def

    def apply_special(self, player, target, movename, damage):
        #       special technique status buffs      #

        pierce = 0
        disarm = 0
                
                    # ~~~ AIR ~~~ 
        if movename == "Pillow of Winds":
            player.stats.add_status("Pillow of Winds", 3)
        elif movename == "Suffocate":
            pierce += 2
            target.stats.add_status("Prevent Healing", 2) # this would wear out immediately at end of the current turn, but could be useful still as attacks could still occur after this technique goes off.
        elif movename == "Double Image":
            player.stats.add_status("Double Image",4) # +1 Spd
        elif movename == "Cloud Clone":
            player.stats.add_status("Cloud Clone",999) 
        elif movename == "Obfuscate":
            pierce += 1
        elif movename == "Disarming Gust":
            disarm = 50
        elif movename == "Submission":
            target.stats.add_status("Prevent Movement", 1)
        elif movename == "Vacuum Chamber":
            pierce += 6
        elif movename == "Third Eye":
            target.stats.add_status("Third Eye", 6)
            
                    # ~~~ WATER ~~~ 
        elif movename == "Grab Weapon":
            disarm = 33
        elif movename == "Slippery Skin":
            player.stats.add_status("Slippery Skin",3)
        elif movename == "Acid Rain":
            pierce += 1
        elif movename == "Jet Stream":
            pierce += 1
        elif movename == "Liquefy":
            player.stats.add_status("Liquefy",3)
        elif movename == "Heal":
            player.stats.add_status("Heal",4)
        elif movename == "Icicle":
            pierce += 2
        elif movename == "Mend":
            player.stats.heal_hp(5)
        elif movename == "Mana Rain":
            player.stats.add_status("Mana Rain", 6)
        elif movename == "Purify":
            player.stats.purify()
        
                    # ~~~ FIRE ~~~ 
        elif movename == "Singe":
            pierce += 1
        elif movename == "Burning Net":
            player.stats.add_status("Prevent Movement", 3)
        elif movename == "Lightning Bolt":
            pierce += 3
        elif movename == "Static Grip":
            player.stats.add_status("Prevent Movement", 3)
        
                    # ~~~ EARTH ~~~ 
        elif movename == "Harden":
            player.stats.add_status("Mana Rain", 6)
        elif movename == "Sandstorm":
            player.stats.add_status("Prevent Healing", 2)
        elif movename == "Drill":
            pierce += 1
        elif movename == "Constrict":
            pierce += 1
        elif movename == "Armorslayer":
            pierce += 3
            if target.stats.get("dfn") < 2:
                damage = 0
        elif movename == "Wall of Clay":
            player.stats.add_status("Wall of Clay", 6)
        elif movename == "Earthwave":
            pierce += 2
        elif movename == "Diamond Smash":
            pierce += 1
        elif movename == "Lockdown":
            target.stats.add_status("Prevent Movement", 3)
        elif movename == "Suppressing Sands":
            player.stats.clear_status()

        return (damage, pierce, disarm,)


    def upkeep(self, player):
        if "Heal" in player.stats.buffs.keys():
            player.heal_hp(1)
        if "Mana Rain" in player.stats.buffs.keys():
            player.heal_sp(1)
        
        player.stats.decrement_turn_timers()
        
# end class


class Combatant_Stats:
    def __init__(self, owner=None, weapon=0):
        self.owner=owner
        self.weapon=weapon
        self.lost_weapon=0
        
        self.update_needed = True
        self.buffs={}
        self.mode="wide"

        self.body=12        # -> HP
        self.spirit=12      # -> SP
        self.skill=3
        
        self.energy=0
        self.sp_max=0
        self.sp=0
        self.hp_max=0
        self.hp=0

        # Modifiable stats:
            # do not reference these directly, but use get() function to get them
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
        self.dmg_base=1     # +1 damage to keep things interesting
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

        self.pierce=0
    # end def

    def get(self, stat):
        if self.update_needed: # To test calculate_stats(), remove this check.
            self.calculate_stats()
            self.update_needed = False
        return self.__dict__[stat]

    def update_base(self, stat, value):
        self.__dict__["{}_base".format(stat)] = value
        self.update_needed = True

    def heal_hp(self, amount):
        if amount <= 0: return
        if "Prevent Healing" in player.stats.buffs.keys():
            print("{} heal prevented!".format(self.owner.name))
            return
        self.hp = min(self.get("hp_max"), self.hp + amount)
    def harm_hp(self, amount):
        if amount <= 0: return
        self.hp = max(0, self.hp - amount)
            # check for death and exhaustion in the Battle class' turn() function
    def heal_sp(self, amount):
        if amount <= 0: return
        self.sp = min(self.get("sp_max"), self.sp + amount)
    def harm_sp(self, amount):
        if amount <= 0: return
        self.sp = max(0, self.sp - amount)
        
    def fill_energy(self):
        self.energy = 3

    def purify(self):   # for use with the Purify technique.
                        #   Clear negative status effects, excepting those that are
                        #   physical in nature e.g. Prevent Movement, Prevent Healing
        keys=self.buffs.keys()
        elif "Burning" in keys:
            del self.buffs["Burning"]
        elif "Softened" in keys:
            del self.buffs["Softened"]
        elif "Hypoxic" in keys:
            del self.buffs["Hypoxic"]
        elif "Stunned" in keys:
            del self.buffs["Stunned"]
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

    def add_status(self, status, duration):
        self.buffs.update({status : duration})
        self.update_needed = True
    def remove_status(self, status):
        del self.buffs[status]
        self.update_needed = True
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
               "Prevent Movement", "Prevent Healing"
               ]
        self._decrement_statuses(tlist)
    # end def
    def decrement_turn_timers(self):
        # Status effects that last for a set number of TURNS

        tlist=["Harden", "Wall of Clay", "Pillow of Winds", "Double Image",
               "Slippery Skin", "Liquefy", "Heal", "Mana Rain"
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

    def retrieve_weapon(self):
        self.weapon = self.lost_weapon
        self.lost_weapon = WPN_NONE
        self.update_needed = True
    def disarm_weapon(self):
        self.lost_weapon = self.weapon
        self.weapon = WPN_NONE
        self.update_needed = True

    def calculate_stats(self):
        # update stats -- calculate from gear, buffs, etc.

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    default values from base    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.hp_max = self.body
        self.sp_max = self.spirit

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
        
        self.pierce += WEAPONS[self.weapon].get("pierce", 0)
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from buffs    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~#

        self.spd += self.spd_buff
        self.acc += self.acc_buff
        self.eva += self.eva_buff
        self.dfn += self.dfn_buff
        self.dmg += self.dmg_buff
            
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #    update from battle position    #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        if self.mode=="wide":
            self.spd += self.spd_wide
            self.acc += self.acc_wide
            self.eva += self.eva_wide
            self.dmg += self.dmg_wide
            self.dfn += self.dfn_wide
        elif self.mode=="short":
            self.spd += self.spd_short
            self.acc += self.acc_short
            self.eva += self.eva_short
            self.dmg += self.dmg_short
            self.dfn += self.dfn_short
            
        
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #     update from ability buffs     #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        for k,v in self.buffs.items():
            if k=="Harden":
                self.dfn += 1
            elif k=="Wall of Clay":
                self.eva += 5
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
        # end for
    # end def
        
# end class


class Combatant_Techniques:
    def __init__(self, favorite_element):
        self.techniques=[]
        self.favorite_element=favorite_element
    def add_tech(self, tech):
        self.techniques.append(tech)
    def remove_tech(self, tech):
        if tech in self.techniques:
            del self.techniques[tech]
    def learn_tech(self, owner, tech):
        reqSkill = TECHNIQUES[tech]["req-skill"]
        #favorite_element -- SP cost -2
        if owner.stats.skill >= reqSkill:
            self.add_tech(tech)
# end class
        

    
class PlayerCharacter:
    def __init__(self, name="", favorite_element=0, weapon=0):
        self.stats = Combatant_Stats(owner=self, weapon=weapon)
        self.techs = Combatant_Techniques(favorite_element)
        self.name = name
        
class NonPlayerCharacter:
    def __init__(self, name="", favorite_element=0, weapon=0):
        self.stats = Combatant_Stats(owner=self, weapon=weapon)
        self.techs = Combatant_Techniques(favorite_element)
        self.name = name
    


if __name__=="__main__":

    game = Game()
    
    npc=NonPlayerCharacter(ELEM_FIRE,weapon=WPN_NONE) #temporary

    # temporary -- testing
    battle=Battle(game.pc,npc)
    battle.turn()
    
    

##    
##    menu.add.button('Technique', act_technique)
##    menu.add.button('Claim Boon', act_boon)
##    menu.add.button('Retrieve Weapon', act_retrieve)
##    menu.add.button('Rest', act_rest)
##    menu.add.button('Suspend', act_suspend)
##    menu.add.button('Forfeit', act_forfeit)
##    menu.add.button('Quit Game', pygame_menu.events.EXIT)
##    
##    menu.mainloop(SURFACE)






