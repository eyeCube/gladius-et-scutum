'''
    gladius.py

    Gladius et Scutum - Jane Wharton

    
'''

import pygame
import random

from const import *
import ui

pygame.init()
WIDTH=1024
HEIGHT=768
SURFACE = pygame.display.set_mode([WIDTH, HEIGHT])

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
    def __init__(self, pc):
        self.locked=False   # used to lock out player input
        
        self.pc=pc
        self.pc_level = 1

        # tech registry stack
        self.register_init()
        
        # Menu initialization
        self.menus={}
        self.menus_toAdd={}
        self.menus_toRemove=[]

        # main menu
        mainMenu = ui.ButtonGroup(
            SURFACE, name="menu_main", enabled=False,
            x=WIDTH/2-64, y=HEIGHT/2-64
            )
        self.menu_add("menu_main", mainMenu)
        ui.Button(mainMenu, name="New Game", x1=0,y1=0,width=128,height=32, action=self.test)
        ui.Button(mainMenu, name="Load", x1=0,y1=1*32,width=128,height=32, action=self.test)
        ui.Button(mainMenu, name="Quit", x1=0,y1=2*32,width=128,height=32, action=self.test)

        self.menu_switch_focus("menu_main")

        

    # menus #
    
    def handle_menus(self):
        for name, menu in self.menus_toAdd.items():
            self._menu_add(name, menu)
        for name in self.menus_toRemove:
            self._menu_remove(name)
        self.menus_toAdd = {}
        self.menus_toRemove = []
    def menu_add(self, name, menu):
        self.menus_toAdd.update({name : menu})
    def menu_remove(self, name):
        self.menus_toRemove.append(name)
    def _menu_add(self, name, menu):
        self.menus.update({name : menu})
    def _menu_remove(self, name):
        if self.menus.get(name):
            del self.menus[name]
    def menu_disable(self, name):
        if self.menus.get(name):
            self.menus[name].disable()
    def menu_enable(self, name):
        if self.menus.get(name):
            self.menus[name].enable()
    def menu_switch_focus(self, menu):
        self.menu_in_focus = menu
    def menu_up_directory(self):
        if self.menu_in_focus == "menu_b":
            self.menu_remove("menu_b")
            self.menu_in_focus = "menu_a"
        elif self.menu_in_focus == "menu_c":
            self.menu_remove("menu_c")
            self.menu_in_focus = "menu_b"
        elif self.menu_in_focus == "menu_d":
            self.menu_remove("menu_d")
            self.menu_in_focus = "menu_c"

    # battle #

    def init_battle(self, battle):
        self.battle=battle
        self._create_battle_menu(battle)
    def _create_battle_menu(self, battle):
        battleMenu = ui.ButtonGroup(
            SURFACE, name="menu_a", enabled=True,
            x=0, y=HEIGHT-256
            )
        self.menu_add("menu_a", battleMenu)
        self.menu_switch_focus("menu_a")
        ui.Button(battleMenu, name="--> Continue", x1=0,y1=0,width=196,height=32,
                  action=self.action_continue, args=[self.battle], hotkey=pygame.K_1)
            # TODO: make this ^ button say "Rest" if NRG == 3
        ui.Button(battleMenu, name="Attack", x1=0,y1=1*32,width=196,height=32,
                  action=self.action_attack, args=[], hotkey=pygame.K_2)
        ui.Button(battleMenu, name="Technique", x1=0,y1=2*32,width=196,height=32,
                  action=self.action_technique, args=[], hotkey=pygame.K_3)
        ui.Button(battleMenu, name="Study", x1=0,y1=3*32,width=196,height=32,
                  action=self.action_study, args=[], hotkey=pygame.K_4)
        ui.Button(battleMenu, name="Claim Boon", x1=0,y1=4*32,width=196,height=32,
                  action=self.action_boon, args=[], hotkey=pygame.K_5)
        ui.Button(battleMenu, name="Retrieve Weapon", x1=0,y1=5*32,width=196,height=32,
                  action=self.action_retrieve, args=[], hotkey=pygame.K_6)
            # TODO: make this ^ button say "Drop Weapon" if weapon is equipped, and do drop function
        ui.Button(battleMenu, name="Suspend Match", x1=0,y1=6*32,width=196,height=32,
                  action=self.action_suspend, args=[], hotkey=pygame.K_7)
        ui.Button(battleMenu, name="Forfeit", x1=0,y1=7*32,width=196,height=32,
                  action=self.action_forfeit, args=[], hotkey=pygame.K_8)

    # level B menus #
    
    def create_element_menu(self): # technique element menu
        print("create element menu") 
        techTypeMenu = ui.ButtonGroup(
            SURFACE, name="menu_b", enabled=True,
            x=196, y=HEIGHT-256
            )
        self.menu_add("menu_b", techTypeMenu)
        self.menu_switch_focus("menu_b")
        self.menu_remove("menu_c")
        self.menu_remove("menu_d")
        ui.Button(techTypeMenu, name="Fire", x1=0,y1=0,width=196,height=32,
                  action=self.create_level_menu, args=["fire"], hotkey=pygame.K_1)
        ui.Button(techTypeMenu, name="Earth", x1=0,y1=1*32,width=196,height=32,
                  action=self.create_level_menu, args=["earth"], hotkey=pygame.K_2)
        ui.Button(techTypeMenu, name="Air", x1=0,y1=2*32,width=196,height=32,
                  action=self.create_level_menu, args=["air"], hotkey=pygame.K_3)
        ui.Button(techTypeMenu, name="Water", x1=0,y1=3*32,width=196,height=32,
                  action=self.create_level_menu, args=["water"], hotkey=pygame.K_4)

    # level C menus #
    
    def create_level_menu(self, args): # technique level selection menu
        element=args[0]
        print("create level menu for", element)
        techLevelMenu = ui.ButtonGroup(
            SURFACE, name="menu_c", enabled=True,
            x=2*196, y=HEIGHT-256
            )
        self.menu_add("menu_c", techLevelMenu)
        self.menu_switch_focus("menu_c")
        self.menu_remove("menu_d")
        # add each level that you have a technique for of this element
        for i in range(MAX_TECH_LEVEL):
            if self.pc.techs.techniques.get(element,{}).get(i+1):
                ui.Button(
                    techLevelMenu, name=(i+1), x1=0, y1=32*i, width=196, height=32,
                    action=self.create_tech_menu, args=[element, (i+1)]
                    )

    # level D menus #
    
    def create_tech_menu(self, args): # technique selection menu
        element, level = args
        print("create tech menu for {}, lv{}".format(element, level))
        techMenu = ui.ButtonGroup(
            SURFACE, name="menu_d", enabled=True,
            x=3*196, y=HEIGHT-256
            )
        self.menu_add("menu_d", techMenu)
        self.menu_switch_focus("menu_d")
        # add each known technique that matches the element / level
        i=0
        for tech in self.pc.techs.techniques[element][level]:
            ui.Button(
                techMenu, name=tech, x1=0,y1=32*i, width=196,height=32,
                action=self.register_tech, args=tech
                )
            i+=1

    # actions #
    
    def action_attack(self, args):
        print("Attack")
        self.register_tech("Attack")

    def action_technique(self, args):
        print("Technique")
        self.create_element_menu()

    def action_study(self, args):
        print("Study")

    def action_boon(self, args):
        print("Boon")

    def action_retrieve(self, args):
        print("Retrieve")

    def action_suspend(self, args):
        print("Suspend")

    def action_forfeit(self, args):
        print("Forfeit")

    def action_continue(self, args):
        print("Continue")
        # if you don't have any techs or attacks in the stack, you just do rest action
        self.pc.resting = True if not self.stack["PC"] else False
        self.pc.rest_interrupted = False
        # enemy chooses actions, combat plays out, then go to next round
        self.battle.turn_end()
        if self.pc.resting:
            self._action_rest(self.pc.rest_interrupted)
        self.battle.turn_begin() # prompt user for input again

    def _action_rest(self, interrupted):
        print("Rest. Interrupted:",interrupted)
        self.pc.stats.heal_sp(1 if interrupted else 3)
        

            # tech registry stack #
    def register_tech(self, tech):
        # add the chosen technique to the stack. It will appear in a list on screen.
        # Once you choose CONFIRM, the battle round begins, the enemy selects their moves,
        # the moves are ordered by priority and speed, and then the technique() function
        # is called for each move in the proper order.
        nrg_cost = TECHNIQUES[tech]["nrg"]
        sp_cost = TECHNIQUES[tech]["sp"]
        print(self.pc.stats.energy)
        if (self.pc.stats.energy >= nrg_cost and self.pc.stats.sp >= sp_cost):
            print("tech registered:", tech)
            self.stack["PC"].append(tech)
            self.pc.stats.energy -= nrg_cost
            self.pc.stats.sp -= sp_cost
            print(self.pc.stats.energy)
        else:
            print("Insufficient energy and/or sp to use this tech")
    def register_backspace(self): # remove most recently registered tech
        if self.stack["PC"]:
            print("tech removed")
            tech = self.stack["PC"][-1]
            self.pc.stats.energy += TECHNIQUES[tech]["nrg"]
            self.pc.stats.sp += TECHNIQUES[tech]["sp"]
            del self.stack["PC"][-1]
    def register_init(self): # clear registered techs from tech registry stack
        self.stack = {"PC":[], "NPC":[]}
    # follow through and actually do a tech, once it's finally time
    def technique(self, tech):
        print("Performing tech ", tech)
        
    
    def level_up(self):
        self.pc_level += 1
        # choose what to improve!
        # HP + 1
        # SP + 1
        # Skill + 1
        stats = self.pc.stats
        print('''Level up!\nChoose what to improve!
b ...... Body (HP)
s ...... Spirit (SP)
t ...... Technique''')
        while True:
            inp = input("> ")
            chosen=None
            if inp=="b":
                chosen="body"
            elif inp=="s":
                chosen="spirit"
            elif inp=="t":
                chosen="skill"
            if chosen:
                stats.improve_core_attribute(chosen, 1)
            else:
                print("Try again... :(")

    def run(self):
        mouse = pygame.mouse.get_pos()

        # event phase
        
        for ev in pygame.event.get(): 
      
            if ev.type == pygame.QUIT: 
                pygame.quit()

            if not self.locked:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.check_menus_mouse(mouse)
                if ev.type == pygame.KEYDOWN:
                    self.check_menus_button(ev.key)
                    if ev.key==pygame.K_ESCAPE:
                        self.menu_up_directory()

        # game upkeep #

        self.handle_menus() # update menu stuff

        # draw phase #
        
        SURFACE.fill((30,70,70))
        self.draw_menus()
        pygame.display.flip()
    # end def

    def draw_menus(self):
        for menu in self.menus.values():
            menu.drawAll()

    def check_menus_mouse(self, mouse):
        for menu in self.menus.values():
            menu.checkAll(mouse, isMouse=True)

    def check_menus_button(self, key):
        for name,menu in self.menus.items():
            if name==self.menu_in_focus:
                menu.checkAll(key, isMouse=False)

    def test(self, args):
        print("TEST SUCCESS!! {}".format(args))
