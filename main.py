#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:45:00 2022

@author: burak
"""

import pygame

pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('assets/font/Sansburg.ttf', 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
bgs = []
banners = []
guns = []
level = 2
for i in range(1,4):
    bgs.append(pygame.image.load(f'assets/bgs/{i}.png'))
    banners.append(pygame.image.load(f'assets/banners/{i}.png'))
    guns.append(pygame.image.load(f'assets/guns/{i}.png'))
    
run = True
while run:
    timer.tick(fps)
    
    screen.fill('black')
    screen.blit(bgs[level -1], (0, 0))
    screen.blit(banners[level -1], (HEIGHT, 200))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
##pygame.quit()