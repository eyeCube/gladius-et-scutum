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
        
        # player selects their moves
        pc_techs = self.pc.techs
        pc_moves=[]
        #temporary
        pc_moves.append(TECHNIQUES["Pressure Bolt"])
        pc_moves.append(TECHNIQUES["Gust Punch"])
        # spend SP (TODO)
        
        # NPC selects their moves
        npc_techs = self.npc.techs
        npc_moves=[]
        #temporary
        npc_moves.append(TECHNIQUES["Firebolt"])
        npc_moves.append(TECHNIQUES["Flame Whip"])
        # spend SP (TODO)

        self.resolve_techniques(pc_moves,npc_moves)
    # end def

    def resolve_techniques(self, pc_moves, npc_moves):
        plist=[]
        # resolution
        for move in pc_moves:
            priority = move['priority']
            speed = self.pc.stats.get("spd")
            plist.append((priority,speed,"PC",move,))
        for move in npc_moves:
            priority = move['priority']
            speed = self.npc.stats.get("spd")
            plist.append((priority,speed,"NPC",move,))
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
                
            movename = movedata['name']
            mode = movedata['mode']
            spcost = movedata['sp']
            nrgcost = movedata['nrg']
            acc = movedata['hit']
            dmg = movedata['damage']
            dfn = movedata['defense']
            eva = movedata['evasion']
            short = movedata['short']
            wide = movedata['wide']
            status = movedata['status']
            statusDur = movedata['status-dur']
            player.stats.sp -= spcost
            player.stats.energy -= nrgcost
            disarm = 0
            pierce = 0

            damage = dmg + player.stats.get("dmg")
            tohit = acc + player.stats.get("acc")

            print("{} used {}!".format(playerName, movename))
            
            if (1+int(random.random()*100)) > tohit: # miss
                print("It missed!")
            else: # hit

                # temporary ability buffs from the technique # these only last 1 turn
                if dfn != 0:
                    player.stats.dfn_buff = dfn 
                if eva != 0:
                    player.stats.eva_buff = eva

                # apply special effects for the technique (from "Special" column)
                damage,pierce,disarm = self.apply_special(player, target, movename, damage)
                
                # apply pierce by reducing defense of the target, down to a minimum of 0.
                # If the target already has below 0 defense, no change is made.
                targetDfn = max(
                    min(0,target.stats.get("dfn")),
                    target.stats.get("dfn") - pierce
                    )
                actual_dmg = max(0, damage - targetDfn)
                print("{} hit for {} dmg!".format(playerName, actual_dmg))

                # deal damage (TODO)

                # attempt disarm based on disarm stat (TODO)

            # standard status effect from element (burn, soft, gasp, daze)

            # countdown status timers
            player.increment_status_timers()
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
            target.stats.add_status("Prevent Healing", 1) # this would wear out immediately at end of the current turn, but could be useful still as attacks could still occur after this technique goes off.
        elif movename == "Double Image":
            player.stats.add_status("Double Image",3) # +1 Spd
        elif movename == "Shadow":
            player.stats.buffs.update({"Shadow":999}) 
        elif movename == "Obfuscate":
            pierce += 1
        elif movename == "Disarming Gust":
            disarm = 67
        elif movename == "Submission":
            target.stats.add_status("Prevent Movement", 1)
        elif movename == "Vacuum Chamber":
            pierce += 6
            target.stats.add_status("Prevent Healing", 1)
            
                    # ~~~ WATER ~~~ 
        elif movename == "Grab Weapon":
            disarm = 50
        elif movename == "Slippery Skin":
            player.stats.add_status("Slippery Skin",3)
        elif movename == "Acid Rain":
            pierce += 1
        elif movename == "Jet Stream":
            pierce += 1
        elif movename == "Liquefy":
            player.stats.buffs.update({"Liquefy":3})
        elif movename == "Heal":
            player.stats.buffs.update({"Heal":4})
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
        elif movename == "Lightning Bolt":
            pierce += 2
        
                    # ~~~ EARTH ~~~ 
        elif movename == "Harden":
            player.stats.add_status("Mana Rain", 6)
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

        return (damage, pierce, disarm,)
                
# end class


class Combatant_Stats:
    def __init__(self, weapon=0):
        self.update_needed = True

        self.buffs={}
        
        self.weapon=weapon
        self.mode="wide"

        self.body=10        # 10 HP
        self.spirit=10      # 10 SP
        self.skill=3
        
        self.energy=0
        self.sp_max=0
        self.sp=0
        self.hp_max=0
        self.hp=0

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

        self.pierce=0

        self.weapon=0
        self.lost_weapon=0

        self.status_burn=0 # fire
        self.status_soft=0 # water
        self.status_gasp=0 # air
        self.status_daze=0 # earth


    def fill_energy(self):
        self.energy = 3

    def purify(self): # for use with the Purify technique
        pass # only clear certain debuffs that are listed in the logic here

    def clear_status(self): # clear ALL status effects, good and bad
        self.buffs={}

    def remove_tech_buffs(self): # do this at the beginning of each turn for all players.
        self.dmg_buff = 0
        self.spd_buff = 0
        self.acc_buff = 0
        self.eva_buff = 0
        self.dfn_buff = 0
        self.update_needed = True

    def add_status(self, status, duration):
        self.buffs.update({status:duration})
        self.update_needed = True

    def remove_status(self, status):
        del self.buffs[i]
        self.update_needed = True

    def increment_status_timers(self):
        # IMPORTANT NOTE!!!!!
        #   This is done when you make an action. NOT when a turn counter increments.
        
        removelist=[]
        for k,v in self.buffs.items():
            newtime = v-1
            if newtime <= 0:
                removelist.append(k)
            else:
                self.buffs.update({k : v-1})
        for i in removelist:
            self.remove_status(self, i)
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
                dfn += 1
            elif k=="Wall of Clay":
                eva += 5
            elif k=="Pillow of Winds":
                eva += 5
            elif k=="Double Image":
                spd += 1
            elif k=="Slippery Skin":
                eva += 10
            elif k=="Liquefy":
                dfn + 1


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
##        self.update_needed = False  # reset update flag

                # TODO: un-comment this out. This is temporary to test!
    # end def

    def get(self, stat):
        if self.update_needed:
            self.calculate_stats()
        return self.__dict__[stat]
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
    def __init__(self, favorite_element=0, weapon=0):
        self.stats = Combatant_Stats(weapon)
        self.techs = Combatant_Techniques(favorite_element)
        
class NonPlayerCharacter:
    def __init__(self, favorite_element=0, weapon=0):
        self.stats = Combatant_Stats(weapon)
        self.techs = Combatant_Techniques(favorite_element)
    


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






