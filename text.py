import pygame, sys
from time import clock
pygame.init()

__HasTyped = ''
__Shifted = False
__lastBlink = 0.0
__blink = True

pygame.key.set_repeat(350, 45)

def text_display(prompt, fontSize, color1, color2, justify, coord, transBack = False, antialiasing = True, fontType = 'freesansbold.ttf'):
    'Display text'
    if justify == 'left': justify = 'topleft'
    elif justify == 'right': justify = 'topright'
    fontObj = pygame.font.Font(fontType, fontSize)
    textObj = fontObj.render(prompt, antialiasing, color1, color2)
    if transBack: textObj.set_colorkey(color2)
    rectObj = textObj.get_rect()
    if justify == 'center':
        rectObj.center = coord
    elif justify == 'topleft':
        rectObj.topleft = coord
    elif justify == 'topright':
        rectObj.topright = coord
    elif justify == 'bottomleft':
        rectObj.bottomleft = coord
    elif justify == 'bottomright':
        rectObj.bottomright = coord

    return [textObj, rectObj]

def get_typed(Key, maxlen, hotkeys = []):
    'Check for typed input. if any hotkeys, specify letter after ctrl\neg ctrl a -> hotkeys = [\'a\']'
    global __Shifted,__lastBlink,__blink
    if Key == ['|']:
        Key = []
    elif Key[-1] == '|':
        Key = Key[:-1]
    checkfor = False
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP]):
        if event.key in [pygame.K_LCTRL,pygame.K_RCTRL] and checkfor and event.type == pygame.KEYUP:
            checkfor = False
            continue
        elif event.key in hotkeys and checkfor:
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN,{'key':event.key}))
            continue
        elif event.key in [pygame.K_LCTRL,pygame.K_RCTRL] and event.type == pygame.KEYDOWN:
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN,{'key':event.key}))
            checkfor = True
            continue
        if event.key in [pygame.K_LSHIFT,pygame.K_RSHIFT] and event.type == pygame.KEYDOWN: __Shifted = True
        elif event.key in [pygame.K_LSHIFT,pygame.K_RSHIFT] and event.type == pygame.KEYUP: __Shifted = False
        elif event.key == pygame.K_RETURN: return 1
        elif event.key == pygame.K_BACKSPACE and event.type == pygame.KEYDOWN and Key != []: Key = Key[:-1]

        elif not __Shifted and event.type == pygame.KEYDOWN: Key += chr(event.key)
        elif __Shifted and event.type == pygame.KEYDOWN:
            if pygame.K_a <= event.key <= pygame.K_z: Key += chr(event.key - 32)
            elif event.key == pygame.K_BACKQUOTE: Key += '~'
            elif event.key == pygame.K_1: Key += '!'
            elif event.key == pygame.K_2: Key += '@'
            elif event.key == pygame.K_3: Key += '#'
            elif event.key == pygame.K_4: Key += '$'
            elif event.key == pygame.K_5: Key += '%'
            elif event.key == pygame.K_6: Key += '^'
            elif event.key == pygame.K_7: Key += '&'
            elif event.key == pygame.K_8: Key += '*'
            elif event.key == pygame.K_9: Key += '('
            elif event.key == pygame.K_0: Key += ')'
            elif event.key == pygame.K_MINUS: Key += '_'
            elif event.key == pygame.K_EQUALS: Key += '+'
            elif event.key == pygame.K_LEFTBRACKET: Key += '{'
            elif event.key == pygame.K_RIGHTBRACKET: Key += '}'
            elif event.key == pygame.K_BACKSLASH: Key += '|'
            elif event.key == pygame.K_SEMICOLON: Key += ':'
            elif event.key == pygame.K_QUOTE: Key += '"'
            elif event.key == pygame.K_COMMA: Key += '<'
            elif event.key == pygame.K_PERIOD: Key += '>'
            elif event.key == pygame.K_SLASH: Key += '?'
    while len(Key) > maxlen: Key = Key[:-1]
    if __lastBlink == 0: __lastBlink = clock()
    elif clock() - __lastBlink >= 0.5:
        __lastBlink = clock()
        __blink = not __blink
    if __blink: Key += '|'
    return Key

