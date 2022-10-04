import pygame as _pygame
import math as _math
_pygame.init()
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
        if self not in particle_group.sprites(): return
        self.surface.blit(self.image,self.rect)

    def kill(self):
        particle_group.remove(self)
        del self

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
    def __init__(self,center,surface,image_list,delay,killTime,loopNum=1,fade=False,fadeTime=None,fadeDelay=None,fadeMultiple=1):
        super().__init__(image_list[0],center,surface)
        self.active_index = 0
        self.image_list = image_list
        self.loops = loopNum
        self.fade = fade
        self.a = 255
        if fade:
            self.fade_time = fadeTime
            self.fade_delay = fadeDelay
            #self.milli_a = (255/fadeMultiple) / (1000 * self.fade_time)
            self.start_fade = False
        self.delay = delay
        self.last_change = None
        self.times = 0
        self.tot_time = self.delay * len(self.image_list) * self.loops
        self.last_fade = None
        self.multiple = fadeMultiple
        self.limit = killTime

    def check_change(self):
        if not self.last_change: self.last_change = _pygame.time.get_ticks()
        if not self.last_fade: self.last_fade = _pygame.time.get_ticks()
        now = _pygame.time.get_ticks()
        if now - self.last_change >= self.limit: self.kill()
        if now - self.last_change >= self.delay:
            self.last_change = _pygame.time.get_ticks()
            self.active_index += 1
            if self.active_index == len(self.image_list):
                self.times += 1
                self.active_index = 0
                if self.times == self.loops: self.remove(self.groups())
        if self.fade and now - self.last_fade >= self.fade_delay: self.start_fade = True
        if self.fade and now - self.last_fade >= self.fade_time and self.start_fade:
            self.last_fade = _pygame.time.get_ticks()
            self.a -= self.multiple
            self.image.set_alpha(self.a)
        self.image = self.image_list[self.active_index]
        self.image.set_alpha(self.a)

class Multi_particle(Particle):
    '''create a particle that performs several actions before vanishing'''

if __name__ == '__main__':
    SURF = _pygame.display.set_mode((300,300))
    Image_particle((150,150),SURF,[_pygame.image.load(__file__.rstrip('animations.pyc')+'images/test_particle_1.png'),_pygame.image.load(__file__.rstrip('animations.pyc')+'images/test_particle_2.png'),_pygame.image.load(__file__.rstrip('animations.pyc')+'images/test_particle_3.png'),_pygame.image.load(__file__.rstrip('animations.pyc')+'images/test_particle_4.png')],100,10,True,10,500)
    while True:
        for r in particle_group.sprites(): r.check_change()
        SURF.fill((255,255,255))
        particle_group.update()
        for e in _pygame.event.get():
            if e.type == _pygame.QUIT:
                _pygame.quit()
                import sys
                sys.exit()
        _pygame.display.update()
