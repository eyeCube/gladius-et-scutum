'''
    ui.py
'''

import pygame

from const import *


class ButtonGroup:
    
    groupID = 0
    
    def __init__(self, surf, name=None, x=0,y=0, enabled=True):
        self.surface = surf
        if name==None:
            name = "Group{}".format(ButtonGroup.groupID)
            ButtonGroup.groupID += 1
        self.name = name
        self.enabled = enabled
        self.x=x
        self.y=y
        self.buttons={}

    def add(self, button):
        self.buttons.update({button.ID : button})

    def checkAll(self, arg, isMouse=False):
        if self.enabled==False: return
        if isMouse:
            for button in self.buttons.values():
                button.check_mouse(arg, self.x,self.y)
        else:
            for button in self.buttons.values():
                button.check_key(arg)

    def drawAll(self):
        if self.enabled==False: return
        for button in self.buttons.values():
            button.draw(self.surface, self.x,self.y)

    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
# end class


class Button:
    
    buttonID = 0
    
    def __init__(self, group,
                 name="", hotkey=pygame.K_0,
                 x1=0, y1=0, width=0, height=0,
                 action=None, args=[],
                 color_font=BLACK, color_dark=GRAY
                 ):
        self.ID=Button.buttonID
        Button.buttonID += 1
        group.add(self)
        self.name=name          # may be str or int
        self.hotkey=hotkey
        self.group=group
        self.x1=x1
        self.y1=y1
        self.width=width
        self.height=height
        self.action=action
        self.args=args          # action function arguments
        self.color_font=color_font
        self.color_dark=color_dark

    def check_mouse(self, mouse, x_origin, y_origin):
        # check if the user is clicking the button
        #   mouse --> pygame.mouse.get_pos()
        #   ev --> for ev in pygame.event.get():
        if not self.action: return
        if (x_origin+self.x1 <= mouse[0] <= x_origin+self.x1+self.width and
            y_origin+self.y1 <= mouse[1] <= y_origin+self.y1+self.height):
            self.action(self.args)

    def check_key(self, key):
        # check if the user is clicking the button
        #   mouse --> pygame.mouse.get_pos()
        #   ev --> for ev in pygame.event.get():
        if not self.action: return
        if (key==self.hotkey):
            self.action(self.args)

    def draw(self, surface, x_origin, y_origin):
        pygame.draw.rect(
            surface, self.color_dark,
            [x_origin+self.x1, y_origin+self.y1,
             self.width, self.height]
            )
        font = pygame.font.SysFont("consolas", 18)
        text = font.render(str(self.name), True, self.color_font)
        text_rect = text.get_rect(center=(x_origin+self.x1+self.width/2, y_origin+self.y1+self.height/2))
        surface.blit(text, text_rect)
# end class




















