import random_selector as rs
import pygame

# colors
WHITE = (255, 255, 255)
DARK_GREY = (25, 25, 25)
MIDDLE_GREY = (125, 125, 125)
LIGHT_GREY = (200, 200, 200)
BLACK = (0, 0, 0)

BLUE = (0,0,255)
LIGHT_BLUE = (90,90,255)
GREEN = (0,255,0)
LIGHT_GREEN = (150, 255, 150)
RED = (255,0,0)
LIGHT_RED = (255, 90, 90)
YELLOW = (255,255,0)
LIGHT_YELLOW = (200, 200, 90)


class Program:

    def __init__(self):

        # window detials
        self.x, self.y = pygame.display.set_mode().get_size()
        self.screen =  pygame.display.set_mode(((500), (500)),pygame.RESIZABLE)
        pygame.display.set_caption("Random Gift Generator")
        self.fps = pygame.time.Clock()

        # font name
        self.font_small = pygame.font.SysFont("arail",40)


    def render(self):
        self.red_button = pygame.Rect((self.screen.get_width() // 2 - 150), \
                                       (self.screen.get_height() - 100), 150, 50)
        
        #Labelinng the buttons
        self.exit_text = self.font_small.render("EXIT", True, BLACK)
        self.exit_text_Rect = self.exit_text.get_rect()
        self.exit_text_Rect.x, self.exit_text_Rect.y = (self.screen.get_width() // 2 - 110), \
                                                        (self.screen.get_height() - 86)
    
    def processInput(self):
        pass

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.red_button.collidepoint(event.pos):#red_button
                    pygame.quit()


    def draw(self):
        self.screen.fill(WHITE)
        # hovering function over the buttons to show interaction
        if self.red_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, RED, self.red_button)
            self.exit_text = self.font_small.render("EXIT", True, WHITE)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.red_button)

        #Labeling for them buttons
        self.screen.blit(self.exit_text, self.exit_text_Rect)


    def run(self):
        while True:
            self.render()
            self.processInput()
            self.update()
            self.draw()
            pygame.display.flip()
            self.fps.tick(30)

if __name__ == "__main__":
    pygame.init()
    program = Program()
    program.run()
    print("end")
    pygame.quit()