import pygame  # A simple TicTacToe game

pygame.init()
screen = pygame.display.set_mode((400, 500))
run = True

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont("comicsansms", 22)

while run:
    # Initialize Board
    screen.fill(black)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    a1 = pygame.draw.rect(screen, white, (25, 25, 100, 100))
    a2 = pygame.draw.rect(screen, white, (150, 25, 100, 100))
    a3 = pygame.draw.rect(screen, white, (275, 25, 100, 100))
    b1 = pygame.draw.rect(screen, white, (25, 150, 100, 100))
    b2 = pygame.draw.rect(screen, white, (150, 150, 100, 100))
    b3 = pygame.draw.rect(screen, white, (275, 150, 100, 100))
    c1 = pygame.draw.rect(screen, white, (25, 275, 100, 100))
    c2 = pygame.draw.rect(screen, white, (150, 275, 100, 100))
    c3 = pygame.draw.rect(screen, white, (275, 275, 100, 100))
    draw_object = 'rect'
    running = True

    def draw_rect(r1, r2, r11, r22, p11, p12):
        pygame.draw.rect(screen, red, (r1, r2, r11, r22))
        global draw_object
        draw_object = 'circle'
        board[p11][p12] = 1

    def draw_circle(c10, c20, c11, c22, p12, p22):
        pygame.draw.circle(screen, green, (c10, c20), c11, c22)
        global draw_object
        draw_object = 'rect'
        board[p12][p22] = 2

    def check_win():  # Check the winner
        if draw_object == 'rect':
            screen.blit(font.render("Player 2 Won", True, (255, 255, 255)), (50, 400))
            screen.blit(font.render("Press Space to reset", True, (255, 255, 255)), (50, 440))
        else:
            screen.blit(font.render("Player 1 Won", True, (255, 255, 255)), (50, 400))
            screen.blit(font.render("Press Space to reset", True, (255, 255, 255)), (50, 440))


    def check_draw():  # Check for Draw
        screen.blit(font.render("Draw", True, (255, 255, 255)), (50, 400))
        screen.blit(font.render("Press space to reset", True, (255, 255, 255)), (50, 440))


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if draw_object == 'rect':
                    if a1.collidepoint(pos) and board[0][0] == 0:
                        draw_rect(50, 50, 50, 50, 0, 0)
                    if a2.collidepoint(pos) and board[0][1] == 0:
                        draw_rect(175, 50, 50, 50, 0, 1)
                    if a3.collidepoint(pos) and board[0][2] == 0:
                        draw_rect(300, 50, 50, 50, 0, 2)
                    if b1.collidepoint(pos) and board[1][0] == 0:
                        draw_rect(50, 175, 50, 50, 1, 0)
                    if b2.collidepoint(pos) and board[1][1] == 0:
                        draw_rect(175, 175, 50, 50, 1, 1)
                    if b3.collidepoint(pos) and board[1][2] == 0:
                        draw_rect(300, 175, 50, 50, 1, 2)
                    if c1.collidepoint(pos) and board[2][0] == 0:
                        draw_rect(50, 300, 50, 50, 2, 0)
                    if c2.collidepoint(pos) and board[2][1] == 0:
                        draw_rect(175, 300, 50, 50, 2, 1)
                    if c3.collidepoint(pos) and board[2][2] == 0:
                        draw_rect(300, 300, 50, 50, 2, 2)
                elif draw_object == 'circle':
                    if a1.collidepoint(pos) and board[0][0] == 0:
                        draw_circle(75, 75, 35, 35, 0, 0)
                    if a2.collidepoint(pos) and board[0][1] == 0:
                        draw_circle(200, 75, 35, 35, 0, 1)
                    if a3.collidepoint(pos) and board[0][2] == 0:
                        draw_circle(325, 75, 35, 35, 0, 2)
                    if b1.collidepoint(pos) and board[1][0] == 0:
                        draw_circle(75, 200, 35, 35, 1, 0)
                    if b2.collidepoint(pos) and board[1][1] == 0:
                        draw_circle(200, 200, 35, 35, 1, 1)
                    if b3.collidepoint(pos) and board[1][2] == 0:
                        draw_circle(325, 200, 35, 35, 1, 2)
                    if c1.collidepoint(pos) and board[2][0] == 0:
                        draw_circle(75, 325, 35, 35, 2, 0)
                    if c2.collidepoint(pos) and board[2][1] == 0:
                        draw_circle(200, 325, 35, 35, 2, 1)
                    if c3.collidepoint(pos) and board[2][2] == 0:
                        draw_circle(325, 325, 35, 35, 2, 2)
                # Row wise
            if (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or (board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]  # To make sure after win player cannot input anymore
                check_win()
            elif (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or (board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
            elif (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or (board[2][0] == 2 and board[2][1] == -1 and board[2][2] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
                # Column wise
            elif (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
            elif (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
            elif (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
                # Diagonally
            elif (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1) or (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
            elif (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or (board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2):
                board = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
                check_win()
                # Draw
            elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 3 not in board[0]:
                check_draw()
        pygame.display.update()

