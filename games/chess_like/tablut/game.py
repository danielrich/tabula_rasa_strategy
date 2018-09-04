"""
Defines the rules that define the game. Do it in a way that I can use the collection
of agents to develop against. Currently the plan is to just make it some simple python.
Long term this really seems like it should have some sort of DSL that defines the rules.
Turns out this exists GDL. out of stanford. As I look at it I am a titch concerned about
the viability from a performance perspective. They are doing it to play games afresh each time.
I want to use this to evaluate learning speed. Plus have fun. maybe I will come back and
and starting using it, but right now I just want to get something working.
"""

# TODO list
# Start with a super simple cnn value network. so Just evaluate who is going to win
# from a given position.
import numpy as np
# init game
CASTLE_OCCUPIED = 9
CASTLE_UNOCCUPIED = 8
KING = 7
DEFENDER = 6
ATTACKER = 5
GOAL = 4

class TablutGame():

    def __init__(self):
        self.board_state = np.zeros((9,9))
        self.board_state[4][4] = CASTLE_OCCUPIED
        # top attackers
        self.board_state[0][3] = ATTACKER
        self.board_state[0][4] = ATTACKER
        self.board_state[0][5] = ATTACKER
        self.board_state[1][4] = ATTACKER
        # bottom attackers
        self.board_state[8][3] = ATTACKER
        self.board_state[8][4] = ATTACKER
        self.board_state[8][5] = ATTACKER
        self.board_state[7][4] = ATTACKER
        # left attackers
        self.board_state[3][0] = ATTACKER
        self.board_state[4][0] = ATTACKER
        self.board_state[5][0] = ATTACKER
        self.board_state[4][1] = ATTACKER
        # right attackers
        self.board_state[3][8] = ATTACKER
        self.board_state[4][8] = ATTACKER
        self.board_state[5][8] = ATTACKER
        self.board_state[4][7] = ATTACKER
        # top defend
        self.board_state[2][4] = DEFENDER
        self.board_state[3][4] = DEFENDER

        self.board_state[5][4] = DEFENDER
        self.board_state[6][4] = DEFENDER

        self.board_state[4][2] = DEFENDER
        self.board_state[4][3] = DEFENDER

        self.board_state[4][5] = DEFENDER
        self.board_state[4][6] = DEFENDER

        self.turn = DEFENDER# Not sure who goes first. might have to make it random
        self.winner = None

    def get_board_state(self):
        return self.board_state, self.turn, self.winner

# get_board_state

# get_legal_moves
    def get_legal_moves(self):
        """
        Return a list of tuples of tuples. Each move is a tuple consisting of
        a tuple representing the start square tuple and the end square tuple.
        """
        # for each square in the castle figure out if an moves can occur from it.
        moves = []
        allowed = [self.turn]
        if self.turn == DEFENDER:
            allowed.extend((KING, CASTLE_OCCUPIED))
        it = np.nditer(self.board_state, flags=['multi_index'])
        while not it.finished:
            index = it.multi_index
            curr_loc = it[0]
            if curr_loc in allowed:
               moves.extend(self.get_legal_move_piece(curr_loc, index))
            it.iternext()
        return moves

    def get_legal_move_piece(self, piece_type, location):

        legal_moves = []
        if piece_type in [ATTACKER, DEFENDER, CASTLE_OCCUPIED, KING]:

            y,x = location
            new_y, new_x = y, x +1
            # move right
            while new_x < 9 and self.board_state[new_y][new_x] == 0:
                legal_moves.append(((y,x), (new_y, new_x)))
                new_x = new_x +1
            new_y, new_x = y, x -1
            # move left
            while new_x >= 0 and self.board_state[new_y][new_x] == 0:
                legal_moves.append(((y,x), (new_y, new_x)))
                new_x = new_x -1
            new_y, new_x = y -1, x
            # move up
            while new_y >= 0  and self.board_state[new_y][new_x] == 0:
                legal_moves.append(((y,x), (new_y, new_x)))
                new_y = new_y -1

            new_y, new_x = y +1, x
            # move up
            while new_y < 9  and self.board_state[new_y][new_x] == 0:
                legal_moves.append(((y,x), (new_y, new_x)))
                new_y = new_y +1

        return legal_moves

    def make_move(self, the_move):
        old_y, old_x = the_move[0]
        new_y, new_x = the_move[1]
        self.board_state[new_y, new_x] = self.board_state[old_y, old_x]
        self.board_state[old_y, old_x] = 0
        if self.board_state[new_y, new_x] == KING:
            if new_y <=0 or new_y >=8 or new_x <=0 or new_x >=8:
                print("defenders won")
                self.winner = DEFENDER

            if old_y == 4 and old_x == 4:
                self.board_state[old_y][old_x] == CASTLE_UNOCCUPIED

        # check for captures
        # check for win
        it = np.nditer(self.board_state, flags=['multi_index'])
        while not it.finished:
            y, x = it.multi_index
            curr_piece = it[0]
            capture_count = 2
            if curr_piece == CASTLE_OCCUPIED:
                capture_count == 4
            neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
            for new_y, new_x in neighbors:
                if new_y < 0 or new_y >8:
                    continue
                if new_x < 0 or new_x >8:
                    continue
                new_piece = self.board_state[new_y][new_x]
                if curr_piece == ATTACKER:
                    if new_piece != 0 and new_piece != curr_piece:
                        capture_count -= 1
                else:
                    if new_piece != 0 and not (new_piece in [DEFENDER, KING, CASTLE_OCCUPIED]):
                        capture_count -= 1
                if curr_piece == KING: # COULD simplify this
                    if new_piece == CASTLE_UNOCCUPIED:
                        capture_count +=2# fix the damange and help out
                if capture_count <= 0:
                    # TODO handle mutual capture better.
                    if curr_piece == 'KING':
                        print("Attackers won")
                        self.winner = ATTACKER
                    self.board_state[y][x] = 0
            it.iternext()

        # progress the turn.
        if self.turn == DEFENDER:
            self.turn = ATTACKER
        else:
            self.turn = DEFENDER

if __name__ == "__main__":
    game = TablutGame()
    while 1:
        print(game.get_board_state())
        test = game.get_legal_moves()
        print("enter_move")
        move = eval(input())
        if move in test:
            print('lega')
            game.make_move(move)
        import pdb;pdb.set_trace()
