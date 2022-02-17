import random
from stack import Stack

class MazeGame:
    '''
    A game where a player moves through a grid to reach some treasure.
    '''

    def __init__(self, width, height, player):
        '''
        (MazeGame, Player) -> None
        Construct a new MazeGame with the given width and height,
        and a player. MazeGame should also place a "gold" at
        a randomly chosen coordinate on the far edge of the grid.
        '''
        
        self.width = width
        self.height = height
        self.player = player
        # place the gold at a random spot on the far edge of the grid
        self.gold_coord = (width-1, random.randint(1, height-1)) 

        self.grid = []
        self.make_grid()
        self.undo_stack=Stack()
        
    def make_grid(self):
        '''
        (MazeGame) -> None
        Given width, height and positions of player and gold,
        append things to this maze's grid.
        '''
        
        for i in range(self.height):
            self.grid.append([])
            for j in range(self.width):
                self.grid[i].append('(_)') 
        
        self.grid[self.player.y][self.player.x] = '(x)'
        self.grid[self.gold_coord[1]][self.gold_coord[0]] = '(*)'
    
    def play_game(self):
        '''
        (MazeGame) -> None
        Play the game, with each player taking turns making a move, until
        one player reaches the gold. Players each keep track of their wins and losses.
        '''
        
        # print out the starting state of the maze
        print(self)
        print('------------')
        
        while (not (self.player.x, self.player.y) == \
               (self.gold_coord[0], self.gold_coord[1])):
            # if no one has reached the gold yet, play one turn of the game (one player makes one move)
            self.play_one_turn()

        
        print('Yay, you won, {}!'.format(self.player.name))


    def get_new_position(self, d):
        '''
        (MazeGame, str) -> tuple of two ints or None        
        Given a direction represented as a string "N", "S", "E", or "W" (for moving North,
        South, East or West respectively), return the new position. If the new position is
        not valid (i.e. falls outside of the grid), return None.
        '''

        direction_dict = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
        dx, dy = direction_dict[d]
        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if (0 <= new_x < self.width) and (0 <= new_y < self.height):
            return new_x, new_y
        else:
            return None

    def update_grid(self, new_position):
        '''
        (MazeGame, tuple of two ints) -> None
        Move player to the given new position in grid.
        '''
        # update grid to reflect updated coordinates for current_player
        # keep track of the Player's current position before they move
        old_x, old_y = self.player.x, self.player.y 
        self.player.move(new_position)
        self.grid[self.player.y][self.player.x] = self.grid[old_y][old_x]
        self.grid[old_y][old_x] = '(_)'
        
    def play_one_turn(self):
        '''
        (MazeGame) -> None
        Play one turn of the game. Turn could involve moving one place,
        attempting to move one place, or undoing the most recent move.
        '''

        # get the direction the Player wants to move
        direction = self.player.get_direction() 

        if direction!='U':
            self.undo_stack.push(direction)
            
        if (direction == 'U'):
            direction=self.undo_last_move()
            if direction==None:
                return None                
        
        # this returns None if move is not valid
        new_position = self.get_new_position(direction) 
            
        if new_position: # this is the same as saying "if new_position != None"                
            self.update_grid(new_position)
            print("Player {} moved {}.".format(self.player.name, direction))
        else:
            print("Player {} attempted to move {}. Way is blocked.".format(self.player.name, direction))

        # print current state of game
        print(self)
        print('------------')

    def undo_last_move(self):
        '''
        (MazeGame) -> None
        Update the grid to the state it was in before the previous move was made.
        If no moves were previously made, print out the message "Can't undo".
        '''
        
        # TODO: IMPLEMENT THIS AS DESCRIBED IN INSTRUCTIONS

        try:
            d=self.undo_stack.pop()
            if d=='W':
                d='E'
            elif d=='E':
                d='W'
            elif d=='N':
                d='S'
            elif d=='S':
                d='N'
            return d
        except (ValueError, IndexError, KeyError):
                print("Can't Undo")
                return None
            
    def __str__(self):
        '''
        (MazeGame) -> str
        Return string representation of the game's grid.
        '''
        s = ''
        for row in self.grid:
            s += ''.join(row) + "\n"
        return s.strip()


# TODO: IMPLEMENT PLAYER CLASS AS DESCRIBED IN INSTRUCTIONS
class Player:

    '''A player for the MazeGame'''
    
    def __init__(self,name,x,y):
        
        '''
        (Player, string, int, int) -> None
        Construct a new player with a given name.
        Set the default intial coordinates of the
        player at (0,0).
        '''

        self.name=name
        self.x=x
        self.y=x
        
    def move(self,new_position):

        '''(Player, tuple of two ints) -> None
        Set's the new position of the player
        after every round.
        '''
        
        new_x,new_y=new_position
        self.x=new_x
        self.y=new_y
        
    def get_direction(self):

        '''(Player)->int
        Obtains input from the User for the
        next move and returns it.
        '''
        
        d=input("What's your next move?")
        return d
        
    

def main():
    """Prompt the user to configure and play the game."""

    width = int(input("Width: "))
    height = int(input("Height: "))

    name = input("What is your name? ")
    p1 = Player(name, 0, 0) # make a player at position (0,0)
    
    play_again = True
    while play_again:
        g = MazeGame(width, height, p1)
        g.play_game()
        # reset player locations at end of round
        p1.move((0,0))
        play_again = input('Again? (y/n) ') == 'y'           


if __name__ == '__main__':
    main()
