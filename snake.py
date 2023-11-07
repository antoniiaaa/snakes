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
    snake_pos = [250, 250]
    snake_color = pygame.Color(102, 255, 102)
    snake = pygame.Rect(0, 0, 0.01*screen_rect.width, 0.01*screen_rect.height)
    snake_body = [
        [100, 50],
        [90, 50],
        [80, 50],
        [70, 50]
    ]
    # snake_rect = snake_body.get_rect()
    snake_speed = 10

    direction = 'RIGHT'
    move_to = direction
    # move = True
    # def snake_move():
    #     if move:
    #         snake_pos.x += 5

    def snake_move():
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

    #APEL
    fruit = pygame.image.load("fruit.jpeg")
    fruit_rect = fruit.get_rect()
    fruit_position = [random.randrange(1, (window_x//10)) * 100, random.randrange(1, (window_y//10)) * 100]
    fruit_spawn = True

    #SCORE
    score = 0

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score: " +str(score), True)
        score_rect = score_surface.get_rect()
        screen.blit(score_surface, score_rect)

    start = True
    while True:
        screen.fill([0, 0, 0])
        # screen.blit(fruit, fruit_rect)
        
        # if start:
        #     snake_move()

        for every_event in pygame.event.get():
            # if every_event.type == pygame.QUIT:
            #     sys.quit()
            if every_event.type == pygame.KEYDOWN:
                if every_event.key == pygame.K_UP:
                    move_to = 'UP'
                if every_event.key == pygame.K_DOWN:
                    move_to = 'DOWN'
                if every_event.key == pygame.K_RIGHT:
                    move_to = 'RIGHT'
                if every_event.key == pygame.K_LEFT:
                    move_to = 'LEFT'

        snake_body.insert(0, list(snake_pos))
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
            game_over()

        for pos in snake_body:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        fruit_spawn = False
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (500//10))*10, random.randrange(1, (500//10))*10]

        if snake_pos[0] == fruit_position[0] and snake_pos[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main()