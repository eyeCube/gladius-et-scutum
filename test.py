
from const import *


class Combatant_Techniques:
    def __init__(self, favorite_element=None):
        self.techniques={ "fire":{}, "earth":{}, "air":{}, "water":{} }
        self.favorite_element=favorite_element

    def add_tech(self, element, level, tech):
        if self.techniques[element].get(level):
            self.techniques[element][level].append(tech)
        else:
            self.techniques[element].update({level: [tech]})

    def remove_tech(self, tech):
        element = ELEMENTS[TECHNIQUES[tech]['element']]
        level = TECHNIQUES[tech]['level']
        try:
            self.techniques[element][level].remove(tech)
        except:
            print("Failed to remove tech -- {} lv{}: '{}'".format(element, level, tech))

    def learn_tech(self, owner, tech):
        data = TECHNIQUES[tech]
        reqSkill = data["req-skill"]
        if data["element"]==self.favorite_element: #favorite_element -> SP cost -2
            reqSkill -= 2
        if owner.stats.skill >= reqSkill:
            self.add_tech(tech)
# end class
        

    
c=Combatant_Techniques("fire")
c.add_tech("fire", 1, "Firebolt")
c.add_tech("fire", 1, "Burning Touch")
c.add_tech("water", 2, "Shield")
print(c.techniques)

c.remove_tech("Gust Punch")
c.remove_tech("Firebolt")
print(c.techniques)
