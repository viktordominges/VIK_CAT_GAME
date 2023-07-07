# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:53:16 2023

@author: vikto
"""
import pygame
from sprites import *
from configuration import *
import math

class Weapon(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
         
        self.game = game
        self._layer = WEAPON_LAYER
        self.groups = self.game.all_sprites, self.game.weapons
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.weapon_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.animationCounter = 1
        
    def animate(self):
        
        animation = [
            self.game.weapon_spritesheet.get_image(0, 0, self.width, self.height),
            self.game.weapon_spritesheet.get_image(32, 0, self.width, self.height),
            self.game.weapon_spritesheet.get_image(64, 0, self.width, self.height)
            ]
        self.image = animation[math.floor(self.animationCounter)]
        self.animationCounter += 0.1
        if self.animationCounter >= 3:
            self.animationCounter = 0
            
    def update(self):
        self.animate()
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
         
        self.game = game
        self._layer = BULLET_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = self.game.player.direction
        self.demage = 1
        
    def move_bullet(self):

        if self.direction == 'right':
            self.rect.x += BULLET_STEPS

        elif self.direction == 'left':
            self.rect.x -= BULLET_STEPS

        elif self.direction == 'up':
            self.rect.y -= BULLET_STEPS

        elif self.direction == 'down':
            self.rect.y += BULLET_STEPS
            
    def collide_block(self):
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if collide:
            self.kill()
            
    def collide_enemy(self):
        collide = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if collide:
            collide[0].demage(self.demage)
            self.kill()
        
    def update(self):
        self.move_bullet()
        self.collide_block()
        self.collide_enemy()
        
        
class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
         
        self.game = game
        self._layer = BULLET_LAYER
        self.groups = self.game.all_sprites, self.game.bullets
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.bullet_spritesheet.get_image(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.direction = self.game.player.direction
        self.demage = 1
        
    def move_bullet(self):

        if self.direction == 'right':
            self.rect.x += BULLET_STEPS

        elif self.direction == 'left':
            self.rect.x -= BULLET_STEPS

        elif self.direction == 'up':
            self.rect.y -= BULLET_STEPS

        elif self.direction == 'down':
            self.rect.y += BULLET_STEPS
            
    def collide_block(self):
        collide = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if collide:
            self.kill()
            
    def collide_player(self):
        collide = pygame.sprite.spritecollide(self, self.game.mainPlayer, False)
        if collide:
            self.game.player.demage(self.demage)
            self.kill()
        
    def update(self):
        self.move_bullet()
        self.collide_block()
        self.collide_player()
        