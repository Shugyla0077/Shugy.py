import pygame 
import math
pygame.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
brush_radius=5
shape_thickess=3
mode='blue'
tool='brush'
points=[]
drawing=False
start_pos=(0,0)
