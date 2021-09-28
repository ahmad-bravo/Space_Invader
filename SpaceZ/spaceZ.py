import pygame
import random

# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf

# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
from starship import Starship
from aliens import Roadster
from bitcoin import Bitcoin


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    
    # Set keys to repeat if held down.
    pygame.key.set_repeat(5,5)
    
    # Create settings object containing game settings
    ai_settings = Settings()

    # Create the main game screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Create a main window caption
    pygame.display.set_caption("Space Z - Mars Flight")

   
     # Function for displaying a message
    def show_msg(msg,x,y,font_size):
        font = pygame.font.Font("freesansbold.ttf",font_size)
        message = font.render(msg,True,(255,0,0))
        screen.blit(message,(x,y))

    
    while ai_settings.lives > 0:
    
        # ** CODE TO CREATE SPRITES/GROUPS GOES HERE **

        #creating instances
        the_ship = Starship(200,400,ai_settings)
        bitcoin = Bitcoin()

        #Creating groups
        starship_group = pygame.sprite.Group()
        roadster_group = pygame.sprite.Group()
        bitcoin_group = pygame.sprite.Group()

        #Adding to groups
        starship_group.add(the_ship)
        bitcoin_group.add(bitcoin)

        #creating 20 roadsters
        roadsters = []
        for x in range(ai_settings.aliens):

            # Setting random speed and postion of a roadster
            new_roadster = Roadster(speed = random.randint(1,15),pos_y = random.randrange(0,ai_settings.screen_height))

            # Adding roadsters to the list and the group
            roadsters.append(new_roadster)
            roadster_group.add(new_roadster)

        


        # Start the main loop for the game.
        while the_ship.damage < 100:

            #Bitcoin Mining 
            if bitcoin.mining < 100 :
                bitcoin.mining += 1


            # Watch for keyboard events.
            gf.check_events(screen, the_ship, bitcoin,ai_settings)
 
            # Now update the sprites, etc. on the screen
            screen.blit(ai_settings.screen_backgrnd, (0,0))


            # Displaying all the statistics
            show_msg(str(f"{the_ship.damage} %"),x = 100, y = 15,font_size = 15)
            show_msg(str(ai_settings.lives),x = 250, y = 15,font_size = 15)
            show_msg(str(ai_settings.score),x = 100, y = 45,font_size = 15)
            show_msg(str(bitcoin.mining),x = 350, y = 40,font_size = 15)
            
            # Drawing the spaceships and the roadsters
            starship_group.draw(screen)
            roadster_group.draw(screen)

            # Draw the bitcoin if it is to be displayed
            if bitcoin.display:
                bitcoin_group.draw(screen)

            # Updating the screen
            gf.update_screen(ai_settings,screen, the_ship, bitcoin, roadster_group, roadsters)


        #Show message
        Display_crashed = True

        while Display_crashed:

            # Show the crashed message
            show_msg("You have Crashed",x = 350, y = 300,font_size = 65)
            pygame.display.update()

            # Checking if any key has been pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    Display_crashed = False

        # Remove a life
        ai_settings.lives -= 1

    # GAME ENDS 

# Call the main method to start the game        
run_game()
