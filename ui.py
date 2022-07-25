'''
    ui.py
'''

import pygame

from const import *

KEYS={
    pygame.K_a : "a",
    pygame.K_b : "b",
    pygame.K_c : "c",
    pygame.K_d : "d",
    pygame.K_e : "e",
    pygame.K_f : "f",
    pygame.K_g : "g",
    pygame.K_h : "h",
    pygame.K_i : "i",
    pygame.K_j : "j",
    pygame.K_k : "k",
    pygame.K_l : "l",
    pygame.K_m : "m",
    pygame.K_n : "n",
    pygame.K_o : "o",
    pygame.K_p : "p",
    pygame.K_q : "q",
    pygame.K_r : "r",
    pygame.K_s : "s",
    pygame.K_t : "t",
    pygame.K_u : "u",
    pygame.K_v : "v",
    pygame.K_w : "w",
    pygame.K_x : "x",
    pygame.K_y : "y",
    pygame.K_z : "z",
    pygame.K_0 : "0",
    pygame.K_1 : "1",
    pygame.K_2 : "2",
    pygame.K_3 : "3",
    pygame.K_4 : "4",
    pygame.K_5 : "5",
    pygame.K_6 : "6",
    pygame.K_7 : "7",
    pygame.K_8 : "8",
    pygame.K_9 : "9",
    pygame.K_COMMA : ",",
    pygame.K_PERIOD : ".",
    pygame.K_MINUS : "-",
    pygame.K_SLASH : "/",
    pygame.K_QUOTE : "'",
    pygame.K_QUOTEDBL : "\"",
    pygame.K_SPACE: " ",
}


# Clickable button form
class UIGroup:
    
    ID = 1
    
    def __init__(self, surf, name=None, x=0,y=0, enabled=True):
        self.ID=UIGroup.ID
        UIGroup.ID += 1
        self.surface = surf
        if name==None:
            name = "Group{}".format(self.ID)
        self.name = name
        self.enabled = enabled
        self.x=x
        self.y=y
        self.buttons={}
        self.inputs={}

    def add_button(self, button): self.buttons.update({button.ID : button})
    def add_input(self, inp): self.inputs.update({inp.ID : inp})

    def check_all_mouse(self, mouse):
        if self.enabled==False:
            return
        
        for button in self.buttons.values():
            button.check_mouse(mouse)
        for inp in self.inputs.values():
            inp.check_mouse_select(mouse) # select if applicable
            
    def check_all_key(self, key):
        if self.enabled==False:
            return
        
        cancel=False
        for inp in self.inputs.values():
            if inp.selected:
                if inp.done:
                    inp.action(inp.args)
                else:
                    inp.check(key)
                cancel=True
                break
            
        if not cancel: # only continue if we haven't given key input to an Input object
            for button in self.buttons.values():
                button.check_key(key)
                    
    def check_all_hover(self, mouse):
        for button in self.buttons.values():
            button.check_mouse_hover(mouse)

    def draw_all(self):
        if self.enabled==False: return
        for button in self.buttons.values():
            button.draw(self.surface)
        for inp in self.inputs.values():
            inp.draw(self.surface)

    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
    def deselect_all(self):
        for button in self.buttons.values():
            button.selected = False
# end class

