import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mol_x = 0
        mol_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    #get row and col of mouse
                    mouse_row = mouse_x//32
                    mouse_col = mouse_y//32
                    #get row and col of mole
                    mole_row = mol_x//32
                    mole_col = mol_y//32

                    if mole_row == mouse_row and mole_col == mouse_col:
                        mol_x = random.randrange(0, 20) * 32
                        mol_y = random.randrange(0, 16) * 32

            #fill screen
            screen.fill("light green")

            # drawing row lines
            #rows
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, (i * 32)), (640, (i * 32)))
            #cols
            for i in range(20):
                pygame.draw.line(screen, "dark green", ((i * 32), 0), ((i * 32), 512))

            #add mole image
            screen.blit(mole_image, mole_image.get_rect(topleft=(mol_x, mol_y)))

            #updating screen
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()