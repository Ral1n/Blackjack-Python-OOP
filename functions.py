import pygame
import blackjack
import buttons as b
import images

def drawText(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def dealCard(deck):
    card = deck.deal_one()
    return card.__str__()

def addCard(list, deck):
    card = dealCard(deck)
    list.append(card)

def drawCard(surface, card, x, y):
    card_list = list(card.split(' '))
    image = 'images/playing_cards/' + card_list[0] + '_' + card_list[1] + '_' + card_list[2] + '.png'
    card_image = pygame.image.load(image)
    surface.blit(card_image, (x, y))

def hitAction(count, player_cards, dealer_cards, surface):
    j = 0
    for i in range(count+1,-1,-1):
        drawCard(surface, player_cards[i], 400-j*100 ,400)
        j+=1
    drawCard(surface, dealer_cards[0], 300, 100)
    surface.blit(images.back_of_card, (400, 100))
    b.hit_button.draw(surface)
    b.stay_button.draw(surface)