class Button:
    
    ID = 1
    
    def __init__(self, group,
                 name="", hotkey=pygame.K_0,
                 x=0, y=0, width=0, height=0,
                 action=None, args=[],
                 hover_action=None, hover_args=[],
                 color_font=BLACK, color_dark=GRAY,
                 color_highlight=WHITE, color_light=LTGRAY
                 ):
        self.ID=Button.ID
        Button.ID += 1
        group.add_button(self)
        self.name=name          # may be str or int
        self.hotkey=hotkey
        self.group=group
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.action=action
        self.args=args          # action function arguments
        self.hover_action=hover_action # when user hovers over the button
        self.hover_args=hover_args
        self.color_font=color_font
        self.color_dark=color_dark
        self.color_light=color_light
        self.color_highlight=color_highlight
        self.selected=False
        self.highlighted=False

    def check_mouse(self, mouse):
        # check if the user is clicking the button
        #   mouse --> pygame.mouse.get_pos()
        if not self.action: return
        if (self.group.x+self.x < mouse[0] < self.group.x+self.x+self.width and
            self.group.y+self.y < mouse[1] < self.group.y+self.y+self.height):
            print("clicked button. args: ", self.args)
            self.action(self, self.args)

    def check_mouse_hover(self, mouse):
        # check if the user is hovering over the button and highlight if so
        if (self.group.x+self.x < mouse[0] < self.group.x+self.x+self.width and
            self.group.y+self.y < mouse[1] < self.group.y+self.y+self.height):
            self.highlighted = True
        else:
            self.highlighted = False

    def check_key(self, key):
        # check if the user is clicking the button
        #   mouse --> pygame.mouse.get_pos()
        #   ev --> for ev in pygame.event.get():
        if not self.action: return
        if (key==self.hotkey):
            self.action(self, self.args)

    def draw(self, surface):
        x = self.x+self.group.x
        y = self.y+self.group.y
        color = self.color_light if self.selected else self.color_dark
        fcol = self.color_highlight if self.highlighted else self.color_font
        pygame.draw.rect(surface, color, [x,y, self.width, self.height])
        font = FONT_MENU_1
        text = font.render(str(self.name), True, fcol)
        text_rect = text.get_rect(center=(x+self.width/2, y+self.height/2))
        text_rect.right = x+self.width-4
        surface.blit(text, text_rect)
        if (self.highlighted and self.hover_action):
            self.hover_action(self, self.hover_args)
# end class


# Text input form
class Input:
    ID=1
    
    def __init__(self, group,
                 label="", x=0,y=0, width=192,height=32,
                 default="", selected=True, action=None, args=[],
                 color_box=GRAY, color_font=BLACK
                 ):
        self.ID=Input.ID
        Input.ID += 1
        group.add_input(self)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.value=default      # text input value
        self.selected=selected
        self.label=label
        self.action=action
        self.args=args
        self.done=False     # done collecting input from user?

    def check_mouse_select(self, mouse):
        # check if the user is clicking the button
        #   mouse --> pygame.mouse.get_pos()
        self.selected = False # revert all except the one clicked on (if any)
        if (self.group.x+self.x <= mouse[0] <= self.group.x+self.x+self.width and
            self.group.y+self.y <= mouse[1] <= self.group.y+self.y+self.height):
            self.selected = True

    def check(self, key):        
        out = KEYS.get(key, "")
        if out != "":
            if len(self.value) < self.max_length:
                self.value = "{}{}".format(self.value, out)
                return
            else:
                # replace last char
                self.value = "{}{}".format(self.value[:-1], out)
                return
            
        if (key==pygame.K_BACKSPACE or key==pygame.K_DELETE): # delete
            if self.value != "":
                self.value = self.value[:-1]
                
        elif (key==pygame.K_RETURN or key==pygame.K_KP_ENTER):
            self.done = True

    def draw(self, surface, x_origin, y_origin):
        x = self.x+x_origin
        y = self.y+y_origin
        color = self.color_box
        fcol = self.color_font
        pygame.draw.rect(surface, color, [x,y, self.width, self.height])
        font = FONT_MENU_1
        # value
        valueText = font.render(str(self.value), True, fcol)
        surface.blit(valueText, (x+4,y+4))
        # label
        labelText = font.render(str(self.label), True, fcol)
        labelTextRect = labelText.get_rect(center=(x+self.width/2, y+self.height/2))
        labelTextRect.right = x-4
        surface.blit(labelText, labelTextRect)
# end class
        

# Message Log
class Log:
    def __init__(self):
        self.log=[]
        
    def msg(self, text):
        self.log.append(text)
        
    def draw_terse(self):
        pass

















