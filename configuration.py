# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:50:22 2023

@author: vikto
"""

WIN_WIDTH = 800
WIN_HEIGHT = 600
TILESIZE = 32
FPS = 60

GROUND_LAYER = 1
BLOCKS_LAYER = 2
ENEMY_LAYER = 3
WEAPON_LAYER = 4
PLAYER_LAYER = 5
HEALTH_LAYER = 6
BULLET_LAYER = 7

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

PLAYER_STEPS = 3
ENEMY_STEPS = 1
BULLET_STEPS = 6

ENEMY_HEALTH = 6
PLAYER_HEALTH = 10

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B....BBB.............................................B',
    'B......................E............BBB..............B',
    'B...........BBBB....................BBBB...........RRB',
    'B............BBB.....................BB...........RRRB',
    'B.........................BBB..............E........RB',
    'B......E....B..............BBB.......................B',
    'B.........BBBB...........BBB..........RRRRR..........B',
    'B............P..W......................RRRRR.........B',
    'B..............RRR..................RRRRRR...........B',
    'B.....BBB.....RRRR...................................B',
    'B......BB......................BBBB..............RRRRB',
    'B............................BBBB..............RRRRRRB',
    'B.............BBB...............................RRRRRB',
    'B........E...BBBBB.......................E.......RRR.B',
    'B.............BB.....................................B',
    'B...RRR.................E......BBBB..................B',
    'BRRRRRRR.........................BBB.................B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    ]