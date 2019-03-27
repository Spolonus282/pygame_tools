import pygame as _pygame
import math as _math

particle_group = _pygame.sprite.Group()

class Particle(_pygame.sprite.Sprite):
    '''Create a particle and add it to a particle list.
    Base particle class'''

    def __init__(self,image,center,surface):
        super().__init__()
        self.rect = image.get_rect()
        self.rect.center = center
        self.image = image
        self.surface = surface
        self.center = center
        particle_group.add(self)

    def update(self,*args):
        self.surface.blit(self.image,self.rect)

class Dilate_particle(Particle):
    '''create a particle that grows over time, then vanishes'''

    def __init__(self,image,center,surface,k,time,fade=False,fadeTime=None):
        super().__init__(image,center,surface)
        self.k = k
        self.delay = time
        if fade:
            self.fade_time = fadeTime
            self.milli_a = 255 / (1000 * self.fade_time)
            self.a = 255
        self.fade = fade
        self.start = None
        self.milli_k = self.k / (1000 * self.delay)
        self.milli_x = self.rect.width * self.milli_k
        self.milli_y = self.rect.height * self.milli_k
        self.millis = 1
        self.start_millis = None
        iterate = 1.0
        x_hold = self.milli_x
        y_hold = self.milli_y
        print(x_hold,y_hold)
        while int(self.milli_x) != self.milli_x or int(self.milli_y) != self.milli_y:
            self.milli_x = x_hold * iterate
            self.milli_y = y_hold * iterate
            self.millis = iterate
            iterate += 1.0
        print(self.millis,self.milli_x,self.milli_y)

    def dilate(self):
        'loop through and update to use'
        if not self.start: self.start = _pygame.time.get_ticks()
        if not self.start_millis: self.start_millis = _pygame.time.get_ticks()
        now = _pygame.time.get_ticks()
        if now - self.start >= 1000*self.delay:
            print(self.rect)
            particle_group.remove(self)
            print(now-self.start)
        if self.fade and now - self.start >= 1000*(self.delay - self.fade_time):
            self.a -= self.milli_a
            self.image.set_alpha(self.a)
        if now - self.start_millis >= self.millis:
            self.start_millis = _pygame.time.get_ticks()
            self.image = _pygame.transform.scale(self.image,(_math.ceil(self.milli_x+self.rect.width),_math.ceil(self.milli_y+self.rect.height)))
            self.rect.inflate_ip(_math.ceil(self.milli_x),_math.ceil(self.milli_y))
            #print(self.milli_x)
        self.rect.center = self.center

class Translate_particle(Particle):
    '''create a particle that moves, then vanishes'''

class Color_particle(Particle):
    '''create a particle that changes color, then vanishes'''

class Image_particle(Particle):
    '''create a particle that changes its texture, either looping once or many times before vanishing'''

class Multi_particle(Particle):
    '''create a particle that performs several actions before vanishing'''
