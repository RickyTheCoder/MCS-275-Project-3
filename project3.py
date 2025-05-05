# I hereby attest that I have adhered to the rules for quizzes and projects as well as UIC’s
# Academic Integrity standards. Signed: Ricky Rivera
# Ricky Rivera
# UIN: 678343651


import random
class PuzzlePiece:

    def __init__(self, x = None, y = None):
        self.secret_id = (x , y)
        # 'secret_id' will hold the true grid position 
        self.connected_to = []
        # each piece will have its own list

    def __str__(self):
        return str(self.secret_id)
        # coordinates will be revealed when printing a piece

# this class will create a whole puzzle that we will solve 
class Puzzle:

    def __init__(self):
        self.u_pieces = [PuzzlePiece(x, y) for x in range(10) for y in range(10)]
        # list of all 'PuzzlePiece' objects in our puzzle 
        self.s_pieces = []
        # empty list where we will add pieces later

    def get_rand_piece(self):
        return random.choice(self.u_pieces)
        # return a random 'PuzzlePiece' from the 'u_pieces' attribute 
    
    def solve_one_piece(self):
        # this method will represent the whole process of adding one pieces
        # to the 'solved' cluster of puzzle pieces 
        
        if not self.s_pieces:
            # if 's_pieces' is an empty list, choose a random pieces from unsolved pile
            p = self.get_rand_piece()
            # get the 'get_rand_piece' method to get a random piece
            self.u_pieces.remove(p)
            # piece removed from the 'u_pieces' attribute
            self.s_pieces.append(p)
            # appended to 's_pieces' attribute
            return
        
        while True:
            # while 's_pieces' is not empty
            candidate = self.get_rand_piece()
            # choose a random piece from unsolved pile until we find one that can
            # be connected to one of the solved pieces 
            neighbors = [
                s for s in self.s_pieces
                # iterate over already solved pieces
                if abs(candidate.secret_id[0] - s.secret_id[0]) + abs(candidate.secret_id[1] - s.secret_id[1]) == 1]
                # calculating the Manhattan distance 
                # (sum of absoulate differences in 'x' and in 'y')
            if neighbors:
                    # if atleast one adjacent piece was found
                    for s in neighbors:
                        candidate.connected_to.append(s)
                        # append 's' so new piece is touching 's'
                        s.connected_to.append(candidate) 
                        # append so each existing pieces knows its touching the new piece
                    # move the candidate
                    self.u_pieces.remove(candidate)
                    self.s_pieces.append(candidate)
                    # take connected 'candidate' out of unsolved pool
                    return
                    # exits since successfullu placed one piece
                
    def solve_all_pieces(self):
        # implements the 'solve_one_piece' method repeatedly until the 'u_pieces'
        # attribute is empty
        if not self.u_pieces: # base case
            return 
        self.solve_one_piece()
        self.solve_all_pieces()
        # solve one piece, then recurse

if __name__ == "__main__":
    random.seed(42)
    puzzle = Puzzle()
