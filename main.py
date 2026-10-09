import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First APK")

font = pygame.font.Font(None, 42)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 30, 50))

    text = font.render("ANIMAL BATTLE!", True, (0, 255, 100))
    screen.blit(text, text.get_rect(center=(300, 160)))

    pygame.draw.rect(screen, (0, 150, 255), (200, 220, 200, 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
