
import pygame

from const import *
import ui as uipy
import ai as aipy
import battle as battlepy


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
        mainMenu = uipy.UIGroup(
            SURFACE, name="menu_main", enabled=False,
            x=WIDTH/2-64, y=HEIGHT/2-64
            )
        self.menu_add("menu_main", mainMenu)
        uipy.Button(mainMenu, name="New Game", x=0,y=0,width=128,height=32, action=self.test)
        uipy.Button(mainMenu, name="Load", x=0,y=1*32,width=128,height=32, action=self.test)
        uipy.Button(mainMenu, name="Quit", x=0,y=2*32,width=128,height=32, action=self.test)

        self.menu_switch_focus("menu_main")

        self.delayed_actions = {}

    def begin_battle(self, level):
        '''
        npc=PlayerCharacter(
            name="Bob",
            favorite_element=ELEM_FIRE,
            weapon=WPN_POLE,
            sprite=SPR_PLAYER_POLE # TODO: equip function that edits sprite and weapon and sets update needed to True for stats obj
            ) #temporary'''
        
        print("OPEN battle")
        npc_ai = aipy.LEVELS[level](self.pc)
        self.npc = npc_ai.npc
        battle=battlepy.Battle(self, self.pc, self.npc)
        self.init_battle(battle, self.pc, self.npc)
        self.pc.stats.calculate_stats()
        self.npc.stats.calculate_stats()
        
        battle.turn_begin()
        while True:
            if self.pc.dead:
                break
            elif self.npc.dead:
                break
            self.run()
        print("CLOSE battle")

        
        #-----------------#
        #     menus       #
        #-----------------#
    
    def handle_menus(self):
        for name, menu in self.menus_toAdd.items():
            self.menus.update({name : menu})
        for name in self.menus_toRemove:
            if self.menus.get(name):
                del self.menus[name]
        self.menus_toAdd = {}
        self.menus_toRemove = []
    def menu_add(self, name, menu):
        self.menus_toAdd.update({name : menu})
    def menu_remove(self, name):
        self.menus_toRemove.append(name)
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

    # chargen -- character generation #
    def _create_chargen_menu(self):
        chargenMenu = uipy.UIGroup(
            SURFACE, name="menu_chargen", enabled=True,
            x=64, y=32
            )
        self.menu_add("menu_chargen", chargenMenu)
        self.menu_switch_focus("menu_chargen")
        uipy.Input(chargenMenu, label="Name: ", x=0,y=0, width=192,height=32,
                 action=_finish_chargen)

    def _finish_chargen(self): # finalize character generation, apply stat changes, etc.
        # TODO
        self.menu_remove("menu_chargen")

    # battle #

    def init_battle(self, battle, pc, npc):
        self.battle=battle
        self._create_battle_menu(battle)
        # fully heal the combatants
        battle.pc.stats.heal_sp(9999) 
        battle.pc.stats.heal_hp(9999)
        battle.npc.stats.heal_sp(9999)
        battle.npc.stats.heal_hp(9999)
        self.npc = npc
    def _create_battle_menu(self, battle):
        battleMenu = uipy.UIGroup(
            SURFACE, name="menu_a", enabled=True,
            x=0, y=HEIGHT-9*32
            )
        self.menu_add("menu_a", battleMenu)
        self.menu_switch_focus("menu_a")
        uipy.Button(battleMenu, name="--> Continue", x=0,y=0,width=192,height=32,
                  action=self.action_continue, args=[self.battle], hotkey=pygame.K_1)
            # TODO: make this ^ button say "Rest" if NRG == 3
        uipy.Button(battleMenu, name="Attack", x=0,y=1*32,width=192,height=32,
                  action=self.action_attack, args=[], hotkey=pygame.K_2)
        uipy.Button(battleMenu, name="Technique", x=0,y=2*32,width=192,height=32,
                  action=self.action_technique, args=[], hotkey=pygame.K_3)
        uipy.Button(battleMenu, name="Study", x=0,y=3*32,width=192,height=32,
                  action=self.action_study, args=[], hotkey=pygame.K_4)
        uipy.Button(battleMenu, name="Claim Boon", x=0,y=4*32,width=192,height=32,
                  action=self.action_boon, args=[], hotkey=pygame.K_5)
        uipy.Button(battleMenu, name="Taunt", x=0,y=5*32,width=192,height=32,
                  action=self.action_taunt, args=[], hotkey=pygame.K_6)
        uipy.Button(battleMenu, name="Retrieve Weapon", x=0,y=6*32,width=192,height=32,
                  action=self.action_retrieve, args=[], hotkey=pygame.K_7)
            # TODO: make this ^ button say "Drop Weapon" if weapon is equipped, and do drop function
        uipy.Button(battleMenu, name="Suspend Match", x=0,y=7*32,width=192,height=32,
                  action=self.action_suspend, args=[], hotkey=pygame.K_8)
        uipy.Button(battleMenu, name="Forfeit", x=0,y=8*32,width=192,height=32,
                  action=self.action_forfeit, args=[], hotkey=pygame.K_9)

        #-------------------------#
        #     level B menus       #
        #-------------------------#
    
    # technique button -> tech element selection
    def create_element_menu(self, button): # technique element menu
        if self.menus.get("menu_a", None):
            self.menus["menu_a"].deselect_all()
        button.selected = True
        techTypeMenu = uipy.UIGroup(
            SURFACE, name="menu_b", enabled=True,
            x=192, y=HEIGHT-9*32
            )
        self.menu_add("menu_b", techTypeMenu)
        self.menu_switch_focus("menu_b")
        self.menu_remove("menu_c")
        self.menu_remove("menu_d")
        uipy.Button(techTypeMenu, name="Fire", x=0,y=0,width=192,height=32,
                  action=self.action_create_level_menu, args=["fire"], hotkey=pygame.K_1)
        uipy.Button(techTypeMenu, name="Earth", x=0,y=1*32,width=192,height=32,
                  action=self.action_create_level_menu, args=["earth"], hotkey=pygame.K_2)
        uipy.Button(techTypeMenu, name="Air", x=0,y=2*32,width=192,height=32,
                  action=self.action_create_level_menu, args=["air"], hotkey=pygame.K_3)
        uipy.Button(techTypeMenu, name="Water", x=0,y=3*32,width=192,height=32,
                  action=self.action_create_level_menu, args=["water"], hotkey=pygame.K_4)

        #-------------------------#
        #     level C menus       #
        #-------------------------#
    
    # tech element selection -> tech level selection
    def action_create_level_menu(self, button, args): # technique level selection menu
        element=args[0]
        if self.menus.get("menu_b", None):
            self.menus["menu_b"].deselect_all()
        button.selected = True
        techLevelMenu = uipy.UIGroup(
            SURFACE, name="menu_c", enabled=True,
            x=2*192, y=HEIGHT-9*32
            )
        self.menu_add("menu_c", techLevelMenu)
        self.menu_switch_focus("menu_c")
        self.menu_remove("menu_d")
        # add each level that you have a technique for of this element
        for i in range(MAX_TECH_LEVEL):
            if self.pc.techs.techniques.get(element,{}).get(i+1):
                uipy.Button(
                    techLevelMenu, name="Level {}".format(i+1),
                    x=0, y=32*i, width=192, height=32,
                    action=self.action_create_tech_menu, args=[element, (i+1)]
                    )

        #-------------------------#
        #     level D menus       #
        #-------------------------#
    
    # tech level selection -> specific tech selection
    def action_create_tech_menu(self, button, args): # technique selection menu
        element, level = args
        print("create tech menu for {}, lv{}".format(element, level))
        if self.menus.get("menu_c", None):
            self.menus["menu_c"].deselect_all()
        button.selected = True
        techMenu = uipy.UIGroup(
            SURFACE, name="menu_d", enabled=True,
            x=3*192, y=HEIGHT-9*32
            )
        self.menu_add("menu_d", techMenu)
        self.menu_switch_focus("menu_d")
        # add each known technique that matches the element / level
        i=0
        for tech in self.pc.techs.techniques[element][level]:
            uipy.Button(
                techMenu, name=tech, x=0,y=32*i, width=192,height=32,
                action=self.action_register_tech, args=tech,
                hover_action=self.action_show_tech, hover_args=tech
                )
            i+=1

        #-------------------#
        #     actions       #
        #-------------------#
    
    def action_attack(self, button, args):
        print("Attack")
        self.action_register_tech(button, "Attack")

    def action_technique(self, button, args):
        print("Technique")
        self.create_element_menu(button)
        button.selected = True

    def action_study(self, button, args):
        print("Study")

    def action_boon(self, button, args):
        print("Boon")

    def action_taunt(self, button, args):
        # appeal to crowd, gaining favor from crowd
            # but also raising ire from your opponent (and their friends)
        print("Taunt")

    def action_retrieve(self, button, args):
        print("Retrieve")

    def action_suspend(self, button, args):
        print("Suspend")

    def action_forfeit(self, button, args):
        print("Forfeit")

    def action_continue(self, button, args): # move to the next turn
        print("Continue")
        print("stack now is ",self.stack["PC"])
        # if you don't have any techs or attacks in the stack, you just do rest action
        self.pc.resting = True if not self.stack["PC"] else False
        self.pc.rest_interrupted = False
        # enemy chooses actions, combat plays out, then go to next round
        self.battle.turn_end()
        if self.pc.resting:
            self._action_rest(self.pc)
        if self.npc.resting:
            self._action_rest(self.npc)
        self.battle.turn_begin() # prompt user for input again

    def _action_rest(self, character):
        print("Rest. Interrupted:", character.rest_interrupted)
        character.stats.heal_sp(1 if character.rest_interrupted else 3)
        character.resting = False
        character.rest_interrupted = False
        

            # tech registry stack #
    def action_register_tech(self, button, tech):
        # add the chosen technique to the stack. It will appear in a list on screen.
        # Once you choose CONFIRM, the battle round begins, the enemy selects their moves,
        # the moves are ordered by priority and speed, and then the technique() function
        # is called for each move in the proper order.
        nrg_cost = TECHNIQUES[tech]["nrg"]
        sp_cost = TECHNIQUES[tech]["sp"]
        sp_total = sp_cost
        for t in self.stack["PC"]: # TODO: show in UI how much NRG/SP your stack costs
            # TODO TEST THIS!!! HAS NOT BEEN TESTED
            sp_total += TECHNIQUES[t]["sp"]
        if (self.pc.stats.energy >= nrg_cost and self.pc.stats.sp >= sp_total):
            print("registered tech: ", tech)
            self.stack["PC"].append(tech)
            self.pc.stats.energy -= nrg_cost
        else:
            print("Insufficient energy and/or sp to use this tech")
        print("NRG: {} / {}".format(self.pc.stats.energy, nrg_cost))
        print("SP: {} / {}".format(self.pc.stats.sp, sp_cost))
        
    def action_register_backspace(self, button=None, args=[]): # remove most recently registered tech
        if self.stack["PC"]:
            print("tech removed")
            tech = self.stack["PC"][-1]
            self.pc.stats.energy = min(3, self.pc.stats.energy + TECHNIQUES[tech]["nrg"])
            del self.stack["PC"][-1] # TODO implement this

    def action_show_tech(self, button=None, args=None):
        self.delayed_actions.update(
            {"draw tech info" : (self.delayed_draw_tech_menu_info, [button, args])} )

    def delayed_draw_tech_menu_info(self, args):
        self.pc.techs.draw_terse(
            SURFACE,
            args[0].x+args[0].group.x + args[0].width,
            args[0].group.y,
            args[1]
            )
            
    def register_init(self): # clear registered techs from tech registry stack
        self.stack = {"PC":[], "NPC":[]}
        
    
    def level_up(self):

                    # TODO: revamp this to use Buttons
        
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
                self.check_menus_mouseover(mouse)
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    self.check_menus_mouse(mouse)
                if ev.type == pygame.KEYDOWN:
                    self.check_menus_key(ev.key)
                    if ev.key==pygame.K_ESCAPE:
                        self.menu_up_directory()

        # game upkeep #

        self.handle_menus() # update menu stuff

        # draw phase #

        # background
        SURFACE.fill(NEUTRAL_DARK)
        SURFACE.blit(BG_TEST, (0,0))

        # menus
        self.draw_menus()
        if self.delayed_actions.get("draw tech info"):
            val = self.delayed_actions["draw tech info"]
            val[0](val[1])
            del self.delayed_actions["draw tech info"]

        # sprites
        self.pc.draw(SURFACE)
        self.npc.draw(SURFACE)
        
        pygame.display.flip()
    # end def

    def draw_menus(self):
        for menu in self.menus.values():
            menu.draw_all()

    def check_menus_mouseover(self, mouse):
        for menu in self.menus.values():
            menu.check_all_hover(mouse)
    def check_menus_mouse(self, mouse):
        for menu in self.menus.values():
            menu.check_all_mouse(mouse)
    def check_menus_key(self, key):
        for name,menu in self.menus.items():
            if name==self.menu_in_focus:
                menu.check_all_key(key)

    def test(self, args):
        print("TEST SUCCESS!! {}".format(args))
# end class




