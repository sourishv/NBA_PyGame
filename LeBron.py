# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo_LeBron.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,600))
     
    # define a variable to control the main loop
    running = True
     
    #load image
    image = pygame.image.load("basketball.png")
    #Colorkey makes pixels w same color not be drawn - white here
    image.set_colorkey((255,255,255))
    #transparency: 0 - 255, 0 is transparent, 255 is opaque; 128 special value, faster than other per-surface values
    image.set_alpha(128)
    #blit
    screen.blit(image, (50, 50))
    #update screen
    pygame.display.flip()
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()