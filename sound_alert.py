import pygame

 
pygame.mixer.init(16000)
#pygame.mixer.pre_init(44100,-16,2,512)


 
#load file
pygame.mixer.music.load("/home/pi/G_space_mini/alarm.mp3")
 
#play
pygame.mixer.music.play()
 
#끝까지 재생할때까지 기다린다.
while pygame.mixer.music.get_busy() == True:
    continue

    
pygame.mixer.music.load("/home/pi/G_space_mini/alarm.mp3")
pygame.mixer.music.play()



