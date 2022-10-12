import pygame as _pygame
from typing import Literal
#from time import clock as _clock
_pygame.init()

__shifted = False
__lastBlink = 0.0
__blink = True
__checkfor = False

__CHARACTERS = [ord(c) for c in ' `1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./']
__BLINK_DELAY = 500

HOTKEYEVENT = 24

_pygame.key.set_repeat(350, 45)

class Text_line():
    __DEFAULT_FONT_TYPE = 'freesansbold.ttf'
    __DEFAULT_FONT_SIZE = 8
    __DEFAULT_FONT = _pygame.font.Font(__DEFAULT_FONT_TYPE, __DEFAULT_FONT_SIZE)

    def __init__(self, **kwargs) -> None:
        self.__text = kwargs.get('prompt', '')
        self.__font_size = kwargs.get('font_size', None)
        self.__font_type = kwargs.get('font_type', None)
        self.__text_color = kwargs.get('text_color', (0,0,0))
        self.__antialiasing = kwargs.get('antialiasing', True)
        self.__background: tuple[int, int, int] | None = kwargs.get('background', None)
        self.__coord: tuple[int, int] = kwargs.get('coord', (0,0))
        self.__justify: str = kwargs.get('justify', 'left')

        self.__font_obj = None

        if self.__font_size is not None: use_size = self.__font_size
        else: use_size = self.__DEFAULT_FONT_SIZE

        if self.__font_type is not None: use_type = self.__font_type
        else: use_type = self.__DEFAULT_FONT_TYPE

        if any([self.__font_size, self.__font_type]):
            self.__font = _pygame.font.Font(use_type, use_size)
        else:
            self.__font = None

    @staticmethod
    def set_default_font(font_type: str=__DEFAULT_FONT_TYPE, font_size: int=__DEFAULT_FONT_SIZE):
        Text_line.__DEFAULT_FONT_TYPE = font_type
        Text_line.__DEFAULT_FONT_SIZE = font_size
        Text_line.__DEFAULT_FONT = _pygame.font.Font(font_type, font_size)
    
    def set_font(self, font_type: str=__DEFAULT_FONT_TYPE, font_size: int=__DEFAULT_FONT_SIZE):
        self.__font_type = font_type
        self.__font_size = font_size
        self.__font = _pygame.font.Font(font_type, font_size)

    @property
    def text(self) -> str:
        return self.__text
    
    @text.setter
    def text(self, prompt: str):
        self.__text = prompt

    def render(self, alternate_prompt: str | None=None) -> _pygame.surface.Surface:
        use_font = self.__font if self.__font is not None else self.__DEFAULT_FONT
        use_text = alternate_prompt if alternate_prompt is not None else self.__text
        
        self.__font_obj = use_font.render(use_text, self.__antialiasing, self.__text_color, self.__background)

        return self.__font_obj
    
    def place(self, location: tuple[int, int] | None=None, justify: str | None=None, surface: _pygame.surface.Surface | None=None) -> tuple[_pygame.surface.Surface, _pygame.rect.Rect]:
        use_coord = location if location is not None else self.__coord
        use_justify = justify if justify is not None else self.__justify

        if self.__font_obj is None:
            self.render()

        assert self.__font_obj is not None
        text_rect = self.__font_obj.get_rect()

        match use_justify:
            case 'center':
                text_rect.center = use_coord
            case 'topleft' | 'left':
                text_rect.topleft = use_coord
            case 'topright' | 'right':
                text_rect.topright = use_coord
            case 'bottomleft':
                text_rect.bottomleft = use_coord
            case 'bottomright':
                text_rect.bottomright = use_coord

        if surface:
            surface.blit(self.__font_obj, text_rect)

        return (self.__font_obj, text_rect)

    @staticmethod
    def static_text_display(prompt, fontSize, color1, color2, justify, coord, transBack = False, antialiasing = True, fontType = 'freesansbold.ttf') -> tuple[_pygame.surface.Surface, _pygame.rect.Rect]:
        background = color2 if transBack else None

        line = Text_line(prompt=prompt, font_size=fontSize, text_color=color1, background=background, justify=justify, coord=coord, antialiasing=antialiasing, font_type=fontType)

        return line.place()