def get_typed_numeric(Key, maxlen):
    'Check for typed numbers and operations'
    if not isinstance(Key, str):
        raise TypeError('Key must be type str')
    if not isinstance(maxlen, int):
        raise TypeError('maxlen must be type int')
    Keys = pygame.key.get_pressed()
    global __HasTyped
    if not any(Keys): __HasTyped = False
    if __HasTyped: return Key
    if any(Keys): __HasTyped = True
    if Keys[pygame.K_LSHIFT] or Keys[pygame.K_RSHIFT]: Shifted = True
    if Keys[pygame.K_RETURN]: return 1
    if Keys[pygame.K_BACKSPACE] and not HasTyped[pygame.K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[pygame.K_1] and not HasTyped[pygame.K_1]: Key += '1'
        elif Keys[pygame.K_2] and not HasTyped[pygame.K_2]: Key += '2'
        elif Keys[pygame.K_3] and not HasTyped[pygame.K_3]: Key += '3'
        elif Keys[pygame.K_4] and not HasTyped[pygame.K_4]: Key += '4'
        elif Keys[pygame.K_5] and not HasTyped[pygame.K_5]: Key += '5'
        elif Keys[pygame.K_6] and not HasTyped[pygame.K_6]: Key += '6'
        elif Keys[pygame.K_7] and not HasTyped[pygame.K_7]: Key += '7'
        elif Keys[pygame.K_8] and not HasTyped[pygame.K_8]: Key += '8'
        elif Keys[pygame.K_9] and not HasTyped[pygame.K_9]: Key += '9'
        elif Keys[pygame.K_0] and not HasTyped[pygame.K_0]: Key += '0'
        elif Keys[pygame.K_MINUS] and not HasTyped[pygame.K_MINUS]: Key += '-'
        elif Keys[pygame.K_EQUALS] and not HasTyped[pygame.K_EQUALS]: Key += '='
        elif Keys[pygame.K_PERIOD] and not HasTyped[pygame.K_PERIOD]: Key += '.'
        elif Keys[pygame.K_SLASH] and not HasTyped[pygame.K_SLASH]: Key += '/'
    elif Shifted:
        if Keys[pygame.K_5] and not HasTyped[pygame.K_5]: Key += '%'
        elif Keys[pygame.K_8] and not HasTyped[pygame.K_8]: Key += '*'
        elif Keys[pygame.K_9] and not HasTyped[pygame.K_9]: Key += '('
        elif Keys[pygame.K_0] and not HasTyped[pygame.K_0]: Key += ')'
        elif Keys[pygame.K_EQUALS] and not HasTyped[pygame.K_EQUALS]: Key += '+'
        elif Keys[pygame.K_COMMA] and not HasTyped[pygame.K_COMMA]: Key += '<'
        elif Keys[pygame.K_PERIOD] and not HasTyped[pygame.K_PERIOD]: Key += '>'

    while len(Key) > maxlen: Key = Key[:-1]
    __HasTyped = Keys
    return Key

class Text_box(pygame.Rect):
    '''Hold a collection of text in one area.'''
    def __init__(self, coords, bounds, surface):
        self.__surface = surface
        #text design values
        self.__coord = (coords[0] + 5, coords[1])
        self.margin = 10
        self.justify = 'left'
        self.text_color = (0,0,0)
        self.back_color = (255,255,255)
        self.font_size = 8
        self.font_type = 'freesansbold.ttf'
        self.transparent = False
        #text rendering values
        self.__line_length = 0
        self.__collide = 0
        self.__hold = ['']
        self.__text = ''
        self.__test_area = [0,0]

        super().__init__(coords, bounds)
    def add_text(self, text_line):
        '''add one long string of text, and it will be auto-formatted'''
        if text_line == '' or text_line == self.__text: return
        #if text_line[-1] == ' ' and text_line != ' ': text_line = text_line[:-1]
        self.__test_area[1] = len(text_line)
        del self.__hold[-1]
        temp2 = []
        temp1 = ''
        temp3 = 0
        while True:
            while True:
                temp = text_display(text_line[self.__test_area[0]:self.__test_area[1]],self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,True,self.font_type)
                if temp[1].w + 2*self.margin >= self.w:
                    while text_line[self.__test_area[1]-1] != ' ' and ' ' in text_line[self.__test_area[0]+1:self.__test_area[1]]: self.__test_area[1] -= 1
                if temp[1].w + 2*self.margin >= self.w: self.__test_area[1] -= 1
                else: break
            temp1 = text_line[self.__test_area[0]:self.__test_area[1]]
            if len(temp1) > 1 and temp1[0] == ' ': temp1 = temp1[1:]
            if len(temp1) > 0 and temp1[-1] == ' ': temp1 = temp1[:-1]
            temp3 = text_display(temp1,self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,True,self.font_type)
            self.__hold.append(temp3)
            temp2.append(temp3)
            if self.__test_area[1] == len(text_line): break
            self.__test_area = [self.__test_area[1],len(text_line)]
        if len(self.__hold) != 1:
            if self.__collide == 0 and len(self.__hold) == 2:
                while len(self.__hold) > 1 and self.__hold[0][1].colliderect(self.__hold[1][1]):
                    self.__collide += 1
                    self.__hold[1][1].y += 1
                self.__collide += 2
                self.__hold[1][1].y -= self.__collide-2
            for b in range(self.__hold.index(temp2[0]),len(self.__hold)):
                self.__hold[b][1].y += self.__collide*b
            self.__line_length = len(self.__hold)
        self.__text = text_line

    def render(self):
        if not self.transparent: pygame.draw.rect(self.__surface,self.back_color,self)
        if self.__hold == ['']: return []
        return self.__hold
