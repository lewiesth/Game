# Import relevant packages
import sys
###sys module to exit the game###
import pygame

Define classes
    Settings to determine background settings
    Ship to load player sprite and define initial position


class Settings():
    
    def __init__(self):
        ###Screen settings###
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        ###In pygame, (0,0) is top left of screen, (max.x,max.y) is the bottom right###
        self.ship_speed_factor=1.5
        ###Gives a dynamic figure of ship speed###


class Ship():
    
    def __init__(self,ai_settings,screen):
        self.screen=screen
        self.ai_settings=ai_settings
        
        self.image=pygame.image.load('BMP.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        ###Load image and get its rect(rectangle even though it may not be rectangle in shape. Allows for x,y coordinates to be used)###
        
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        ###start ship at bottom center of screen. Centerx is the x-coordinate of the center of the ship###
        
        self.center=float(self.rect.centerx)
        ###converts rect.centerx into float since ship_speed_factor from Settings() is float and rect can only store int###
        
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
        ###if self.moving_right is True (from check_events) AND coordinates does not exceed max###
        ###self.rect.right returns xcoordinates of right edge of ship,self.screen_rect.right return right max of screen###
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor
        ###Adds a dyanmic speed value to the movement of the ship by factor in Settings###
        self.rect.centerx=self.center
        ###Coordinates increases factor amount when key is pressed ###
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        ###Draw ship at current location###
        

#Define controls
    #Check_events to check for player input and corresponding returns for KEYDOWN/KEYUP


def check_events(ship):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                ###if player exits file through top right X, exit application with sys.exit()###
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ship)
            ###KEYDOWN to detect input###
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
            ###KEYUP to detect when input ends###



def check_keydown_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
                ###if input is right key, update moving_right (from class Ship()) to True###
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True



def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right =False
                ###when K_RIGHT is no longer pressed to update moving_right from check_keydown_events to False###
    elif event.key == pygame.K_LEFT:
        ship.moving_left =False



def update_screen(ai_settings,screen,ship):
        screen.fill(ai_settings.bg_color)
        ### fill('color')###
        ship.blitme()
        ###updates ship position###
        pygame.display.flip()
        ###will be used to update the shown image to give impression of fluidity###


# Body of the game

###basic running of game to initialise the window, and its size and to close###
def run_game():
    pygame.init()
    ###init() initialises the game###
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ###Calls the .screen_width,.screen_height from Settings() class###
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings,screen)
    ###must be before while loop so not initialised every loop###
    while True:
    ###while loop used to listen for events; input by player to react accordingly###
        check_events(ship)
        ###checks the input by running check_events() function ###
        ship.update()
        update_screen(ai_settings,screen,ship)
        ###Update screen settings accordingly###


run_game()





