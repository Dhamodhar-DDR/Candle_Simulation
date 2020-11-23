
# import pygame module in this program  
import pygame 
  
# activate the pygame library .   
# initiate pygame and give permission   
# to use pygame's functionality.   
pygame.init() 
  
# create the display surface object   
# of specific dimension..e(500, 500).   
win = pygame.display.set_mode((1900, 950)) 
  
# set the pygame window name  
pygame.display.set_caption("Moving rectangle") 

x = 200
y = 200
width = 400
height = 350
run = True
wellwidth = 0
wellheight = 0
moltenheight = 0

# infinite loop  
while run: 
    pygame.time.delay(40) 
      
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False         
              
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 100, 0), (x, y, width, height))   
    pygame.draw.rect(win, (0, 0, 0), (x + width/2 - (wellwidth/2), y, wellwidth, wellheight))
    pygame.draw.rect(win, (150, 100, 0), (x + width/2 - (wellwidth/2), y+wellheight-moltenheight, wellwidth, moltenheight))   
    
    if(wellheight<100):
        wellheight +=2
    if(wellwidth<100):
        wellwidth +=1
    if(moltenheight<50):
        moltenheight += 1

    pygame.display.update()  
  
# closes the pygame window  
pygame.quit() 