# end class


class Battle:
    def __init__(self, game, pc, npc):
        self.game=game
        self.pc=pc
        self.npc=npc
        self.mode="wide"

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
        npc_techs = self.npc.techs
        npc_chosen_moves=[]
        #temporary
        npc_chosen_moves.append("Firebolt")
        npc_chosen_moves.append("Flame Whip")
        # spend SP (TODO)

        # rest
        self.npc.resting=False
        self.npc.rest_interrupted=False

        # move resolution
        self.resolve_techniques(self.game.stack["PC"], npc_chosen_moves)
        self.game.locked=False
    # end def

    def resolve_techniques(self, pc_moves, npc_moves):
        plist=[]
        
        # PC
        for move in pc_moves:
            data=TECHNIQUES[move]
            priority = data['priority']
            speed = self.pc.stats.get("spd")
            plist.append((priority,speed,"PC",data,))

            # temporary buffs (until beginning of next turn) are applied instantly
            if data['defense'] != 0: 
                self.pc.stats.dfn_buff += dfn 
            if data['evasion'] != 0:
                self.pc.stats.eva_buff += eva
        # NPC 
        for move in npc_moves:
            data=TECHNIQUES[move]
            priority = data['priority']
            speed = self.npc.stats.get("spd")
            plist.append((priority,speed,"NPC",data,))
            
            # " temporary buffs
            if data['defense'] != 0:
                self.npc.stats.dfn_buff += dfn 
            if data['evasion'] != 0:
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
            
            player.stats.sp -= spcost
            player.stats.energy -= nrgcost

            damage = dmg + player.stats.get("dmg")
            tohit = acc + player.stats.get("acc")
            tohit -= target.stats.get("eva")

            print("{} used {}!".format(playerName, movename))

            # decrement the countdown status timers counted by number of actions
            player.stats.decrement_status_counters()

            # go through possible failure states for the technique
            failed = False
            if ("Stunned" in player.stats.buffs.keys() and random.random()*100 < 25):
                print("In a daze; the attack fails!")
                failed=True
            elif (mode!="both" and self.mode!=mode):
                print("    It failed!")
                failed=True
            elif random.random()*100 >= tohit: # miss
                print("    It missed!")
                failed=True
                
            if not failed: # hit

                # apply special effects for the technique (from "Special" column)
                damage, pierce, disarm, destroy = self.apply_special(
                    player, target, movename, damage
                    )

                # standard status effect from element (burning, softened, hypoxic, stunned)
                if status > 0:
                    
                    # increased chance of causing status from elemental mastery
                                # 10%->55%, 60%->80%, 90%->95%, etc.
                                # 0% -> 0%: mastery does not add status effects to techs
                    for e in ['F','E','W','A']:
                        if (element==e and player.techs.mastery[e]["status"]):
                            status = round(status + (100-status)//2)
                            
                    if (1+int(random.random()*100)) <= status:
                        for e in ['F','E','W','A']:
                            if element==e:
                                statusType = ELEMENTS[e]['status']
                                target.stats.accumulate_status(statusType, statusDur)
                
                
                # apply pierce by reducing defense of the target, down to a minimum of 0.
                # If the target has below 0 defense, no change is made.
                targetDfn = max(
                    min(0,target.stats.get("dfn")),
                    target.stats.get("dfn") - pierce
                    )
                actual_dmg = max(0, damage - targetDfn) if damage > 0 else 0
                print("    It does {} dmg!".format(actual_dmg))

                # deal damage
                target.stats.harm_hp(actual_dmg)
                
                # attempt to disarm or destroy weapon based on disarm/destroy stats
                if WEAPONS[self.weapon].get("destroy"): # first, apply buff to destroy stat
                    destroy = round(destroy + (100-destroy)*(WEAPONS[self.weapon]["destroy"]/100))
                if (destroy and random.random()*100 < destroy):
                    target.stats.destroy_weapon() # TODO func body
                    print("Destroyed weapon of {}".format(target.name))
                else: # only attempt disarm if destroy fails
                    if WEAPONS[self.weapon].get("disarm"): # first, apply buff to disarm stat
                        disarm = round(disarm + (100-disarm)*(WEAPONS[self.weapon]["disarm"]/100))
                    # attempt disarm based on disarm stat
                    if (disarm and random.random()*100 < disarm):
                        target.stats.disarm() # TODO func body
                        print("Disarmed {}".format(target.name))

                # attempt to go wide or short as the technique may call for
                if (self.mode=="wide" and random.random()*100 < short):
                    self.mode="short"
                    player.move_short()
                    target.move_short()
                    print("Moved short")
                elif (self.mode=="short" and random.random()*100 < wide):
                    self.mode="wide"
                    player.move_wide()
                    target.move_wide()
                    print("Moved wide")

                # interrupt rest
                if target.resting:
                    target.rest_interrupted=True
        # end for
    # end def

    def apply_special(self, player, target, movename, damage):
        #       special technique status buffs      #

        pierce = player.stats.get("pierce")
        disarm = 0
        destroy = 0 # destroy weapon
                
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
        elif movename == "Compression Bomb":
            if random.random()*100 < 50:
                player.stats.accumulate_status("Stunned", 3)
        elif movename == "Vacuum Chamber":
            pierce += 6
        elif movename == "Third Eye":
            target.stats.add_status("Third Eye", 6)
        elif movename == "Vortex":
            disarm = 75
        elif movename == "Dust Devils":
            target.stats.add_status("Dust Devils", 2)
            
                    # ~~~ WATER ~~~ 
        elif movename == "Grab Weapon":
            disarm = 40
        elif movename == "Slippery Skin":
            player.stats.add_status("Slippery Skin",3)
        elif movename == "Acid Rain":
            value = 67 if player.techs.mastery["water"]["status"] else 33
            if random.random()*100 < value:
                target.stats.accumulate_status("Toxic",2)
        elif movename == "Dissolve":
            value = 67 if player.techs.mastery["water"]["status"] else 33
            if random.random()*100 < value:
                target.stats.accumulate_status("Toxic",3)
        elif movename == "Jet Stream":
            if self.mode=="short":
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
        elif movename == "Pressure Beam":
            pierce += 2
        elif movename == "Frostbite":
            if random.random()*100 < 50:
                target.stats.accumulate_status("Burning", 6)
        elif movename == "Tentacle":
            target.stats.accumulate_status("Prevent Movement", 3)
        
                    # ~~~ FIRE ~~~ 
        elif movename == "Singe":
            pierce += 1
        elif movename == "Grasshopper":
            player.stats.add_status("Grasshopper", 4)
        elif movename == "Burning Net":
            player.stats.add_status("Prevent Movement", 3)
        elif movename == "Flaming Aura":
            target.stats.add_status("Flaming Aura", 2)
        elif movename == "Lightning Bolt":
            pierce += 3
        elif movename == "Static Grip":
            player.stats.add_status("Prevent Movement", 3)
        elif movename == "Overdrive":
            if random.random()*100 < 90:
                player.stats.accumulate_status("Hypoxic", 3)
        elif movename == "Conduction":
            disarm = 90
        
                    # ~~~ EARTH ~~~ 
        elif movename == "Harden":
            player.stats.add_status("Mana Rain", 6)
        elif movename == "Sandstorm":
            player.stats.add_status("Prevent Healing", 3)
        elif movename == "Drill":
            pierce += 1
        elif movename == "Constrict":
            pierce += 1
        elif movename == "Armorslayer":
            pierce += 4
            if target.stats.get("dfn") <= 0:
                damage = 1
        elif movename == "Vibrohammer":
            if random.random()*100 < 33:
                player.stats.accumulate_status("Softened", 3)
        elif movename == "Wall of Clay":
            player.stats.add_status("Wall of Clay", 6)
        elif movename == "Earthwave":
            pierce += 2
        elif movename == "Diamond Smash":
            pierce += 1
        elif movename == "Lockdown":
            target.stats.add_status("Prevent Movement", 3)
        elif movename == "Solid Guard":
            target.stats.add_status("Prevent Movement", 3)
        elif movename == "Leverage Weapon":
            target.stats.add_status("Prevent Movement", 3)
        elif movename == "Shatter Weapon":
            destroy = 50
            disarm = 100
        elif movename == "Suppressing Sands":
            player.stats.clear_status()
        elif movename == "Grounding":
            player.stats.purify()

        return (damage, pierce, disarm, destroy)


    def upkeep(self, player):
        if "Heal" in player.stats.buffs.keys():
            player.heal_hp(1)
        if "Mana Rain" in player.stats.buffs.keys():
            player.heal_sp(1)
        if "Burning" in player.stats.buffs.keys():
            player.harm_hp(1)
        if "Toxic" in player.stats.buffs.keys():
            player.harm_hp(1)
        
        player.stats.decrement_turn_timers()
        
# end class


class Combatant_Stats:
    def __init__(self, owner=None, weapon=0, favorite_weapon=0):
        self.owner=owner
        self.weapon=weapon
        self.favorite_weapon=favorite_weapon
        self.lost_weapon=0
        
        self.update_needed = True
        self.buffs={}

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
        self.dmg_base=1         # start at 1 to make combat more interesting and brutal
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

    def improve_core_attribute(self, stat, add_value):
        self.__dict__[stat] += add_value
        self.update_needed = True

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

    def add_status(self, status, duration):
        self.buffs.update({status : duration})
        self.update_needed = True
        print("Added status to {}: {} for {}".format(self.owner.name, status, statusDur))
    def remove_status(self, status):
        del self.buffs[status]
        self.update_needed = True
        print("Removed status from {}: {} for {}".format(self.owner.name, status, statusDur))
    def accumulate_status(self, status, duration):
        # add the status if it doesn't exist, or if it does, add to the duration.
        if status in self.buffs.keys():
            self.buffs.update({status : self.buffs[status] + duration})
        else:
            self.add_status(status, duration)
        print("Accumulated status to {}: {} for {}".format(self.owner.name, status, statusDur))

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
               "Slippery Skin", "Liquefy", "Heal", "Mana Rain", "Toxic"
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

        # set because there is no base value for pierce
        self.pierce = WEAPONS[self.weapon].get("pierce", 0)
        print(self.pierce)

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
            elif k=="Dust Devils":
                self.dmg_wide += 1
            elif k=="Flaming Aura":
                self.dmg_short += 1
            elif k=="Grasshopper":
                self.spd += 1
        # end for
            
        
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
            
    # end def
        
# end class


class Combatant_Techniques:
    def __init__(self, favorite_element=None):
        self.techniques={ "fire":{}, "earth":{}, "air":{}, "water":{} }
        # example: {"fire": {1: ["Firebolt",],},
        self.favorite_element=favorite_element
        self.mastery={
            "F":{"hit":0, "status":False},
            "E":{"hit":0, "status":False},
            "A":{"hit":0, "status":False},
            "W":{"hit":0, "status":False},
            }

    def add_tech(self, tech):
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

    def learn_tech(self, owner, tech):
        data = TECHNIQUES[tech]
        reqSkill = data["req-skill"]
        if ELEMENTS[data["element"]]['name']==self.favorite_element:
            reqSkill -= 2
        if owner.stats.skill >= reqSkill:
            self.add_tech(tech)
            return True
        return False

    def draw_terse(self, surface, x,y, tech): # show brief info as it appears in lists
        pass

    def draw_details(self, surface, x,y, tech, show_reqs=True): # show detailed information for technique
        font = pygame.font.SysFont("consolas", 18)
        data = TECHNIQUES[tech]
        
        if show_reqs:
            reqs='''
    Req. Techs: {reqs}
    Req. Skill: {skill}'''.format(reqs=data['pre-reqs'], skill=data['req-skill'])
        else:
            reqs=""

        spec='''
{hit}{dmg}{dfn}{eva}{short}{wide}{status}{statusDur}{special}{desc}'''.format(
    hit="    Hit: {}%\n".format(data['hit']) if data['hit']>0 else "",
    dmg="    DMG: {}\n".format(data['damage']) if data['damage']>0 else "",
    dfn="    DFN: {}\n".format(data['defense']) if data['defense']>0 else "",
    eva="    EVA: {}\n".format(data['evasion']) if data['evasion']>0 else "",
    short="    {}% chance to move Short\n".format(data['short']) if data['short']>0 else "",
    wide="    {}% chance to move Wide\n".format(data['wide']) if data['wide']>0 else "",
    status="    {}% chance target is {} for {} actions\n".format(
        data['status'], ELEMENTS[data['element']['status'], data['statusDur']
        ) if data['status']>0 else "",
    special="    Special: {}\n".format(data['special']) if data['special'] else "",
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
    priority=data['priority']
),
            True, BLACK
            )
        
        surface.blit(text, (x,y,))
# end class
        

    
class PlayerCharacter: # class PC class and non-player character NonPlayerCharacter
    def __init__(self, name="", favorite_element=0, weapon=0, pc=False, sprite=None):
        self.stats = Combatant_Stats(owner=self, weapon=weapon, favorite_weapon=weapon)
        self.techs = Combatant_Techniques(favorite_element)
        self.name = name
        self.pc=pc
        self.sprite=sprite
        self.mode = "wide"
        self.resting = False
        self.rest_interrupted = False
        self.stale_moves = 0        # counter for doing the same move x times in a row
                                    # reduce accuracy proportional to this value
        
    def move_wide(self):
        self.mode = "wide"
        self.stats.update_needed=True
    def move_short(self):
        self.mode = "short"
        self.stats.update_needed=True

    def update_sprite(self):
        # TODO: call this when updating weapon / disarming / rearming etc.
        if self.pc:
            self.sprite = PC_WEAPON_SPRITES[self.weapon]

    def draw(self, surface):
        if self.sprite==None:
            print("self.sprite value for player with name '{}' is None.".format(self.name))
            return
        
        ypos=300
        if self.pc:
            xpos=200
        else:
            xpos=WIDTH-200

        # draw the sprite
        surface.blit(self.sprite, (xpos,ypos,))
# end class


if __name__=="__main__":

    pc = PlayerCharacter(
            name="Jaen", 
            favorite_element=ELEM_AIR,
            weapon=WPN_SLING,
            pc=True
            ) # temporary auto-populated test data
    game = Game(pc)
    
    npc=PlayerCharacter(
        name="Bob",
        favorite_element=ELEM_FIRE,
        weapon=WPN_HAMSHIELD
        ) #temporary

    pc.stats.calculate_stats()
    npc.stats.calculate_stats()

    print("OPEN")

    battle=Battle(game, pc, npc)
    game.init_battle(battle)

    battle.turn_begin()
    while True:
        game.run()
    
    