def get_typed(start_string: str, maxlen: int, *, hotkeys: list[int] = [], ignore: list[int] = []) -> str | Literal[1]:
    '''
    Check for typed input.\n
    Hotkeys will trigger when ctrl is held and releases a HOTKEYEVENT\n
    (Due to Python's limitations, the character 'c' cannot be used as a hotkey)
    '''
    global __shifted,__checkfor

    for event in _pygame.event.get([_pygame.KEYDOWN, _pygame.KEYUP]):

        match event.key:
            case _ if event.key in ignore: _pygame.event.post(event)

            case _pygame.K_LCTRL | _pygame.K_RCTRL: __checkfor = event.type == _pygame.KEYDOWN
            case _pygame.K_LSHIFT | _pygame.K_RSHIFT: __shifted = event.type == _pygame.KEYDOWN

            case _ if event.type == _pygame.KEYUP: pass

            case _ if event.key in hotkeys and __checkfor: _pygame.event.post(_pygame.event.Event(HOTKEYEVENT,{'key':event.key}))

            case _pygame.K_RETURN: return 1
            case _pygame.K_BACKSPACE if start_string != []: start_string = start_string[:-1]
            case _pygame.K_CAPSLOCK: pass
            case _pygame.K_ESCAPE: pass

            case _ if event.key in __CHARACTERS and not __shifted: start_string += chr(event.key)
            case _ if _pygame.K_a <= event.key <= _pygame.K_z: start_string += chr(event.key - 32)

            case _pygame.K_BACKQUOTE: start_string += '~'
            case _pygame.K_1: start_string += '!'
            case _pygame.K_2: start_string += '@'
            case _pygame.K_3: start_string += '#'
            case _pygame.K_4: start_string += '$'
            case _pygame.K_5: start_string += '%'
            case _pygame.K_6: start_string += '^'
            case _pygame.K_7: start_string += '&'
            case _pygame.K_8: start_string += '*'
            case _pygame.K_9: start_string += '('
            case _pygame.K_0: start_string += ')'
            case _pygame.K_MINUS: start_string += '_'
            case _pygame.K_EQUALS: start_string += '+'
            case _pygame.K_LEFTBRACKET: start_string += '{'
            case _pygame.K_RIGHTBRACKET: start_string += '}'
            case _pygame.K_BACKSLASH: start_string += '|'
            case _pygame.K_SEMICOLON: start_string += ':'
            case _pygame.K_QUOTE: start_string += '"'
            case _pygame.K_COMMA: start_string += '<'
            case _pygame.K_PERIOD: start_string += '>'
            case _pygame.K_SLASH: start_string += '?'

    start_string = start_string[:maxlen]

    return start_string

def add_type_bar():
    global __lastBlink, __blink
    current = _pygame.time.get_ticks()
    if __lastBlink == 0 or current - __lastBlink >= __BLINK_DELAY:
        __lastBlink = current
        __blink = not __blink
    if __blink: 
        return '|'
    return ''

class Text_box(_pygame.Rect):
    '''Hold a collection of text in one area.'''
    def __init__(self, coords, bounds, surface, **design_kwargs):
        self.__surface = surface

        #text design values
        self.__coord = (coords[0], coords[1])
        self.margin = design_kwargs.get('margin', 10)
        self.justify = design_kwargs.get('justify', 'left')
        self.text_color = design_kwargs.get('text_color', (0,0,0))
        self.back_color = design_kwargs.get('back_color', (255,255,255))
        self.font_size = design_kwargs.get('font_size', 8)
        self.font_type = design_kwargs.get('font_type', 'freesansbold.ttf')
        self.transparent = design_kwargs.get('transparent', False)
        self.antialiasing = design_kwargs.get('antialiasing', True)
        self.spacing = design_kwargs.get('spacing', 5)

        #text rendering values
        self.__line_length = 0
        self.__collide = 0
        self.__hold = ['']
        self.__text = ''
        self.__test_area = [0,0]
        self.__calc_lengths()
        super().__init__(coords, bounds)

    def __calc_lengths(self):
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
            self.__hold = [Text_line.static_text_display('',self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type)]
            return #empty string, no update
        if text_line == '|' and __blink:
            self.__hold = [Text_line.static_text_display('|',self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type)]
            return#empty string with style, no update
        if __blink and text_line[-1] == '|': text_use = text_line[:-1]
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
        if __blink:
            #print(temp2)
            temp2[-1] += '|'
        for t in temp2:
            self.__hold.append(Text_line.static_text_display(t,self.font_size,self.text_color,self.back_color,self.justify,(self.__coord[0]+self.margin,self.__coord[1]),self.transparent,self.antialiasing,self.font_type))
        #print('tick')
        for h in range(len(self.__hold)):
            self.__hold[h][1].centery += h*(self.__character_height + self.spacing)

    def render(self):
        if not self.transparent: _pygame.draw.rect(self.__surface,self.back_color,self)
        if self.__hold == ['']: return []
        return self.__hold
