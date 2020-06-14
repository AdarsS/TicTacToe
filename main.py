#!/usr/bin/env python3
'''
    simple TicTacToe game
'''
# Import
import pygame
import os

## Global variables
# Initalize board
pygame.display.init()
screen = pygame.display.set_mode((600, 750))
box_colour = (255, 255, 255)
a1 = pygame.draw.rect(screen, box_colour, (25, 25, 150, 150))
a2 = pygame.draw.rect(screen, box_colour, (225, 25, 150, 150))
a3 = pygame.draw.rect(screen, box_colour, (425, 25, 150, 150))
b1 = pygame.draw.rect(screen, box_colour, (25, 225, 150, 150))
b2 = pygame.draw.rect(screen, box_colour, (225, 225, 150, 150))
b3 = pygame.draw.rect(screen, box_colour, (425, 225, 150, 150))
c1 = pygame.draw.rect(screen, box_colour, (25, 425, 150, 150))
c2 = pygame.draw.rect(screen, box_colour, (225, 425, 150, 150))
c3 = pygame.draw.rect(screen, box_colour, (425, 425, 150, 150))
pygame.display.set_caption("TicTacToe")

# Set Players
base_dir = os.path.dirname(__file__)
x = pygame.image.load(base_dir+"/images/X.png")
o = pygame.image.load(base_dir+"/images/O.png")
players = {1: [x,1], -1: [o,2]}
current_player = 1

# Keeps track of all turns
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  

# To Display who won
pygame.font.init()
font = pygame.font.SysFont("comicsansms", 22)

def game_over(nodraw=True):
    screen.blit(font.render(f"Player {players[current_player][1]} it's your turn", True, (pygame.Color("black"))), (50, 600)) 
    if nodraw:
        game_rover = font.render(f"Player {players[current_player][1]}  won", True, (255, 255, 255))
    else:
        game_rover = font.render(f"Draw!!!", True, (255, 255, 255))
    screen.blit(game_rover, (50, 600))

def check_win():
      # Row wise
        if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or (board[0][0] == -1 and board[0][1] == -1 and board[0][2] == -1):
            pygame.draw.line(screen, (0, 0, 0), (0, 100), (600, 100), 9)
            game_over()
        elif (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or (board[1][0] == -1 and board[1][1] == -1 and board[1][2] == -1):
            pygame.draw.line(screen, (0, 0, 0), (0, 300), (600, 300), 9)
            game_over()
        elif (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or (board[2][0] == -1 and board[2][1] == -1 and board[2][2] == -1):
            pygame.draw.line(screen, (0, 0, 0), (0, 500), (600, 500), 9)
            game_over()

        # Coloumn wise
        elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][0] == -1 and board[1][0] == -1 and board[2][0] == -1):
            pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 600), 9)
            game_over()
        elif (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][1] == -1 and board[1][1] == -1 and board[2][1] == -1):
            pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 600), 9)
            game_over()
        elif (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or (board[0][2] == -1 and board[1][2] == -1 and board[2][2] == -1):
            pygame.draw.line(screen, (0, 0, 0), (500, 0), (500, 600), 9)
            game_over()

        # Diagonally
        elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[0][0] == -1 and board[1][1] == -1 and board[2][2] == -1):
            pygame.draw.line(screen, (0, 0, 0), (0, 0), (600, 600), 9)
            game_over()
        elif (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or (board[0][2] == -1 and board[1][1] == -1 and board[2][0] == -1):
            pygame.draw.line(screen, (0, 0, 0), (600, 0), (0, 600), 9)
            game_over()

        # Draw
        elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
            game_over(False)
        
        else: return True
    
def turn(pos):
    if a1.collidepoint(pos) and board[0][0] == 0:
        screen.blit(players[current_player][0], (50, 50))
        board[0][0] = current_player
    elif a2.collidepoint(pos) and board[0][1] == 0:
        screen.blit(players[current_player][0], (250, 50))
        board[0][1] = current_player
    elif a3.collidepoint(pos) and board[0][2] == 0:
        screen.blit(players[current_player][0], (450, 50))
        board[0][2] = current_player
    elif b1.collidepoint(pos) and board[1][0] == 0:
        screen.blit(players[current_player][0], (50, 250))
        board[1][0] = current_player
    elif b2.collidepoint(pos) and board[1][1] == 0:
        screen.blit(players[current_player][0], (250, 250))
        board[1][1] = current_player
    elif b3.collidepoint(pos) and board[1][2] == 0:
        screen.blit(players[current_player][0], (450, 250))
        board[1][2] = current_player
    elif c1.collidepoint(pos) and board[2][0] == 0:
        screen.blit(players[current_player][0], (50, 450))
        board[2][0] = current_player
    elif c2.collidepoint(pos) and board[2][1] == 0:
        screen.blit(players[current_player][0], (250, 450))
        board[2][1] = current_player
    elif c3.collidepoint(pos) and board[2][2] == 0:
        screen.blit(players[current_player][0], (450, 450))
        board[2][2] = current_player

def main():
    # local variables
    loop = True
    global current_player
    screen.blit(font.render("Player 1 it's your turn", True, (255, 255, 255)), (50, 600))  
    screen.blit(font.render("Press <Space> to quit", True, (255, 255, 255)), (50, 650))  
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(board)
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(font.render(f"Player {players[current_player][1]} it's your turn", True, (pygame.Color("black"))), (50, 600))                  
                turn(pygame.mouse.get_pos())
                check = check_win()
                # Change Player
                if check:
                    current_player *= -1
                    screen.blit(font.render(f"Player {players[current_player][1]} it's your turn", True, (255, 255, 255)), (50, 600))  
                
            pygame.display.update()

if __name__ == "__main__":
    main()
