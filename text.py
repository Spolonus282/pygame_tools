import pygame, sys
pygame.init()

__HasTyped = ''

def text_display(prompt, fontSize, color1, color2, justify, coord,
             transBack = False, antialiasing = True,
             fontType = 'freesansbold.ttf'):
    'Display text'
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

def get_typed(Key, maxlen):
    'Check for typed input'
    if not isinstance(Key, str):
        raise TypeError('Key must be type str')
    if not isinstance(maxlen, int):
        raise TypeError('maxlen must be type int')
    Shifted = False
    Keys = pygame.key.get_pressed()
    global __HasTyped
    if Keys[pygame.K_LSHIFT] or Keys[pygame.K_RSHIFT]: Shifted = True
    if Keys[pygame.K_RETURN]: return 1
    if Keys[pygame.K_BACKSPACE] and not __HasTyped[pygame.K_BACKSPACE]: Key = Key[:-1]
    if not Shifted:
        if Keys[pygame.K_BACKQUOTE] and not __HasTyped[pygame.K_BACKQUOTE]: Key += '`'
        elif Keys[pygame.K_1] and not __HasTyped[pygame.K_1]: Key += '1'
        elif Keys[pygame.K_2] and not __HasTyped[pygame.K_2]: Key += '2'
        elif Keys[pygame.K_3] and not __HasTyped[pygame.K_3]: Key += '3'
        elif Keys[pygame.K_4] and not __HasTyped[pygame.K_4]: Key += '4'
        elif Keys[pygame.K_5] and not __HasTyped[pygame.K_5]: Key += '5'
        elif Keys[pygame.K_6] and not __HasTyped[pygame.K_6]: Key += '6'
        elif Keys[pygame.K_7] and not __HasTyped[pygame.K_7]: Key += '7'
        elif Keys[pygame.K_8] and not __HasTyped[pygame.K_8]: Key += '8'
        elif Keys[pygame.K_9] and not __HasTyped[pygame.K_9]: Key += '9'
        elif Keys[pygame.K_0] and not __HasTyped[pygame.K_0]: Key += '0'
        elif Keys[pygame.K_MINUS] and not __HasTyped[pygame.K_MINUS]: Key += '-'
        elif Keys[pygame.K_EQUALS] and not __HasTyped[pygame.K_EQUALS]: Key += '='
        elif Keys[pygame.K_q] and not __HasTyped[pygame.K_q]: Key += 'q'
        elif Keys[pygame.K_w] and not __HasTyped[pygame.K_w]: Key += 'w'
        elif Keys[pygame.K_e] and not __HasTyped[pygame.K_e]: Key += 'e'
        elif Keys[pygame.K_r] and not __HasTyped[pygame.K_r]: Key += 'r'
        elif Keys[pygame.K_t] and not __HasTyped[pygame.K_t]: Key += 't'
        elif Keys[pygame.K_y] and not __HasTyped[pygame.K_y]: Key += 'y'
        elif Keys[pygame.K_u] and not __HasTyped[pygame.K_u]: Key += 'u'
        elif Keys[pygame.K_i] and not __HasTyped[pygame.K_i]: Key += 'i'
        elif Keys[pygame.K_o] and not __HasTyped[pygame.K_o]: Key += 'o'
        elif Keys[pygame.K_p] and not __HasTyped[pygame.K_p]: Key += 'p'
        elif Keys[pygame.K_LEFTBRACKET] and not __HasTyped[pygame.K_LEFTBRACKET]: Key += '['
        elif Keys[pygame.K_RIGHTBRACKET] and not __HasTyped[pygame.K_RIGHTBRACKET]: Key += ']'
        elif Keys[pygame.K_BACKSLASH] and not __HasTyped[pygame.K_BACKSLASH]: Key += '\\'
        elif Keys[pygame.K_a] and not __HasTyped[pygame.K_a]: Key += 'a'
        elif Keys[pygame.K_s] and not __HasTyped[pygame.K_s]: Key += 's'
        elif Keys[pygame.K_d] and not __HasTyped[pygame.K_d]: Key += 'd'
        elif Keys[pygame.K_f] and not __HasTyped[pygame.K_f]: Key += 'f'
        elif Keys[pygame.K_g] and not __HasTyped[pygame.K_g]: Key += 'g'
        elif Keys[pygame.K_h] and not __HasTyped[pygame.K_h]: Key += 'h'
        elif Keys[pygame.K_j] and not __HasTyped[pygame.K_j]: Key += 'j'
        elif Keys[pygame.K_k] and not __HasTyped[pygame.K_k]: Key += 'k'
        elif Keys[pygame.K_l] and not __HasTyped[pygame.K_l]: Key += 'l'
        elif Keys[pygame.K_SEMICOLON] and not __HasTyped[pygame.K_SEMICOLON]: Key += ';'
        elif Keys[pygame.K_QUOTE] and not __HasTyped[pygame.K_QUOTE]: Key += '\''
        elif Keys[pygame.K_z] and not __HasTyped[pygame.K_z]: Key += 'z'
        elif Keys[pygame.K_x] and not __HasTyped[pygame.K_x]: Key += 'x'
        elif Keys[pygame.K_c] and not __HasTyped[pygame.K_c]: Key += 'c'
        elif Keys[pygame.K_v] and not __HasTyped[pygame.K_v]: Key += 'v'
        elif Keys[pygame.K_b] and not __HasTyped[pygame.K_b]: Key += 'b'
        elif Keys[pygame.K_n] and not __HasTyped[pygame.K_n]: Key += 'n'
        elif Keys[pygame.K_m] and not __HasTyped[pygame.K_m]: Key += 'm'
        elif Keys[pygame.K_COMMA] and not __HasTyped[pygame.K_COMMA]: Key += ','
        elif Keys[pygame.K_PERIOD] and not __HasTyped[pygame.K_PERIOD]: Key += '.'
        elif Keys[pygame.K_SLASH] and not __HasTyped[pygame.K_SLASH]: Key += '/'
        elif Keys[pygame.K_SPACE] and not __HasTyped[pygame.K_SPACE]: Key += ' '
    elif Shifted:
        if Keys[pygame.K_BACKQUOTE] and not __HasTyped[pygame.K_BACKQUOTE]: Key += '~'
        elif Keys[pygame.K_1] and not __HasTyped[pygame.K_1]: Key += '!'
        elif Keys[pygame.K_2] and not __HasTyped[pygame.K_2]: Key += '@'
        elif Keys[pygame.K_3] and not __HasTyped[pygame.K_3]: Key += '#'
        elif Keys[pygame.K_4] and not __HasTyped[pygame.K_4]: Key += '$'
        elif Keys[pygame.K_5] and not __HasTyped[pygame.K_5]: Key += '%'
        elif Keys[pygame.K_6] and not __HasTyped[pygame.K_6]: Key += '^'
        elif Keys[pygame.K_7] and not __HasTyped[pygame.K_7]: Key += '&'
        elif Keys[pygame.K_8] and not __HasTyped[pygame.K_8]: Key += '*'
        elif Keys[pygame.K_9] and not __HasTyped[pygame.K_9]: Key += '('
        elif Keys[pygame.K_0] and not __HasTyped[pygame.K_0]: Key += ')'
        elif Keys[pygame.K_MINUS] and not __HasTyped[pygame.K_MINUS]: Key += '_'
        elif Keys[pygame.K_EQUALS] and not __HasTyped[pygame.K_EQUALS]: Key += '+'
        elif Keys[pygame.K_q] and not __HasTyped[pygame.K_q]: Key += 'Q'
        elif Keys[pygame.K_w] and not __HasTyped[pygame.K_w]: Key += 'W'
        elif Keys[pygame.K_e] and not __HasTyped[pygame.K_e]: Key += 'E'
        elif Keys[pygame.K_r] and not __HasTyped[pygame.K_r]: Key += 'R'
        elif Keys[pygame.K_t] and not __HasTyped[pygame.K_t]: Key += 'T'
        elif Keys[pygame.K_y] and not __HasTyped[pygame.K_y]: Key += 'Y'
        elif Keys[pygame.K_u] and not __HasTyped[pygame.K_u]: Key += 'U'
        elif Keys[pygame.K_i] and not __HasTyped[pygame.K_i]: Key += 'I'
        elif Keys[pygame.K_o] and not __HasTyped[pygame.K_o]: Key += 'O'
        elif Keys[pygame.K_p] and not __HasTyped[pygame.K_p]: Key += 'P'
        elif Keys[pygame.K_LEFTBRACKET] and not __HasTyped[pygame.K_LEFTBRACKET]: Key += '{'
        elif Keys[pygame.K_RIGHTBRACKET] and not __HasTyped[pygame.K_RIGHTBRACKET]: Key += '}'
        elif Keys[pygame.K_BACKSLASH] and not __HasTyped[pygame.K_BACKSLASH]: Key += '|'
        elif Keys[pygame.K_a] and not __HasTyped[pygame.K_a]: Key += 'A'
        elif Keys[pygame.K_s] and not __HasTyped[pygame.K_s]: Key += 'S'
        elif Keys[pygame.K_d] and not __HasTyped[pygame.K_d]: Key += 'D'
        elif Keys[pygame.K_f] and not __HasTyped[pygame.K_f]: Key += 'F'
        elif Keys[pygame.K_g] and not __HasTyped[pygame.K_g]: Key += 'G'
        elif Keys[pygame.K_h] and not __HasTyped[pygame.K_h]: Key += 'H'
        elif Keys[pygame.K_j] and not __HasTyped[pygame.K_j]: Key += 'J'
        elif Keys[pygame.K_k] and not __HasTyped[pygame.K_k]: Key += 'K'
        elif Keys[pygame.K_l] and not __HasTyped[pygame.K_l]: Key += 'L'
        elif Keys[pygame.K_SEMICOLON] and not __HasTyped[pygame.K_SEMICOLON]: Key += ':'
        elif Keys[pygame.K_QUOTE] and not __HasTyped[pygame.K_QUOTE]: Key += '"'
        elif Keys[pygame.K_z] and not __HasTyped[pygame.K_z]: Key += 'Z'
        elif Keys[pygame.K_x] and not __HasTyped[pygame.K_x]: Key += 'X'
        elif Keys[pygame.K_c] and not __HasTyped[pygame.K_c]: Key += 'C'
        elif Keys[pygame.K_v] and not __HasTyped[pygame.K_v]: Key += 'V'
        elif Keys[pygame.K_b] and not __HasTyped[pygame.K_b]: Key += 'B'
        elif Keys[pygame.K_n] and not __HasTyped[pygame.K_n]: Key += 'N'
        elif Keys[pygame.K_m] and not __HasTyped[pygame.K_m]: Key += 'M'
        elif Keys[pygame.K_COMMA] and not __HasTyped[pygame.K_COMMA]: Key += '<'
        elif Keys[pygame.K_PERIOD] and not __HasTyped[pygame.K_PERIOD]: Key += '>'
        elif Keys[pygame.K_SLASH] and not __HasTyped[pygame.K_SLASH]: Key += '?'
    while len(Key) > maxlen: Key = Key[:-1]
    __HasTyped = Keys
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

class text_box():
'''Hold a collection of text in one area. text won't wrap'''
    def __init__(self, bounds, coords):
        self.rect = Rect(coords,bounds)
        self.text = []
        self.tcol = (0,0,0)
        self.bcol = (255,255,255)
        self.size = 8
    def add_line(self, text_line):
        self.text.append(text_line)
    def edit_text_attributes(self, text_color = (0,0,0), font_size = 8, backround_color = (255,255,255), justify = 'left'):

    def render(self):
