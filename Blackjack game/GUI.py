import pygame
import Blackjack
import os
import csv

tick = 0
blackjack = Blackjack.Blackjack()
running = True
pygame.init()
pygame.display.set_caption("Blackjack")
font = pygame.font.Font(os.path.join("assets", "TimesNewRoman.ttf"), 35)
screen = pygame.display.set_mode((800, 550))
clock = pygame.time.Clock()
policy = []
with open('res.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        policy.append(row)
win=0
lose=0
score=0
can=0

while running:
    tick += 1

    image = pygame.image.load(os.path.join("assets", "back.png"))
    hit = pygame.image.load(os.path.join("assets", "hit.png"))
    stand = pygame.image.load(os.path.join("assets", "stand.png"))
    double = pygame.image.load(os.path.join("assets", "double.png"))
    restart = pygame.image.load(os.path.join("assets", "restart.png"))

    image = pygame.transform.scale(image, (900, 600))
    restart = pygame.transform.scale(restart, (50, 50))

    screen.blit(image, (0, 0))
    screen.blit(hit, (500, 450))
    screen.blit(stand, (600, 450))
    screen.blit(double, (700, 450))
    screen.blit(restart, (30, 460))

    if not blackjack.isPlayer:
        blackjack.dealer_plays()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 568>x>500 and 520>y>450:
                blackjack.player_plays(0)
            if 668>x>600 and 520>y>450:
                blackjack.player_plays(1)
            if 768>x>700 and 520>y>450:
                blackjack.player_plays(2)
            if 80 > x > 30 and 510 > y > 460:
                blackjack.start_game()
                can = 0

    player = font.render("Player: " + str(blackjack.player.get_total()), False, (255, 255, 255))
    for card in range(len(blackjack.player.hand)):
        picture = pygame.image.load(os.path.join("assets", blackjack.player.hand[card] + ".png"))
        picture = pygame.transform.scale(picture, (125, 182))
        screen.blit(picture, (200 + 50 * card, 260))
    screen.blit(player, (10, 260))

    dealer = font.render("Dealer: " + str(blackjack.dealer.get_total()), False, (255, 255, 255))
    for card in range(len(blackjack.dealer.hand)):
        picture1 = pygame.image.load(os.path.join("assets", blackjack.dealer.hand[card] + ".png"))
        picture1 = pygame.transform.scale(picture1, (125, 182))
        screen.blit(picture1, (200 + 50 * card, 10))
    screen.blit(dealer, (10, 10))

    if blackjack.player.aces > 0:
        ace_score = 100
    else:
        ace_score = 0
    screen.blit(font.render("Score:" + str(score), False, (255, 255, 255)), (640, 10))

    if blackjack.player.aces > 0:
        ace_score = 100-9
    else:
        ace_score = 0




    if can==0 and blackjack.get_reward() > 0:
        win += 1
        score+=blackjack.get_reward()
        can=1

    if can==0 and blackjack.get_reward() < 0:
        lose += 1
        score+=blackjack.get_reward()
        can=1

    p = policy[blackjack.get_player_state() - 2 - ace_score][blackjack.get_dealer_state() - 2]
    ql=""
    if p == " H" or p == "H":
        ql = "Hit"
    if p == " S" or p == "S":
        ql = "Stand"
    if p == " D" or p == "D":
        ql = "Double"
    if blackjack.isRunning:
        screen.blit(font.render("QL: " + str(ql), False, (255, 255, 255)), (550, 400))

    if blackjack.isRunning == False:
        screen.blit(font.render("Reward=" + str(blackjack.get_reward()), False, (255, 255, 255)), (350, 200))

    screen.blit(font.render("Score:" + str(score), False, (255, 255, 255)), (640, 10))
    screen.blit(font.render("Win:" + str(win), False, (255, 255, 255)), (660, 60))
    screen.blit(font.render("Lose:" + str(lose), False, (255, 255, 255)), (650, 110))

    pygame.display.flip()

    clock.tick(10)

pygame.quit()

