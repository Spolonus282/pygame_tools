import pygame as _pygame
from time import clock as _clock
_pygame.init()

__HasTyped = ''
__Shifted = False
__lastBlink = 0.0
_blink = True
#HOTKEYEVENT = 24
__checkfor = False

_pygame.key.set_repeat(350, 45)

def text_display(prompt, fontSize, color1, color2, justify, coord, transBack = False, antialiasing = True, fontType = 'freesansbold.ttf'):
    'Display text'
    if justify == 'left': justify = 'topleft'
    elif justify == 'right': justify = 'topright'
    fontObj = _pygame.font.Font(fontType, fontSize)
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
    global __Shifted,__lastBlink,_blink,__checkfor
    if Key == '|':
        Key = ''
    elif Key != '' and Key[-1] == '|':
        Key = Key[:-1]
    for event in _pygame.event.get([_pygame.KEYDOWN,_pygame.KEYUP]):
        #print(event.key)
        if event.key in [_pygame.K_LCTRL,_pygame.K_RCTRL] and __checkfor and event.type == _pygame.KEYUP:
            __checkfor = False
            continue
        elif chr(event.key) in hotkeys and __checkfor:
            _pygame.event.post(_pygame.event.Event(HOTKEYEVENT,{'key':event.key}))
            #print('hoi')
            continue
        elif event.key in [_pygame.K_LCTRL,_pygame.K_RCTRL] and event.type == _pygame.KEYDOWN:
            #_pygame.event.post(_pygame.event.Event(_pygame.KEYDOWN,{'key':event.key}))
            __checkfor = True
            continue
        if event.key in [_pygame.K_LSHIFT,_pygame.K_RSHIFT] and event.type == _pygame.KEYDOWN: __Shifted = True
        elif event.key in [_pygame.K_LSHIFT,_pygame.K_RSHIFT] and event.type == _pygame.KEYUP: __Shifted = False
        elif event.key == _pygame.K_RETURN: return 1
        elif event.key == _pygame.K_BACKSPACE and event.type == _pygame.KEYDOWN and Key != []: Key = Key[:-1]
        elif event.key == _pygame.K_CAPSLOCK and event.type == _pygame.KEYDOWN:pass
        #elif event.key == _pygame.K_ESCAPE: continue

        elif not __Shifted and event.type == _pygame.KEYDOWN and chr(event.key) in ' `1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./': Key += chr(event.key)
        elif __Shifted and event.type == _pygame.KEYDOWN:
            if _pygame.K_a <= event.key <= _pygame.K_z: Key += chr(event.key - 32)
            elif event.key == _pygame.K_BACKQUOTE: Key += '~'
            elif event.key == _pygame.K_1: Key += '!'
            elif event.key == _pygame.K_2: Key += '@'
            elif event.key == _pygame.K_3: Key += '#'
            elif event.key == _pygame.K_4: Key += '$'
            elif event.key == _pygame.K_5: Key += '%'
            elif event.key == _pygame.K_6: Key += '^'
            elif event.key == _pygame.K_7: Key += '&'
            elif event.key == _pygame.K_8: Key += '*'
            elif event.key == _pygame.K_9: Key += '('
            elif event.key == _pygame.K_0: Key += ')'
            elif event.key == _pygame.K_MINUS: Key += '_'
            elif event.key == _pygame.K_EQUALS: Key += '+'
            elif event.key == _pygame.K_LEFTBRACKET: Key += '{'
            elif event.key == _pygame.K_RIGHTBRACKET: Key += '}'
            elif event.key == _pygame.K_BACKSLASH: Key += '|'
            elif event.key == _pygame.K_SEMICOLON: Key += ':'
            elif event.key == _pygame.K_QUOTE: Key += '"'
            elif event.key == _pygame.K_COMMA: Key += '<'
            elif event.key == _pygame.K_PERIOD: Key += '>'
            elif event.key == _pygame.K_SLASH: Key += '?'
        else:
            _pygame.event.post(_pygame.event.Event(event.type,event.dict))
        __checkfor = False
    while len(Key) > maxlen: Key = Key[:-1]
    if __lastBlink == 0: __lastBlink = _clock()
    elif _clock() - __lastBlink >= 0.5:
        __lastBlink = _clock()
        _blink = not _blink
    if _blink: Key += '|'
    return Key

