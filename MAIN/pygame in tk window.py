import tkinter as tk
import pygame
from pygame.locals import *
from spritesheet import Spritesheet
class PygameInTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title("Pygame in Tkinter")

        self.canvas = tk.Canvas(self.master, width=400, height=300)
        self.canvas.pack()

        self.init_pygame()

    def init_pygame(self):
        # Pygame initialization
        pygame.init()

        # Create Pygame screen
        self.pygame_screen = pygame.Surface((400, 300))

        # Create a Pygame clock to control the frame rate
        self.clock = pygame.time.Clock()

        # Start Pygame loop in a separate thread
        self.master.after(100, self.pygame_loop)

    def pygame_loop(self):
        global characterx, charactery, indexl, indexr, indexd, indexu
        global spritel, spriter, sprited, spriteu, display

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            display.fill("grey")
            display.blit(spritel[indexl], (characterx, charactery))
            characterx -= 2
            indexl = ((indexl + 1) % 9)
        elif keys[pygame.K_RIGHT]:
            display.fill("grey")
            display.blit(spriter[indexr], (characterx, charactery))
            characterx += 2
            indexr = ((indexr + 1) % 9)
        elif keys[pygame.K_DOWN]:
            display.fill("grey")
            display.blit(sprited[indexd], (characterx, charactery))
            charactery += 2
            indexd = ((indexd + 1) % 9)
        elif keys[pygame.K_UP]:
            display.fill("grey")
            display.blit(spriteu[indexu], (characterx, charactery))
            charactery -= 2
            indexu = ((indexu + 1) % 9)

        if characterx < -5 or characterx > 1000 or charactery < -5 or charactery > 1024:
            (characterx, charactery) = 0, 0

        # Your additional game logic can go here

        # Continue Pygame loop
        self.master.after(10, self.pygame_loop)

        # Convert Pygame surface to Tkinter PhotoImage
        tk_photo = pygame.image.tostring(self.pygame_screen, 'RGBA')
        img = tk.PhotoImage(width=self.pygame_screen.get_width(), height=self.pygame_screen.get_height())
        img.put(tk_photo)

        # Clear the Canvas
        self.canvas.delete("all")

        # Draw Tkinter PhotoImage on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # Update Tkinter window
        self.master.update()

        # Tick Pygame clock to control the frame rate
        self.clock.tick(30)

if __name__ == "__main__":
    root = tk.Tk()
    app = PygameInTkinter(root)

    # Define your sprite images and variables here
    characterx, charactery = 0, 0
    indexl, indexr, indexd, indexu = 0, 0, 0, 0

    my_spritesheet = Spritesheet("C:/Users/musta/Downloads/New folder (1)/MAIN/GAME/car.png")
    spritel = [my_spritesheet.get_sprite(22, 79, 22, 47), my_spritesheet.get_sprite(83, 80, 25, 46),
               my_spritesheet.get_sprite(149, 79, 22, 46), my_spritesheet.get_sprite(214, 79, 24, 46),
               my_spritesheet.get_sprite(278, 79, 25, 47), my_spritesheet.get_sprite(340, 80, 28, 46),
               my_spritesheet.get_sprite(406, 79, 25, 47), my_spritesheet.get_sprite(470, 79, 24, 47),
               my_spritesheet.get_sprite(534, 79, 23, 47)]  # left

    spriter = [my_spritesheet.get_sprite(20, 207, 22, 47), my_spritesheet.get_sprite(84, 208, 25, 46),
               my_spritesheet.get_sprite(149, 207, 22, 46), my_spritesheet.get_sprite(210, 207, 24, 46),
               my_spritesheet.get_sprite(273, 207, 25, 47), my_spritesheet.get_sprite(336, 208, 28, 46),
               my_spritesheet.get_sprite(401, 207, 24, 47), my_spritesheet.get_sprite(466, 207, 24, 47),
               my_spritesheet.get_sprite(532, 207, 23, 47)]  # right

    sprited = [my_spritesheet.get_sprite(16, 143, 32, 48), my_spritesheet.get_sprite(80, 143, 32, 48),
               my_spritesheet.get_sprite(144, 143, 32, 48), my_spritesheet.get_sprite(208, 144, 32, 48),
               my_spritesheet.get_sprite(272, 143, 32, 49), my_spritesheet.get_sprite(336, 143, 32, 48),
               my_spritesheet.get_sprite(400, 143, 32, 48), my_spritesheet.get_sprite(464, 144, 32, 48),
               my_spritesheet.get_sprite(528, 143, 32, 49)]  # down

    spriteu = [my_spritesheet.get_sprite(16, 143, 32, 48), my_spritesheet.get_sprite(80, 15, 32, 46),
               my_spritesheet.get_sprite(144, 15, 32, 47), my_spritesheet.get_sprite(208, 16, 32, 47),
               my_spritesheet.get_sprite(16, 16, 32, 47), my_spritesheet.get_sprite(336, 16, 32, 48),
               my_spritesheet.get_sprite(400, 16, 32, 48), my_spritesheet.get_sprite(464, 16, 32, 48),
               my_spritesheet.get_sprite(528, 143, 32, 49)]  # up

    display.blit(sprited[4], (characterx, charactery))
    display.blit(pygame.image.load('ba.png'), (0, 100))

    root.mainloop()
