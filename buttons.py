import pygame
import images as i

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    
    def draw(self, surface):    
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def make_action(self):
        action = False

        mouse_position = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
    
        return action
    
    def hover_action(self):
        action = False

        mouse_position = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_position):
            action = True
        
        return action


# back button
back_button = Button(20, 20, i.back_button_image)

# first page buttons
start_game_button = Button(0, 0, i.background)
play_button = Button(368, 132, i.play_button_image)
balance_button = Button(368, 216, i.balance_image)
rules_button = Button(368, 300, i.rules_image)
settings_button = Button(368, 384, i.settings_image)

# balance page buttons
tick_button_balance = Button(368, 380, i.tick_button_image)

# play page buttons
tick_button_bet = Button(200, 200, i.tick_button_image)
hit_button = Button(550, 450, i.hit_stay_button_image)
stay_button = Button(650, 450, i.hit_stay_button_image)
restart_button = Button(100, 100, i.restart_button_image)