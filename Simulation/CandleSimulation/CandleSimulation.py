import pygame 
import math

pygame.init() 

win = pygame.display.set_mode((1900, 1050)) 
  
# set the pygame window name  
pygame.display.set_caption("Moving rectangle") 

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render(str(0), True, green, blue) 

text2 = font.render(str(1), True, green, blue) 

textRect = text.get_rect()  
textRect.center = (400 // 2, 400 // 2) 

textRect2 = text2.get_rect()  
textRect2.center = (400 // 2, 200 // 2) 

timefactor =1

x = 600
y = 200
width = 700
height = 1050
run = True
wellwidth = 0
wellheight = 105
moltenheight = 0
time = 0

l = 2.2
d = 0.229

def play():
  # infinite loop  
  while run: 
      pygame.time.delay(10) 

      for event in pygame.event.get(): 
          if event.type == pygame.QUIT: 
              run = False
          if event.type == pygame.KEYDOWN:
              if (event.key == pygame.K_UP):
                  timefactor += 5
              elif (event.key == pygame.K_DOWN) and timefactor > 6:
                  timefactor += -5
      win.fill((0, 0, 0))

      pygame.draw.rect(win, (255, 100, 0), (x, y, width, height))   
      pygame.draw.rect(win, (0, 0, 0), (x + width/2 - (wellwidth/2), y, wellwidth, wellheight))
      pygame.draw.rect(win, (150, 100, 0), (x + width/2 - (wellwidth/2), y+wellheight-moltenheight, wellwidth, moltenheight))   

      if(time<3759):
          wellheight = 100*( 1.25 - (pow((time-4000),2))/12800000)
      else:
          wellheight = 100*(1.05 + 0.000052*(time))
      print wellheight
      # if(wellheight<100):
      #     wellheight += 2
      wellwidth = 200*(2.2 - (pow((2.2 - 0.29),(1-(time/3000))))*(pow((2.2 -2),(time/3000)))) 
      # print(wellwidth)
      if(time<8000):
          moltenheight = 100*(64 - pow((time/1000)-8,2))/128
      else:
          moltenheight = 50

      text = font.render(str(time), True, green, blue)
      text2 = font.render(str(timefactor), True, green, blue) 

      time+=(0.01*timefactor)
      # print(timefactor)
      win.blit(text, textRect) 
      win.blit(text2, textRect2) 
      pygame.display.update()  

play()

# closes the pygame window  
pygame.quit() 
