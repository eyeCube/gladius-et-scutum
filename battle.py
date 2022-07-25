
import pygame
import random

from const import *



def act_technique():
    pass
def act_boon():
    pass
def act_retrieve():
    pass
def act_rest(character):
    character.resting = True
    character.rest_interrupted = False
def act_suspend():
    pass
def act_forfeit():
    pass


class Battle:
    def __init__(self, game, pc, npc):
        self.game=game
        self.pc=pc
        self.npc=npc
        self.mode="wide"

    def try_apply_status(self, player, target, status, duration, value, accumulate=False):
        if ((status=="Burning" and player.techs.mastery["fire"]["status"])
        or (status=="Stunned" and player.techs.mastery["earth"]["status"])
        or (status=="Softened" and player.techs.mastery["water"]["status"])
        or (status=="Hypoxic" and player.techs.mastery["air"]["status"]) ):
            value += (100-value)//2
        if random.random()*100 < value:
            if accumulate:
                target.stats.accumulate_status(status,duration)
            else:
                target.stats.add_status(status,duration)

    def turn_begin(self):
        print("turn begin")
        # reset buffs from techs
        self.pc.stats.remove_tech_buffs()
        self.npc.stats.remove_tech_buffs()

        # upkeep
        self.pc.stats.fill_energy()
        self.npc.stats.fill_energy()
        self.upkeep(self.pc)
        self.upkeep(self.npc)

        # reset stack
        self.game.register_init()
        
    def turn_end(self):

        self.game.locked=True
            # ^ just in case we have some animations in the future that involve
            # multiple frames playing during multiple iterations of the main game loop
        
        # NPC selects their moves
        npc_chosen_moves = self.npc.ai.decide(self.pc, self.mode)

        # rest
        self.npc.resting=False
        self.npc.rest_interrupted=False

        # move resolution
        self.resolve_actions(self.game.stack["PC"], npc_chosen_moves)
        self.game.locked=False
    # end def

    def resolve_actions(self, pc_moves, npc_moves): # prev: resolve_techniques
        # moves is a list of strings (names of techniques or actions)
        plist=[]

        print(pc_moves)
        
        # PC
        for move in pc_moves:

            data=TECHNIQUES[move]
            if data['sp'] > self.pc.stats.sp:
                data=TECHNIQUES["Attack"] # temporary (default behavior for low SP)
            else:
                self.pc.stats.harm_sp(data['sp'])
            priority = data['priority']
            speed = self.pc.stats.gets("spd")
            plist.append((priority,speed,"PC",data,))

            # negative temporary buffs are applied instantly
            #   (whether or not the tech is successful)
            if data['defense'] < 0: 
                self.pc.stats.dfn_buff += data['defense'] 
            if data['evasion'] < 0:
                self.pc.stats.eva_buff += data['evasion']
        # NPC 
        for move in npc_moves:
            if move=="Rest":
                act_rest(self.npc)
                continue

            data=TECHNIQUES[move]
            if data['sp'] > self.npc.stats.sp:
                data=TECHNIQUES["Attack"] # temporary (default behavior for low SP)
            else:
                self.npc.stats.harm_sp(data['sp'])
            priority = data['priority']
            speed = self.npc.stats.gets("spd")
            plist.append((priority,speed,"NPC",data,))
            
            # " negative temporary buffs
            if data['defense'] < 0: 
                self.npc.stats.dfn_buff += data['defense'] 
            if data['evasion'] < 0:
                self.npc.stats.eva_buff += data['evasion']
                
        # sort by priority first, then by player speed, and finally,
        #   add some randomness for when speed and priorities are equal.
        #   This randomness applies to one of the players in the battle
        #   for this round, for all their techniques. Otherwise, technique 
        #   order is preserved, all else being equal. This allows for
        #   strategies to develop using timing of techniques.
        
        tempo_victor = random.choice(("PC","NPC",)) # choose a tempo winner for tie-breakers
        sortlist = sorted(
            plist, key=lambda x: (x[0], x[1], x[2]==tempo_victor), reverse=True
            )

        self.resolve_actions_sorted(sortlist)

    def resolve_actions_sorted(self, sortlist):

        for item in sortlist:
            priority,speed,combatantName,movedata=item
            
            if combatantName=="PC":
                attkr=self.pc
                dfndr=self.npc
            elif combatantName=="NPC":
                attkr=self.npc
                dfndr=self.pc

            if attkr.dead:
                print("{} is defeated.".format(attkr.name))
                return
            elif dfndr.dead:
                print("{} is defeated.".format(dfndr.name))
                return

            element = movedata['element']
            movename = movedata['name']
            mode = movedata['mode'].lower()
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
            nstrikes = 1

            print("{} used {}!".format(combatantName, movename))

            # decrement the countdown status timers counted by number of actions
            attkr.stats.decrement_status_counters()

            # switch stances to the elemental style of the chosen technique
            attkr.stats.set_stance(ELEMENTS.get(element,{}).get('stance',0))

            # damage
            damage = 0 if dmg==0 else dmg + attkr.stats.gets("dmg")

            # accuracy and determining if we hit...
            accbonus = self.apply_tohit_bonuses(movename, attkr, dfndr)

            hitchance = acc + accbonus + attkr.stats.gets("acc") - dfndr.stats.gets("eva")
            
            # elemental resistances affect accuracy
            if element:
                res = "res_{}".format(ELEMENTS.get(element,{}).get("name","NONE"))
                value = dfndr.stats.gets(res)
                hitchance -= value

            # go through possible failure states for the technique
            failed = False
            if ("Stunned" in attkr.stats.buffs.keys() and random.random()*100 < 25):
                print("In a daze; the attack fails!")
                attkr.stats.heal_sp(spcost) # don't lose SP for this since you didn't do it
                failed=True
            elif (mode!="agile" and self.mode!=mode):
                print("    It failed!")
                attkr.stats.heal_sp(spcost) # don't lose SP for this since you didn't do it
                failed=True
            elif random.random()*100 >= hitchance: # miss
                # still lose SP because you tried but just missed
                print("    It missed!")
                failed=True

            if not failed: # hit

                # apply positive buffs only after successful use of the technique
                if dfn > 0: 
                    self.npc.stats.dfn_buff += dfn
                if eva > 0:
                    self.npc.stats.eva_buff += eva

                # apply special effects for the technique (from "Special" column)
                damage,pierce,disarm,disarm_self,destroy,nstrikes=self.apply_special(
                    attkr, dfndr, movename, damage
                    )

                # standard status effect from element (burning, softened, hypoxic, stunned)
                if status > 0:
                    
                    # increased chance of causing status from elemental mastery
                                # 10%->55%, 60%->80%, 90%->95%, etc.
                                # 0% -> 0%: mastery does not add status effects to techs
                    for e in ['F','E','W','A']:
                        if (element==e and attkr.techs.mastery[e]["status"]):
                            status = round(status + (100-status)//2)
                            
                    if (1+int(random.random()*100)) <= status:
                        for e in ['F','E','W','A']:
                            if element==e:
                                statusType = ELEMENTS[e]['status']
                                dfndr.stats.accumulate_status(statusType, statusDur)
                

                # apply extra damage from stance
                if (damage > 0 and
                    attkr.stats.stance == STANCES[dfndr.stats.stance]['weakness']):
                    damage += 1
                    print("    It's highly effective!")
                    # TODO: consider limits on damage
                        # (only up to 1 extra damage per turn OR dfndr stance resets
                        # after you exploit their weakness.
                
                # apply pierce by reducing defense of the dfndr, down to a minimum of 0.
                # If the dfndr has below 0 defense, no change is made.
                if damage > 0:
                    tdfn = dfndr.stats.gets("dfn")
                    actualDfn = max(min(0,tdfn), tdfn - pierce)
                    actualDmg = max(0, damage - actualDfn)

                    # deal the damage
                    dfndr.stats.harm_hp(actualDmg)
                    print("    It does {} dmg.".format(actualDmg))
                else:
                    actualDmg = 0
                
                # attempt to disarm or destroy weapon based on disarm/destroy stats
                # first, apply buff to destroy stat
                if (destroy > 0 and WEAPONS[attkr.stats.weapon].get("destroy")):
                    destroy = round(destroy + (100-destroy)*(WEAPONS[attkr.stats.weapon]["destroy"]/100))
                if (destroy and random.random()*100 < destroy):
                    dfndr.destroy_weapon() # TODO func body
                    print("    Destroyed weapon of {}.".format(dfndr.name))
                else: # only attempt disarm if destroy fails
                    # first, apply buff to disarm stat
                    if (disarm > 0 and WEAPONS[attkr.stats.weapon].get("disarm")):
                        disarm = round(disarm + (100-disarm)*(WEAPONS[attkr.stats.weapon]["disarm"]/100))
                    # attempt disarm based on disarm stat
                    if (disarm and random.random()*100 < disarm):
                        dfndr.disarm_weapon() # TODO func body
                        print("    Disarmed {}.".format(dfndr.name))
                # possibly disarm self based on disarm_self stat
                if (disarm_self and random.random()*100 < disarm_self):
                    attkr.disarm_weapon() # TODO func body
                    print("    Disarmed {}.".format(attkr.name))

                # movement
                # first apply resistances
                short -= dfndr.stats.gets("res_short")
                wide -= dfndr.stats.gets("res_wide")
                # attempt to go wide or short as the technique may call for
                if (self.mode=="wide" and random.random()*100 < short):
                    self.mode="short"
                    attkr.move_short()
                    dfndr.move_short()
                    print("    Moved short")
                elif (self.mode=="short" and random.random()*100 < wide):
                    self.mode="wide"
                    attkr.move_wide()
                    dfndr.move_wide()
                    print("    Moved wide")

                # interrupt rest
                if dfndr.resting:
                    dfndr.rest_interrupted=True
        # end for
    # end def

    def apply_special(self, attkr, dfndr, movename, damage):
        #       special technique status buffs      #

        pierce = attkr.stats.gets("pierce")
        disarm = 0
        disarm_self = 0
        destroy = 0 # destroy weapon
        nstrikes = 1
                
                    # ~~~ AIR ~~~ 
        if movename == "Pillow of Winds":
            attkr.stats.add_status("Pillow of Winds", 3)
        elif movename == "Suffocate":
            pierce += 2
            dfndr.stats.add_status("Prevent Healing", 2) # this would wear out immediately at end of the current turn, but could be useful still as attacks could still occur after this technique goes off.
        elif movename == "Double Image":
            attkr.stats.add_status("Double Image",4) # +1 Spd
        elif movename == "Cloud Clone":
            attkr.stats.add_status("Cloud Clone",999) 
        elif movename == "Obfuscate":
            pierce += 1
        elif movename == "Disarming Gust":
            disarm = 50
        elif movename == "Submission":
            dfndr.stats.add_status("Prevent Movement", 1)
        elif movename == "Compression Bomb":
            self.try_apply_status(attkr, dfndr, "Stunned", 3, 50, accumulate=True)
        elif movename == "Vacuum Chamber":
            pierce += 6
        elif movename == "Third Eye":
            dfndr.stats.add_status("Third Eye", 6)
        elif movename == "Vortex":
            disarm = 75
        elif movename == "Dust Devils":
            dfndr.stats.add_status("Dust Devils", 2)
        elif movename == "Cloudwalk":
            attkr.stats.add_status("Cloudwalk", 6)
        elif movename == "Zephyr":
            nstrikes = 2
            
                    # ~~~ WATER ~~~ 
        elif movename == "Grab Weapon":
            disarm = 40
        elif movename == "Slippery Skin":
            attkr.stats.add_status("Slippery Skin",3)
        elif movename == "Acid Rain":
            self.try_apply_status(attkr, dfndr, "Toxic", 2, 33, accumulate=True)
        elif movename == "Dissolve":
            self.try_apply_status(attkr, dfndr, "Toxic", 3, 33, accumulate=True)
        elif movename == "Guiding Line":
            pierce += 1
            attkr.stats.add_status("Guiding Line",3)
        elif movename == "Jet Stream":
            if self.mode=="short":
                pierce += 1
        elif movename == "Liquefy":
            attkr.stats.add_status("Liquefy",3)
        elif movename == "Heal":
            attkr.stats.add_status("Heal",4)
        elif movename == "Icicle":
            pierce += 2
        elif movename == "Mend":
            attkr.stats.heal_hp(5)
        elif movename == "Mana Rain":
            attkr.stats.add_status("Mana Rain", 6)
        elif movename == "Purify":
            attkr.stats.purify()
        elif movename == "Pressure Beam":
            pierce += 2
        elif movename == "Frostbite":
            self.try_apply_status(attkr, dfndr, "Burning", 6, 50, accumulate=True)
        elif movename == "Tentacle":
            dfndr.stats.accumulate_status("Prevent Movement", 3)
        elif movename == "Medusa":
            nstrikes = 2
            self.try_apply_status(attkr, dfndr, "Stunned", 2, 50, accumulate=True)
        
                    # ~~~ FIRE ~~~ 
        elif movename == "Singe":
            pierce += 1
        elif movename == "Cannon Calves":
            attkr.stats.add_status("Grasshopper", 4)
        elif movename == "Burning Net":
            attkr.stats.add_status("Prevent Movement", 3)
        elif movename == "Hot Temper":
            dfndr.stats.add_status("Hot Temper", 2)
        elif movename == "Lightning Bolt":
            pierce += 3
        elif movename == "Static Grip":
            attkr.stats.add_status("Prevent Movement", 3)
        elif movename == "Overdrive":
            self.try_apply_status(attkr, dfndr, "Hypoxic", 3, 90, accumulate=True)
        elif movename == "Conduction":
            disarm = 90
        
                    # ~~~ EARTH ~~~ 
        elif movename == "Harden":
            attkr.stats.add_status("Harden", 3)
        elif movename == "Sandstorm":
            attkr.stats.add_status("Prevent Healing", 3)
        elif movename == "Drill":
            pierce += 1
        elif movename == "Constrict":
            pierce += 2
            if dfndr.stats.get_status("Stunned"):
                damage += 1
        elif movename == "Missile Weapon":
            disarm_self = 100
        elif movename == "Armorslayer":
            # damage scales with dfndr's Defense stat
            dfn = dfndr.stats.gets("dfn")
            damage = 1
            if dfn > 0:
                damage += dfn
                pierce += dfn     # pierce through all of the defense
        elif movename == "Vibrohammer":
            self.try_apply_status(attkr, dfndr, "Softened", 3, 33, accumulate=True)
        elif movename == "Wall of Clay":
            attkr.stats.add_status("Wall of Clay", 6)
        elif movename == "Earthwave":
            pierce += 2
        elif movename == "Diamond Smash":
            pierce += 1
            if self.mode=="wide":
                damage += 1
        elif movename == "Lockdown":
            dfndr.stats.add_status("Prevent Movement", 3)
        elif movename == "Solid Guard":
            attkr.stats.add_status("Solid Guard", 1) # TODO: implement!
        elif movename == "Leverage Weapon":
            disarm = 100
        elif movename == "Shatter Weapon":
            destroy = 50 # TODO: implement!
            disarm = 100
        elif movename == "Suppressing Sands":
            dfndr.stats.clear_status()
        elif movename == "Grounding":
            attkr.stats.purify()

        return (damage, pierce, disarm, disarm_self, destroy, nstrikes)

    # apply bonuses to-hit from technique special abilities
    def apply_tohit_bonuses(self, movename, attkr, dfndr):
        acc = 0
        if (movename == "Targeted Combustion" and dfndr.stats.get_status("Burning")):
            acc += 30
        return acc



    def upkeep(self, combatant):
        if "Heal" in combatant.stats.buffs.keys():
            combatant.stats.heal_hp(1)
        if "Mana Rain" in combatant.stats.buffs.keys():
            combatant.stats.heal_sp(1)
        if "Burning" in combatant.stats.buffs.keys():
            combatant.stats.harm_hp(1)
        if "Toxic" in combatant.stats.buffs.keys():
            combatant.stats.harm_hp(1)
        
        combatant.stats.decrement_turn_timers()
        
# end class




