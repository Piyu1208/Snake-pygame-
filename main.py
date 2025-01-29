import pygame
import random


pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, WIDTH))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
SNAKE_LENGTH = 3

font = pygame.font.Font(None, 50)

class Snake:
    def __init__(self):
        self.dead = False
        self.x = BLOCK_SIZE
        self.y = BLOCK_SIZE
        self.x_dir = 1
        self.y_dir = 0
        

        self.head = pygame.Rect((self.x, self.y), (BLOCK_SIZE, BLOCK_SIZE))
        self.body = [pygame.Rect((self.x-BLOCK_SIZE, self.y), (BLOCK_SIZE, BLOCK_SIZE))]


    
    def update(self):
        for part in self.body:
            if self.head.x == part.x and self.head.y == part.y:
                self.dead = True
            if self.head.x not in range(WIDTH) or self.head.y not in range(HEIGHT):
                self.dead = True


        if snake.dead == True:
            self.dead = False
            self.x = BLOCK_SIZE
            self.y = BLOCK_SIZE
            self.x_dir = 1
            self.y_dir = 0
        

            self.head = pygame.Rect((self.x, self.y), (BLOCK_SIZE, BLOCK_SIZE))
            self.body = [pygame.Rect((self.x-BLOCK_SIZE, self.y), (BLOCK_SIZE, BLOCK_SIZE))]

        

        self.body.append(self.head)

        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.x_dir*BLOCK_SIZE
        self.head.y += self.y_dir*BLOCK_SIZE
        self.body.remove(self.head)

        if self.x not in range(WIDTH):
            self.dead = True

        if self.y not in range(HEIGHT):
            self.dead = True

        
class Apple:
    def __init__(self):
        self.x = BLOCK_SIZE*random.randint(0, (WIDTH//BLOCK_SIZE)-1)
        self.y = BLOCK_SIZE*random.randint(0, (HEIGHT//BLOCK_SIZE)-1)


        self.body = pygame.Rect((self.x, self.y), (BLOCK_SIZE, BLOCK_SIZE))




def grid():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            rect = pygame.Rect((0+x*BLOCK_SIZE, 0+y*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, "gray", rect, 1)




snake = Snake()
apple = Apple()
score = font.render("1", True, (255, 255, 255))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.x_dir != 1:
                snake.x_dir, snake.y_dir = -1, 0
            elif event.key == pygame.K_RIGHT and snake.x_dir != -1:
                snake.x_dir, snake.y_dir = 1, 0
            elif event.key == pygame.K_UP and snake.y_dir != 1:
                snake.x_dir, snake.y_dir = 0, -1
            elif event.key == pygame.K_DOWN and snake.y_dir != 1:
                snake.x_dir, snake.y_dir = 0, 1



    snake.update()

    score = font.render(f"{len(snake.body)}", True, "white")
    
                
    screen.fill("black")
    grid()

    pygame.draw.rect(screen, "red", apple.body)

    pygame.draw.rect(screen, "green", snake.head)
    
    for part in snake.body:
        pygame.draw.rect(screen, "green", part)

    screen.blit(score, (WIDTH/2, 0))

    pygame.display.update()


    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect((part.x, part.y), (BLOCK_SIZE, BLOCK_SIZE)))
        apple  = Apple()
    

    clock.tick(60)






