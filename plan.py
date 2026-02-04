'''
position 
get key
if keydown "left arrow"
    move position left 

if keydown "right arrow"
    move position right

'''
import pygame

#screen display
pygame.init()
WIDTH, HEIGHT, = 640, 480
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing")

clock = pygame.time.Clock()

#colors
BLACK = (0, 0, 0)

screen.fill(BLACK)

#create sprite
player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 1, 30, 30)
coin_circl = pygame.Rect(WIDTH // 2, HEIGHT // 5, 10, 10)

pygame.draw.rect(player_rect)
    
if event.type == pygame.KEYDOWN:
    
    if event.key == pygame.K_LEFT:
            player_rect.x 
    
    if event.key == pygame.K_RIGHT:
            player_rect.x 
            

class FallingCoin:
    def __init__(self, file, x, y, width, height):
        self.file = file
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load(self.file).convert_alpha(), (self.width, self.height))

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

falling_coin = FallingCoin ('Coin.jpg', 300, -100, 50, 100)

run = True
while run:

clock.tick (60)
falling_coin.y += 25
if falling_coin.y > 600:
    falling_coin
