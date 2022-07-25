'''
    gladius.py

    Gladius et Scutum - Jane Wharton
    
'''

import pygame
import random

from const import *
import ui as uipy
import ai as aipy
import battle as battlepy
import game as gamepy
import combatant


if __name__=="__main__":

    pc = combatant.Combatant(
            name="Jaen", 
            favorite_element=ELEM_AIR,
            weapon=WPN_SLING,
            pc=True,
            ) # temporary auto-populated test data
    pc.stats.update_base("eva", 10)
    pc.stats.update_base("acc", 10)
        # chargen allows player to select favorite tech, favorite weapon, name, etc.
    print("Pressure Bolt:",pc.techs.learn_tech("Pressure Bolt"))
    print("Breath of Wind:",pc.techs.learn_tech("Breath of Wind"))
    print("Bubble:",pc.techs.learn_tech("Bubble"))
    print("Watergun:",pc.techs.learn_tech("Watergun"))
    print("Compression Wave:",pc.techs.learn_tech("Compression Wave"))
    
    game = gamepy.Game(pc)

    game.begin_battle(2)


    #
    
    




