'''Clickable button class'''
import pygame, os.path
pygame.init()
missing = pygame.image.load(''.join([__file__.rstrip('button.pycw'),'images/missing.png']))

class Button():
    'creates a new button'
    def __init__(self, coords, runFunction):
        '''runFunction takes a searchable keyward'''
        assert isinstance(coords, list) or isinstance(coords, tuple)
        self._x = coords[0]
        self._y = coords[1]
        self._coords = [self._x, self._y]
        self._run = runFunction

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def setx(self, x):
        self._coords[0] = x
        self._x = x

    def sety(self, y):
        self._coords[1] = y
        self._y = y

class Static_button(Button):
    def __init__(self, coords, runkey, surface, idle=missing, hover=missing):
        super().__init__(coords,runkey)
        self._idle = idle
        self._hover = hover
        self._surface = surface

    def check_click(self):
        '''checks button for clicks. If clicked,
        returns key. Else, sends update command'''
        check = False
        getMouse = pygame.mouse.get_pos()
        getClick = pygame.mouse.get_pressed()[0]
        #print(getMouse)
        if (self._rectangle.left < getMouse[0] < self._rectangle.right and
            self._rectangle.top < getMouse[1] < self._rectangle.bottom): check = True
        else: check = False
        if getClick and check: return self._run
        else: return check

class Static_button_color(Static_button):
    '''creates a new clickable box.
    idle and hover are three-element tuples'''
    def __init__(self, coords, runkey, idle_color, hover_color, w, h, surface):
        super().__init__(coords, runkey, surface, idle_color, hover_color)
        self._rectangle = pygame.Rect(0,0,w,h)
        self._rectangle.center = self._coords

    def update(self, checked):
        if checked: pygame.draw.rect(self._surface, self._hover, self._rectangle)
        else: pygame.draw.rect(self._surface, self._idle, self._rectangle)
    

class Static_button_image(Static_button):
    'creates a new clickable image'
    def __init__(self, coords, runkey, surface, idle=missing, hover=missing):
        super().__init__(coords, runkey, surface, idle, hover)
        self._rectangle = self._idle.get_rect()
        self._rectangle.center = self._coords

    def update(self, checked):
        if checked: self._surface.blit(self._hover, self._rectangle)
        else: self._surface.blit(self._idle, self._rectangle)
    
    def send_blittables(self, checked):
        if checked: return self._hover, self._rectangle
        else: return self._idle, self._rectangle

class Dynamic_button(Button):
    def __init__(self, coords, runkey, surface, idle=missing, hover=missing):
        super().__init__(coords, runkey)
        self._idle = idle
        self._hover = hover
        self._surface = surface

    def check_click(self):
        '''checks button for clicks. If clicked,
        returns key. Else, sends update command'''
        check = False
        getMouse = pygame.mouse.get_pos()
        getClick = pygame.mouse.get_pressed()[0]
        if (self._rect0.left < getMouse[0] < self._rect0.right and
            self._rect0.top < getMouse[1] < self._rect0.bottom): check = True
        else: check = False
        if getClick and check: return self._run
        else: return check

class Dynamic_button_image(Dynamic_button):
    'creates a new dynamic clickable image'
    def __init__(self, coords, runkey, surface, idle=missing, hover=missing):
        super().__init__(coords, runkey, surface, idle, hover)
        self._rect0 = self._idle.get_rect()
        self._rect1 = self._hover.get_rect()
        self._rect0.center = self._coords
        self._rect1.center = self._coords
        self._reset = self._rect1.copy()

    def update(self, checked):
        if checked: self._surface.blit(self._hover, self._rect1)
        else: self._surface.blit(self._idle, self._rect0)
    
    def send_blittables(self, checked):
        if checked: return self._hover, self._rect1
        else: return self._idle, self._rect0

class Dynamic_button_color(Dynamic_button):
    '''creates a new dynamic clickable box
    idle and hover are three-element tuples'''
    def __init__(self, coords, runkey, surface, idle_color, hover_color, w, h, w1, h1):
        super().__init__(coords, runkey, surface, idle_color, hover_color)
        self._rect0 = pygame.Rect(0, 0, w, h)
        self._rect1 = pygame.Rect(0, 0, w1, h1)
        self._rect0.center = self._coords
        self._rect1.center = self._coords
        self._reset = self._rect1.copy()

    def update(self, checked):
        if checked: pygame.draw.rect(self._surface, self._hover, self._rect1)
        else: pygame.draw.rect(self._surface, self._idle, self._rect0)
