import pygame 
import buttons as b
import blackjack
import functions as f
import images as img


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine': 9, 'Ten':10, 'Ace':11, 'Jack':10, 'Queen':10, 'King':10}

pygame.init()

clock = pygame.time.Clock()

# game window width and height 
game_window_width = 800
game_window_height = 600

# initialize game window
game_window = pygame.display.set_mode((game_window_width, game_window_height))

# set icon and game title
pygame.display.set_caption('21 BlackJack')
game_logo_icon = pygame.image.load('images/blackjack.png')
pygame.display.set_icon(game_logo_icon)

font_60 = pygame.font.Font('fonts/Headmong Rounded-SemiBold.otf', 60)
font_36 = pygame.font.Font('fonts/Headmong Rounded-SemiBold.otf', 36)
font_24 = pygame.font.Font('fonts/Headmong Rounded-SemiBold.otf', 24)

running = True
page = 0

# balance page variables
balance_input = ''
show_balance = False
enter_amount = False
balance_page_back_button_count = 0

# game logic variables
deck = blackjack.Deck()
deck.shuffle()
enter_bet = False
bet_input = ''
start_game = False
balance_int = 0
bet_int = 0

dealer_cards, player_cards = [], []

stage_one, draw_stage_one = True, True

hit, stay = False, False

deal1, deal2, deal3 = True, True, True

count_hit = 0
count_dealer_cards = 2

show = False
shuffle = True

final = False

player_won, tie, dealer_won, bust = False, False, False, False
modify_balance = True

