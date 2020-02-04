#！/usr/bin/python3
#-*- coding:utf-8 -*-


import time
import os
import threading
import sys

import pygame

pygame.init()
pygame.mixer.set_num_channels(128)#多通道

screen = pygame.display.set_mode((500, 304))
pygame.display.set_caption('Py-Piano') # 设置窗口标题
background=pygame.image.load(r".//music.png") #设置窗口背景
screen.blit(background,(0,0))  #对齐的坐标
pygame.display.update()   #显示内容


keyDict={
    pygame.K_1:"c",
    pygame.K_2:"d",
    pygame.K_3:"e",
    pygame.K_4:"f",
    pygame.K_5:"g",
    pygame.K_6:"a",
    pygame.K_7:"b",
    pygame.K_8:"c1",
    pygame.K_9:"d1",
    pygame.K_0:"e1",
    pygame.K_MINUS:"f1",

    pygame.K_EQUALS:'g1',
    pygame.K_q:'a1',
    pygame.K_w:'b1',
    pygame.K_e:'c2',
    pygame.K_r:'d2',
    pygame.K_t:'e2',
    pygame.K_y:'f2',
    pygame.K_u:'g2',
    pygame.K_i:'a2',
    pygame.K_o:'b2',
    pygame.K_p:'c3',
    pygame.K_a:'d3',
    pygame.K_s:'e3',
    pygame.K_d:'f3',
    pygame.K_f:'g3',
    pygame.K_g:'a3',
    pygame.K_h:'b3',

    pygame.K_j:'c4',
    pygame.K_k:'d4',
    pygame.K_l:'e4',
    pygame.K_z:'f4',
    pygame.K_x:'g4',
    pygame.K_c:'a4',
    pygame.K_v:'b4',
    pygame.K_b:'c5'
}


while True:
    #time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = event.key
            if(key == pygame.K_ESCAPE):
                pygame.quit()

            elif key in keyDict.keys():
                fileName = "./audios/"+str(keyDict[key])+".wav"
                if os.path.exists(fileName):
                    print(keyDict[key],end=' ')
                    pygame.mixer.Sound(fileName).play()