def get_typed_numeric(Key, maxlen):
    'Check for typed numbers and operations'
    if not isinstance(Key, str):
        raise TypeError('Key must be type str')
    if not isinstance(maxlen, int):
        raise TypeError('maxlen must be type int')
    Keys = _pygame.key.get_pressed()
    global __HasTyped
    if not any(Keys): __HasTyped = False
    if __HasTyped: return Key
    if any(Keys): __HasTyped = True
    if Keys[_pygame.K_LSHIFT] or Keys[_pygame.K_RSHIFT]: Shifted = True
    if Keys[_pygame.K_RETURN]: return 1
    if Keys[_pygame.K_BACKSPACE] and not HasTyped[_pygame.K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[_pygame.K_1] and not HasTyped[_pygame.K_1]: Key += '1'
        elif Keys[_pygame.K_2] and not HasTyped[_pygame.K_2]: Key += '2'
        elif Keys[_pygame.K_3] and not HasTyped[_pygame.K_3]: Key += '3'
        elif Keys[_pygame.K_4] and not HasTyped[_pygame.K_4]: Key += '4'
        elif Keys[_pygame.K_5] and not HasTyped[_pygame.K_5]: Key += '5'
        elif Keys[_pygame.K_6] and not HasTyped[_pygame.K_6]: Key += '6'
        elif Keys[_pygame.K_7] and not HasTyped[_pygame.K_7]: Key += '7'
        elif Keys[_pygame.K_8] and not HasTyped[_pygame.K_8]: Key += '8'
        elif Keys[_pygame.K_9] and not HasTyped[_pygame.K_9]: Key += '9'
        elif Keys[_pygame.K_0] and not HasTyped[_pygame.K_0]: Key += '0'
        elif Keys[_pygame.K_MINUS] and not HasTyped[_pygame.K_MINUS]: Key += '-'
        elif Keys[_pygame.K_EQUALS] and not HasTyped[_pygame.K_EQUALS]: Key += '='
        elif Keys[_pygame.K_PERIOD] and not HasTyped[_pygame.K_PERIOD]: Key += '.'
        elif Keys[_pygame.K_SLASH] and not HasTyped[_pygame.K_SLASH]: Key += '/'
    elif Shifted:
        if Keys[_pygame.K_5] and not HasTyped[_pygame.K_5]: Key += '%'
        elif Keys[_pygame.K_8] and not HasTyped[_pygame.K_8]: Key += '*'
        elif Keys[_pygame.K_9] and not HasTyped[_pygame.K_9]: Key += '('
        elif Keys[_pygame.K_0] and not HasTyped[_pygame.K_0]: Key += ')'
        elif Keys[_pygame.K_EQUALS] and not HasTyped[_pygame.K_EQUALS]: Key += '+'
        elif Keys[_pygame.K_COMMA] and not HasTyped[_pygame.K_COMMA]: Key += '<'
        elif Keys[_pygame.K_PERIOD] and not HasTyped[_pygame.K_PERIOD]: Key += '>'

    while len(Key) > maxlen: Key = Key[:-1]
    __HasTyped = Keys
    return Key

class Text_box(_pygame.Rect):
    '''Hold a collection of text in one area.'''
    def __init__(self, coords, bounds, surface):
        self.__surface = surface
        #text design values
        self.__coord = (coords[0], coords[1])
        self.margin = 10
        self.justify = 'left'
        self.text_color = (0,0,0)
        self.back_color = (255,255,255)
        self.font_size = 8
        self.font_type = 'freesansbold.ttf'
        self.transparent = False
        self.antialiasing = True
        self.spacing = 5
        #text rendering values
        self.__text_obj = _pygame.font.Font(self.font_type,self.font_size)
        self.__line_length = 0
        self.__collide = 0
        self.__hold = ['']
        self.__text = ''
        self.__test_area = [0,0]
        self.__al_lengths_small = {chr(t):self.__text_obj.size(chr(t))[0] for t in range(97,123)}
        self.__al_lengths_big = {chr(T):self.__text_obj.size(chr(T))[0] for T in range(65, 91)}
        self.__num_lengths = {chr(n):self.__text_obj.size(chr(n))[0] for n in range(48, 58)}
        self.__symbol_lengths = {'`':self.__text_obj.size('`')[0], '~':self.__text_obj.size('~')[0], '!':self.__text_obj.size('!')[0],
                                 '@':self.__text_obj.size('@')[0], '#':self.__text_obj.size('#')[0], '$':self.__text_obj.size('$')[0],
                                 '%':self.__text_obj.size('%')[0], '^':self.__text_obj.size('^')[0], '&':self.__text_obj.size('&')[0],
                                 '*':self.__text_obj.size('*')[0], '(':self.__text_obj.size('(')[0], ')':self.__text_obj.size(')')[0],
                                 '-':self.__text_obj.size('-')[0], '_':self.__text_obj.size('_')[0], '=':self.__text_obj.size('=')[0],
                                 '+':self.__text_obj.size('+')[0], '[':self.__text_obj.size('[')[0], '{':self.__text_obj.size('{')[0],
                                 ']':self.__text_obj.size(']')[0], '}':self.__text_obj.size('}')[0], '\\':self.__text_obj.size('\\')[0],
                                 '|':self.__text_obj.size('|')[0], ';':self.__text_obj.size(';')[0], ':':self.__text_obj.size(':')[0],
                                 "'":self.__text_obj.size("'")[0], '"':self.__text_obj.size('"')[0], ',':self.__text_obj.size(',')[0],
                                 '<':self.__text_obj.size('<')[0], '.':self.__text_obj.size('.')[0], '>':self.__text_obj.size('>')[0],
                                 '/':self.__text_obj.size('/')[0], '?':self.__text_obj.size('?')[0], ' ':self.__text_obj.size(' ')[0]}
        self.__character_height = self.__text_obj.size('W')[1]

        super().__init__(coords, bounds)
    def calc_lengths(self):
        self.__text_obj = _pygame.font.Font(self.font_type,self.font_size)
        self.__al_lengths_small = {chr(t):self.__text_obj.size(chr(t))[0] for t in range(97,123)}
        self.__al_lengths_big = {chr(T):self.__text_obj.size(chr(T))[0] for T in range(65, 91)}
        self.__num_lengths = {chr(n):self.__text_obj.size(chr(n))[0] for n in range(48, 58)}
        self.__symbol_lengths = {'`':self.__text_obj.size('`')[0], '~':self.__text_obj.size('~')[0], '!':self.__text_obj.size('!')[0],
                                 '@':self.__text_obj.size('@')[0], '#':self.__text_obj.size('#')[0], '$':self.__text_obj.size('$')[0],
                                 '%':self.__text_obj.size('%')[0], '^':self.__text_obj.size('^')[0], '&':self.__text_obj.size('&')[0],
                                 '*':self.__text_obj.size('*')[0], '(':self.__text_obj.size('(')[0], ')':self.__text_obj.size(')')[0],
                                 '-':self.__text_obj.size('-')[0], '_':self.__text_obj.size('_')[0], '=':self.__text_obj.size('=')[0],
                                 '+':self.__text_obj.size('+')[0], '[':self.__text_obj.size('[')[0], '{':self.__text_obj.size('{')[0],
                                 ']':self.__text_obj.size(']')[0], '}':self.__text_obj.size('}')[0], '\\':self.__text_obj.size('\\')[0],
                                 '|':self.__text_obj.size('|')[0], ';':self.__text_obj.size(';')[0], ':':self.__text_obj.size(':')[0],
                                 "'":self.__text_obj.size("'")[0], '"':self.__text_obj.size('"')[0], ',':self.__text_obj.size(',')[0],
                                 '<':self.__text_obj.size('<')[0], '.':self.__text_obj.size('.')[0], '>':self.__text_obj.size('>')[0],
                                 '/':self.__text_obj.size('/')[0], '?':self.__text_obj.size('?')[0], ' ':self.__text_obj.size(' ')[0]}
        self.__character_height = self.__text_obj.size('W')[1]
    def add_text(self, text_line):
        '''add one long string of text, and it will be auto-formatted'''
        #print(text_line)
        if text_line == '' or text_line == self.__text:
            self.__hold = [text_display('',self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type)]
            return #empty string, no update
        if text_line == '|' and _blink:
            self.__hold = [text_display('|',self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type)]
            return#empty string with style, no update
        if _blink and text_line[-1] == '|': text_use = text_line[:-1]
        else: text_use = text_line
        self.__hold = []
        temp2 = []
        lengths = []
        for l in text_use:
            if l in self.__al_lengths_small: lengths.append(self.__al_lengths_small[l])
            elif l in self.__al_lengths_big: lengths.append(self.__al_lengths_big[l])
            elif l in self.__num_lengths: lengths.append(self.__num_lengths[l])
            elif l in self.__symbol_lengths: lengths.append(self.__symbol_lengths[l])
        #print(str(lengths)+'\n')
        start = 0
        end = 0
        cutback = 0
        while end < len(text_use): #creates the lists of lines
            while sum(lengths[start:end+1]) + 2*self.margin < self.w and end < len(text_use)-1: #checks to see if line is too long or is done
                cutback = end #buffer to remove if too large
                end += 1 #add one to counter to keep from cancelling immediately
                while text_use[end] not in ' -' and end != len(text_use)-1: end += 1 #goes until the end of a word or split
            check_cut = start == cutback
            cutback += 1
            if check_cut and sum(lengths[start:end+1]) + 2*self.margin >= self.w:
                temp_end = start
                while sum(lengths[start:temp_end+1]) + 2*self.margin < self.w: temp_end += 1
                cutback = temp_end
                temp2.append(text_use[start:cutback]) #remove last part, because it's too long
                start = cutback #if needed, this is where to start next time
            elif sum(lengths[start:end+1]) + 2*self.margin >= self.w:
                temp2.append(text_use[start:cutback]) #remove last part, because it's too long
                start = cutback #if needed, this is where to start next time
            elif end == len(text_use)-1:
                temp2.append(text_use[start:end+1])
                break
            #print(sum(lengths[start:cutback]) + 2*self.margin)
            if end != len(text_use)-1: end = cutback
            #print(end)
        #print(temp2)
        if _blink:
            #print(temp2)
            temp2[-1] += '|'
        for t in temp2:
            self.__hold.append(text_display(t,self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type))
        #print('tick')
        for h in range(len(self.__hold)):
            self.__hold[h][1].centery += h*(self.__character_height + self.spacing)

    def render(self):
        if not self.transparent: _pygame.draw.rect(self.__surface,self.back_color,self)
        if self.__hold == ['']: return []
        return self.__hold
