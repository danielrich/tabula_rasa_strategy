import pygame
from game import TablutGame, ATTACKER, DEFENDER

pygame.font.init()

class Game:

    def __init__(self):
        self.game = TablutGame()
        self.window_size = 900
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        self.background = pygame.image.load('resources/grid.png')

    def draw(self):
        board_state, turn, winner = self.game.get_board_state()
        pass

    def event_loop(self):
        # retrieve move

        move = ((0,0), (0,0))
        self.game.make_move(move)

    def start_game(self):
        self.draw()

        while True:
            self.event_loop()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.start_game()