while running:

    game_window.fill((0, 0, 0))

    if page == 0:

        game_window.blit(img.background, (0, 0))
    
        if b.start_game_button.make_action():
            page = 1
    
    # first page (with all the buttons)
    if page == 1:
        
        if b.play_button.hover_action():
            f.drawText(game_window, 'PLAY', font_60, (255,255,255), 350, 130)
        else:
            b.play_button.draw(game_window)
        
        if b.balance_button.hover_action():
            f.drawText(game_window, 'BALANCE', font_60, (255,255,255), 305, 210)
        else:
            b.balance_button.draw(game_window)

        if b.rules_button.hover_action():
            f.drawText(game_window, 'RULES', font_60, (255,255,255), 335, 290)
        else:
            b.rules_button.draw(game_window)  

        if b.settings_button.hover_action():
            f.drawText(game_window, 'SETTINGS', font_60, (255,255,255), 300, 370)
        else:
            b.settings_button.draw(game_window)  

        if b.play_button.make_action():
            page = 2

        if b.balance_button.make_action():
            page = 3
        
        if b.rules_button.make_action():
            page = 4
        
        if b.settings_button.make_action():
            page = 5
            
    # game page (after pressing PLAY button)
    if page == 2:
        game_window.fill((150,150,170))

        b.back_button.draw(game_window)
        if b.back_button.make_action():
            page = 1

        pygame.draw.line(game_window, (128, 128, 128), (0, 500), (800, 500), 5)
        pygame.draw.line(game_window, (128, 128, 128), (250, 500), (250, 600), 5)
        pygame.draw.line(game_window, (128, 128, 128), (550, 500), (550, 600), 5)

        if balance_int == 0:
            game_window.fill((255,255,255))
            f.drawText(game_window, 'YOUR BALANCE IS ZERO', font_60, (255,0,0), 150, 250)
            f.drawText(game_window, 'PLEASE DEPOSIT SOME MONEY', font_60, (255,0,0), 90, 300)
        
        enter_bet = True

        f.drawText(game_window, f'BALANCE', font_36, (255, 255, 255), 50, 520)
        f.drawText(game_window, f'{balance_int}', font_36, (255, 255, 255), 50, 560)
        
        f.drawText(game_window, 'ENTER YOUR BET', font_36, (255,255,255), 290, 510)
        f.drawText(game_window, bet_input, font_36, (255,0,0), 350, 550)

        b.tick_button_bet.draw(game_window)

        if b.tick_button_bet.make_action():
            start_game = True
                
            bet_int = int(bet_input)
            balance_int -= bet_int
            bet_input = ''
            
        if start_game:

            game_window.blit(img.dealer, (336, 0))

            if stage_one:
                for i in range(2):
                    f.addCard(player_cards, deck)
                    f.addCard(dealer_cards, deck)
                    
                player_score = values[player_cards[0].split(' ')[0]] + values[player_cards[1].split(' ')[0]]
                dealer_score = values[dealer_cards[0].split(' ')[0]] + values[dealer_cards[1].split(' ')[0]]

                stage_one = False
            
            if draw_stage_one:
                f.drawCard(game_window, player_cards[0], 300, 400)
                f.drawCard(game_window, player_cards[1], 400, 400)
                f.drawCard(game_window, dealer_cards[0], 300, 100)
                game_window.blit(img.back_of_card, (400, 100))
                b.hit_button.draw(game_window)
                b.stay_button.draw(game_window)

            if b.hit_button.make_action():
                count_hit += 1
                
            if b.stay_button.make_action():
                stay = True

            if count_hit == 1:
                if deal1:
                   f.addCard(player_cards, deck)
                   player_score += values[player_cards[2].split(' ')[0]]
    
                   deal1 = False
                
                if player_score > 21:
                    final = True
                
                f.hitAction(count_hit, player_cards, dealer_cards, game_window)
                draw_stage_one = False
                    
            if count_hit == 2:
                if deal2:
                    f.addCard(player_cards, deck)
                    player_score += values[player_cards[3].split(' ')[0]]

                    deal2 = False
                
                if player_score > 21:
                    final = True
                
                f.hitAction(count_hit, player_cards, dealer_cards, game_window)

            if count_hit == 3:
                if deal3:
                    f.addCard(player_cards, deck) 
                    player_score += values[player_cards[4].split(' ')[0]]

                    deal3 = False
                
                if player_score > 21:
                    final = True
                
                f.hitAction(count_hit, player_cards, dealer_cards, game_window)
            
            if count_hit > 3:
                f.hitAction(3, player_cards, dealer_cards, game_window)
                f.drawText(game_window, 'ERROR', font_36, (255,0,0), 500, 500)
            
            if stay:
                f.drawCard(game_window, dealer_cards[1], 400, 100)
                while dealer_score <= 17:
                    f.addCard(dealer_cards, deck)
                    dealer_score += values[dealer_cards[count_dealer_cards].split(' ')[0]]
                    count_dealer_cards += 1
                    show = True

                if show:
                   f.drawCard(game_window, dealer_cards[1], 400, 100)
                   f.drawCard(game_window, dealer_cards[count_dealer_cards - 1], 200, 100)
                   if dealer_cards[count_dealer_cards - 2] != dealer_cards[1]:
                       f.drawCard(game_window, dealer_cards[count_dealer_cards - 2], 100, 100)
                   if dealer_cards[count_dealer_cards - 3] != dealer_cards[1] and dealer_cards[count_dealer_cards - 3] != dealer_cards[0]:
                       f.drawCard(game_window, dealer_cards[count_dealer_cards - 3], 0, 100)
                else:
                   f.drawCard(game_window, dealer_cards[1], 400, 100)

                final = True
            
            if final: 
                if (player_score < 21 and 21 - player_score < 21 - dealer_score) or (player_score == 21 and dealer_score != 21) or dealer_score > 21:
                    player_won = True
                elif player_score == dealer_score or (player_score == 21 and dealer_score == 21):
                    tie = True
                elif (dealer_score < 21 and 21 - dealer_score < 21 - player_score) or (dealer_score == 21 and player_score != 21): 
                    dealer_won = True
                elif player_score > 21:
                    bust = True
            
                if player_won:
                    f.drawText(game_window, 'PLAYER WON', font_60, (255,0,0), 300, 300)
                    b.restart_button.draw(game_window)
                    if modify_balance:
                        balance_int += 2*bet_int
                        modify_balance = False
                
                if tie:
                    f.drawText(game_window, 'TIE', font_60, (255,0,0), 300, 300)
                    b.restart_button.draw(game_window)
                    if modify_balance:
                        balance_int += bet_int
                        modify_balance = False
                
                if dealer_won:
                    f.drawText(game_window, 'DEALER WON', font_60, (255,0,0), 300, 300)
                    b.restart_button.draw(game_window)
        
                if bust:
                   f.drawText(game_window, 'BUST! DEALER WON', font_60, (255,0,0), 300, 300) 
                   b.restart_button.draw(game_window)

                if b.restart_button.make_action():            
                    start_game = False
                    enter_bet = False

                    deck = blackjack.Deck()

                    player_cards, dealer_cards = [], []

                    player_score, dealer_score = 0, 0

                    stage_one, draw_stage_one = True, True

                    hit, stay = False, False

                    deal1, deal2, deal3 = True, True, True

                    count_hit = 0
                    count_dealer_cards = 2

                    show = False
                    shuffle = True

                    final = False
                    modify_balance = True

                    player_won, tie, dealer_won, bust = False, False, False, False

                    if shuffle:
                        deck.shuffle()
                        shuffle = False
                      
    # balance page (after pressing BALANCE button)
    if page == 3:
        game_window.fill((100, 120, 100))
        enter_amount = True

        b.back_button.draw(game_window)
        if b.back_button.make_action():
            page = 1
            if show_balance:
                balance_page_back_button_count += 1

        if show_balance == False and balance_page_back_button_count == 0:
            f.drawText(game_window, 'BALANCE', font_60, (255,255,255), 305, 130)

            f.drawText(game_window, 'Please enter an amount of money', font_36, (255,255,255), 180, 210)

            game_window.blit(img.input_box, (336, 250))

            b.tick_button_balance.draw(game_window)
            
            f.drawText(game_window, balance_input, font_36, (255,255,255), 345, 288)

            if b.tick_button_balance.make_action() and balance_input != '' and balance_input.isdigit() == True:
                show_balance = True
            elif balance_input != '' and balance_input.isdigit() == False:
                f.drawText(game_window, 'Invalid Amount', font_24, (255,0,0), 340, 340) 
        
        if balance_input != '' and balance_input.isdigit() and show_balance and balance_page_back_button_count == 0:
            f.drawText(game_window, 'BALANCE', font_60, (255,255,255), 305, 70)
            f.drawText(game_window, f'You deposited ${balance_input}!', font_36, (255,255,255), 260, 150)
            game_window.blit(img.money_bag, (240, 200))
            f.drawText(game_window, f'{balance_input}', font_60, (0,0,0), 350, 450)
            balance_int = int(balance_input)
        
        if balance_page_back_button_count > 0 and show_balance:
            f.drawText(game_window, 'BALANCE', font_60, (255,255,255), 305, 70)
            game_window.blit(img.money_bag, (240, 180))
            f.drawText(game_window, f'{balance_input}', font_60, (0,0,0), 350, 430)  
    
    # rules page (after pressing RULES button)
    if page == 4:
        b.back_button.draw(game_window)
    
    # settings page (after pressing SETTINGS button)
    if page == 5:
        b.back_button.draw(game_window)

    # quit the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if enter_amount:
                    balance_input = balance_input[:-1]
                if enter_bet:
                    bet_input = bet_input[:-1]
            elif event.key != pygame.K_RETURN:
                if len(balance_input) < 6 and enter_amount:
                    balance_input += event.unicode  
                if len(bet_input) < 6 and enter_bet:
                    bet_input += event.unicode
            else:
                if balance_input != '':
                    show_balance = True
                
    pygame.display.update()
    
    clock.tick(90)