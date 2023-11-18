import sys
import pygame
import random
import time

def main():
    pygame.init()
    window_x = 500
    window_y = 500
    screen = pygame.display.set_mode([500, 500])
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Snake Game')
    fps = pygame.time.Clock()


    #SNAKE
    snake_pos = [250, 50]
    snake_color = pygame.Color(102, 255, 102)
    snake = pygame.Rect(0, 0, 0.01*screen_rect.width, 0.01*screen_rect.height)
    snake_body = [
        [100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
    ]
    snake_speed = 20

    direction = 'RIGHT'
    move_to = direction

    def snake_move():
        global fruit_spawn, fruit_position
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10


    #APEL
    # fruit = pygame.image.load("fruit.jpeg")
    # fruit_rect = fruit.get_rect()
    fruit_position = [0, 0]
    fruit_spawn = False

    #SCORE
    score = 0
    score_label = pygame.font.Font("fonts\BirdyGame.ttf", 25)
    score_image = score_label.render(str(f"SCORE: {score}"), True, (255, 255, 255))
    score_image_rect = score_image.get_rect()
    score_image_rect.topleft = screen_rect.topleft
    score_image_rect.y += 10
    score_image_rect.x += 10

    def snake_eat():
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == fruit_position[0] and snake_pos[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score: " +str(score), True)
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

    #BUTTON
    button = pygame.image.load("play_button.png")
    button_rect = button.get_rect()
    button = pygame.transform.scale(button, (0.1*screen_rect.width, 0.1*screen_rect.height))
    button_rect = button.get_rect()
    button_rect.center = screen_rect.center

    #GAME OVER
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('GAME OVER', True, (168, 17, 0))
        # game_over_surface = my_font.render('Highscore' + str(score), True, (168, 17, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/3)
        screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(1)
        pygame.quit()
        quit()

    start = False
    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_to = 'UP'
                if event.key == pygame.K_DOWN:
                    move_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    move_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    move_to = 'RIGHT'

        if move_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if move_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if move_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if move_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if start:
            screen.blit(score_image, score_image_rect)
            snake_move()
            snake_eat()
        else:
            screen.blit(title_label_image, title_label_image_rect)
            screen.blit(button, button_rect)

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == fruit_position[0] and snake_pos[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()
        
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x//20)) * 10, random.randrange(1, (window_y//20)) * 10]
            fruit_spawn = True
            
        screen.fill([0,0,0])
        
        for pos in snake_body:
            pygame.draw.rect(screen, [102, 255, 102], pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, [102, 255, 102], pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            game_over()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main()