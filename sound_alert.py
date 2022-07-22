import pygame
 
#init
pygame.mixer.init()
 
#load file
pygame.mixer.music.load("/home/pi/G_space_mini/alarm.mp3")
 
#play
pygame.mixer.music.play()
 
#끝까지 재생할때까지 기다린다.
while pygame.mixer.music.get_busy() == True:
    continue

    
pygame.mixer.music.load("/home/pi/G_space_mini/alarm.mp3")
pygame.mixer.music.play()






